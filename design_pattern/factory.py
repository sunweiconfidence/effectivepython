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
        
class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return Wechatpay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            raise TypeError(f"No such payment named {method}")

pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)