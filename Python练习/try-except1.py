##try:
##    open("abc.txt",'r')
##except IOError:
##        pass
##    
##
##try:
##    print aa
##except IOError:
##    pass

try:
    print aa
except NameError,msg:
    print msg
    
