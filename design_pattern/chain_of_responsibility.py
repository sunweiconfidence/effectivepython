from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass
    
    @abstractmethod
    def set_content(self, content):
        pass
    
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r')
        self.content = f.read()
        f.close()
    
    def get_content(self):
        return self.content
    
    def set_content(self, content):
        f = open(self.filename, 'w')
        f.write(content)
        f.close()

class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None
    
    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()
    
    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)
        

subj = VirtualProxy("test.txt")
print(subj.get_content())