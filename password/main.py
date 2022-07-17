import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "123456789"
symbol = "!@#$%^&*()-_=+"

ans = lower + upper + num + symbol

length = 9

password = "".join(random.sample(ans,length))

print("Your new strong password is ",password)