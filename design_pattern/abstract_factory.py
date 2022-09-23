from abc import ABCMeta, abstractmethod

# -----抽象产品--------------------------------
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# --------抽象工厂------------------------
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass
    @abstractmethod
    def make_cpu(self):
        pass
    @abstractmethod
    def make_os(self):
        pass
    
#-----具体产品--------------------------------------------------------
class SmallmiShell(PhoneShell):
    def show_shell(self):
        print("小米 手机壳")

class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果 手机壳")

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙 CPU")

class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科 CPU")

class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果 CPU")

class AndroidOS(OS):
    def show_os(self):
        print("Android 操作系统")

class AppleOS(OS):
    def show_os(self):
        print("苹果 操作系统")

#-----具体工厂------------------
class XiaomiFactory(PhoneFactory):
    def make_shell(self):
        return SmallmiShell()
    def make_cpu(self):
        return SnapDragonCPU()
    def make_os(self):
        return AndroidOS()

class IPhoneFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()
    def make_cpu(self):
        return AppleCPU()
    def make_os(self):
        return AppleOS()


#-----客户端-----------
class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell
    
    def show_info(self):
        print("手机信息:")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)

p1 = make_phone(XiaomiFactory())
p1.show_info()
    



