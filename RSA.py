import random 
import math  

def is_prime(n):
    if n < 2:
        raise ValueError("Number is not prime")
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            raise ValueError("Number is not prime")
    return True
 

q= int(input("enter a prime number"))
print(is_prime(q))
p= int(input("enter a prime number"))
print(is_prime(p))
n = q*p 
eul = (p - 1) * (q - 1)
e = int(input("enter the public exponent")) 
factors = []

def factor_modulus(n):
    factors = []
    for i in range (2, N):
       while N % i == 0:
                factors.append(i)  
                N //= i
    while True:
        if N == 1:
            break 
        else:
           return factor_modulus



# def input_prime(prompt):
#     while True:
#         num = int(input(prompt))
#         if is_prime(num):
#             return num 
#         print("Invalid input. Please enter a prime number.")


# def prime_numbers(x):
#     if x <= 1:
#         return False
#     for i in range(2, n // 2+1):
#         if x % i == 0:
#             return True
#         else:
#             return False 
# print(prime_numbers(q))
     
    
def private_exponent(e, p, q):
    eul = (p - 1) * (q - 1)
    d = pow(e, -1, eul)
    return d 
eul = (p - 1) * (q - 1)
d = pow(e, -1, eul)
def public_exponent():
    e = int(input("Enter the public exponenet"))
    N = int(input("Enter the modulus") )  

    factors = factor_modulus(N)

def extended_gcd(a,b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1 
    return a, x0, y0
e = 17 
phi_n = 40 
gcd, x, y = extended_gcd(e, phi_n)

 
def gcd(a, b):
    while b != 0:
     a,b = b,a%b 
    return a

while e < eul:
    if gcd(e,eul)==1:
        break
    else:
        e+=1



def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a//b) * y1
    return gcd, x, y

def modular_inverse(e, phi_n):
    gcd, x, = extended_euclidean_algorithm
    if gcd == 1:
        return x % phi_n 
    else: 
        raise ValueError("No modular inverse exists")


d=pow(e,-1,eul)
print(f"public{e,n}")
print(f"private{d,n}")
m=11
c=pow(m,e,n)
M=pow(c,d,n)
print(m,c,M)








