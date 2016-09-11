__metaclass__ = type
class Myclass:
    def smeth():
        print'this is a static method'
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print 'this is a class method of', cls
    cmeth = classmethod(cmeth)
    

##__metaclass__ = type
##Class 11111:
##    @staticmethod
##    def smeth():
##        print 'This is a static method'
##    @classmethod
##    def cmeth(cls):
##        print 'This is a class method of.' cls
