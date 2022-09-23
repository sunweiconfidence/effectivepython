from abc import ABCMeta, abstractmethod

class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg
    
    def __str__(self):
        return f"{self.face} {self.body} {self.arm} {self.leg}"

class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass
    
    @abstractmethod
    def build_body(self):
        pass
    
    @abstractmethod
    def build_arm(self):
        pass
    
    @abstractmethod
    def build_leg(self):
        pass

class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    
    def build_face(self):
        self.player.face = "漂亮脸蛋儿"
    
    def build_body(self):
        self.player.body = "苗条"
    
    def build_arm(self):
        self.player.arm = "美丽胳膊"
    
    def build_leg(self):
        self.player.leg = "大长腿"

class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    
    def build_face(self):
        self.player.face = "怪兽脸"
    
    def build_body(self):
        self.player.body = "怪兽身材"
    
    def build_arm(self):
        self.player.arm = "长毛的胳膊"
    
    def build_leg(self):
        self.player.leg = "长毛的腿"

class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player

#client
builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)
print(p)

        