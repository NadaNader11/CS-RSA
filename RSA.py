import random 
import math  
import time

def is_prime(n):
    if n < 2:
        raise ValueError("Number is not prime")
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            raise ValueError("Number is not prime")
    return True

def check_m_smaller_than_n(m, n):
    if m >= n:
        print("Invalid input m must be smaller than n")
        raise ValueError("m must be smaller than n")
    else:
        return True
 
size= int(input("Operate using 16-bit or 8-bit? (Enter 8 or 16)"))
if size != 8:
    if size != 16:
        raise ValueError("Number should be 8 or 16")
q= int(input("enter a prime number"))
print(is_prime(q))
p= int(input("enter a prime number"))
print(is_prime(p))
n = q*p
m = int(input("Enter the number you'd like to encrypt"))
check_m_smaller_than_n(m, n)
if m > 255 and size == 8:
    raise ValueError(f"{m} is not an 8-bit number")
if m > 65535 and size == 16:
    raise ValueError(f"{m} is not an 16-bit number")
eul = (p - 1) * (q - 1)
e = int(input("enter the public exponent")) 
factors = []
def bits():



    def factor_modulus(n):
     factors = []
    for i in range (2, n):
       while n % i == 0:
                factors.append(i)  
                n //= i
    while True:
        if n == 1:
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

def factor_modulus():
    def private_exponent(e, p, q):
        eul = (p - 1) * (q - 1)
    start = time.perf_counter
    d = pow(e, -1, eul)
    End = time.perf_counter
    runtime = End - start
    
    return d, runtime
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

def brute_force_private_exponent(e, phi_n):
    d = 2 
    while True: 
        if (d * e) % phi_n == 1:
            # start2 = time.perf_counter()
            return d 
        # end2= time.perf_counter() 
        d += 1

        
# def choose_bit_length():
#     # def generate_test_cases():
#         def generate_prime(): 
#             def test_cases():
#                  for bits in [8, 16]:
#                     while True:
#                      choice = input("Choose the bit length (8 or 16)")
#                      if choice in ['8', '16']:
#                         return int(choice)
#                      else: 
#                         print("Invalid please enter a number of 8 or 16")
#                         test_cases = []
#             p = generate_prime(bits)
#             q = generate_prime(bits)
#             N = p * q 
#             e = 3
#             test_cases.append((N, e))
#             return test_cases


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

start = time.perf_counter()
d=pow(e,-1,eul)
End = time.perf_counter()
runtime = End - start
print(f"The time taken to get d is {runtime}")
print(f"public{e,n}")
print(f"private{d,n}")

c=pow(m,e,n)
M=pow(c,d,n)
print(m,c,M)







