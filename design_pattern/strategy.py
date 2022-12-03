from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass
    
class FastStrategy(Strategy):
    def execute(self, data):
        print(f"use faster speed to deal with%s" % data)
        
class SlowStrategy(Strategy):
    def execute(self, data):
        print(f"use slower speed to deal with%s" % data)

class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def do_strategy(self):
        self.strategy.execute(self.data)

# Client
data = "[...]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()