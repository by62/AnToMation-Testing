class Calculator:
    def calculate(self, expreesion):
        self.value = eval(expreesion)
class Talker:
    def talk(self):
        print 'Hi, My value is ', self.value
class TalingCalculator(Calculator,Talker):
    pass
