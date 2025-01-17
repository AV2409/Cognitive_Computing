# 3
import random

def isPrime(n):
  for i in range(2,n):
    if(n%i==0):
      return False
  return True

arr=[]
for i in range(100):
  num=random.randint(100,900)
  arr.append(num)

even_count=0
odd_count=0
prime_count=0
prime_arr=[]
even_arr=[]
odd_arr=[]
for i in arr:
  if(i%2==0):
    even_count+=1
    even_arr.append(i)
  else:
    odd_count+=1
    odd_arr.append(i)

  if(isPrime(i)):
    prime_count+=1
    prime_arr.append(i)

print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")
print(f"Prime count: {prime_count}")
print(f"Even numbers: {even_arr}")
print(f"Odd numbers: {odd_arr}")
print(f"Prime numbers: {prime_arr}")