#!/usr/bin/python

import string
import random
from sys import argv

fo = open("pss.txt", "a+")
#script, filename = argv

target = open("pss.txt", "a+")
print "Type in your username: "
name = raw_input("> ")
target.write(name)
target.write(" - ")
print "How long would you like your password(Please choose between 6-16)"
num = raw_input("> ")

def id_generator6(size=6, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator7(size=7, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator8(size=8, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator9(size=9, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator10(size=10, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator11(size=11, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator12(size=12, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator13(size=13, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator14(size=14, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator15(size=15, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

def id_generator16(size=16, chars=string.ascii_uppercase + string.lowercase + string.digits + '!@#$%^&*()'):
    return "".join(random.choice(chars) for _ in range(size))

if num == "6":
    print id_generator6()
    target.write(id_generator6())
    target.write("\n")    
elif num == "7":
    print id_generator7()
    target.write(id_generator7())
    target.write("\n")    
elif num == "8":
    print id_generator8()
    target.write(id_generator8())
    target.write("\n")    
elif num == "9":
    print id_generator9()
    target.write(id_generator9())
    target.write("\n")    
elif num == "10":
    print id_generator10()
    target.write(id_generator10())
    target.write("\n")    
elif num == "11":
    print id_generator11()
    target.write(id_generator11())
    target.write("\n")    
elif num == "12":
    print id_generator12()
    target.write(id_generator12())
    target.write("\n")    
elif num == "13":
    print id_generator13()
    target.write(id_generator13())
    target.write("\n")    
elif num == "14":
    print id_generator14()
    target.write(id_generator14())
    target.write("\n")    
elif num == "15":
    print id_generator15()
    target.write(id_generator15())
    target.write("\n")    
elif num == "16":
    print id_generator16()
    target.write(id_generator16())
    target.write("\n")    
else:
    print "Please choose between 6 and 16 and run again"

target.close()