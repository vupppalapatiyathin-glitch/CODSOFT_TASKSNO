#PASSWORD GENERATOR python 
import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
symbols="!#$%^&*()"
string=upper+lower+numbers+symbols
length=int(input("enter the password length: "))
password="".join(random.sample(string, length))
print("your password is: ",password)