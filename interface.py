from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元" %money)

class WeChatpay(Payment):
    def pay(self, money):
        print("微信支付%d元" %money)

p=WeChatpay()
p.pay(100)


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass
    
class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass

class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class Tiger(LandAnimal):
    def walk(self):
        print("老虎走路")