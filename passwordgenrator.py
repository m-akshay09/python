import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
symbole = "*@./"

genrate = lower+upper+digit+symbole
length = int(input("Enter Your Password Length: "))
password ="".join(random.sample(genrate,length))
print(password)