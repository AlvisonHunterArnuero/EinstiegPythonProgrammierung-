import math

print("Calculates LCM of two numbers \n ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = (math.gcd(a,b))
lcm = str(a*b/gcd)
print("LCM = "+ lcm)
input("\nPress enter to continue..")
