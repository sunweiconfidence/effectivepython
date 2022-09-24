from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print("阿里支付%d" %money)

class Wechatpay(Payment):
    def pay(self, money):
        print("微信支付%d" %money)

class Bankpay:
    def cost(self, money):
        print("银行卡支付%d元" %money)

class Applepay:
    def cost(self, money):
        print("苹果支付%d元" %money)

# 类适配器
class NewBankpay(Payment, Bankpay):
    def pay(self, money):
        self.cost(money)

# p = NewBankpay()
# p.pay(1000)

class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment
    def pay(self, money):
        self.payment.cost(money)

# 组合
p = PaymentAdapter(Applepay())
p.pay(150)


        