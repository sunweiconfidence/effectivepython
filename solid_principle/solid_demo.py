'''
里式替换原则
'''
class User:
    def show_name(self):
        pass
    
class VIPUser(User):
    def show_name(self):
        pass

def show_user(u):
    res = u.show_name()