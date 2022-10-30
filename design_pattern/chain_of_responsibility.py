from abc import ABCMeta, abstractmethod
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass
    
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" %day)
        else:
            print("你还是辞职吧")

class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()
        
    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%d天" %day)

class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()
    
    def handle_leave(self, day):
        if day <= 1:
            print("项目主管准假%d天" %day)
        else:
            print("项目主管职权不足")
            self.next.handle_leave(day)

# Client
day = 4
h = ProjectDirector()
h.handle_leave(day)
