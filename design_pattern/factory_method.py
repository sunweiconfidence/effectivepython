from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei
    def pay(self, money):
        if self.use_huabei:
            print("花呗支付 %d" %money)
        else:
            print("阿里支付%d" %money)
    
class Wechatpay(Payment):
    def pay(self, money):
        print("微信支付%d" %money)

class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechatpayFactory(PaymentFactory):
    def create_payment(self):
        return Wechatpay()

class HuabeipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

# client
pf = HuabeipayFactory()
p = pf.create_payment()
p.pay(120)