import random
import string

pass_len=int(input("Enter the length of the password:"))
charvalues= string.ascii_letters + string.digits + string.punctuation

Password=""
for i in range(pass_len):
    Password += random.choice(charvalues)

print("Your Password is generated:",Password)
