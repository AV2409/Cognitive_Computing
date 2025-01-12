import random

# 9.1 
rand_list=[]
n=5
for i in range(n):
    rand_list.append(random.randint(1,100))
print(rand_list)

# 9.2 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True
random_number = random.randint(1, 100)
if (is_prime(random_number)):
    print(f"{random_number} is a prime number")
    
else:
    print(f"{random_number} is not a prime number")

# 9.3 
print(random.randint(1, 6))

# 9.4 
list_numbers = [1, 2, 3, 4, 5]
random.shuffle(list_numbers)
print(list_numbers)

# 9.5 
print(random.choice(list_numbers))

# 9.6 
def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    pwd=''
    for i in range(0,length):
        pwd += random.choice(chars)
    
    return pwd  
print(generate_password(8))

# 9.7 
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []
for suit in suits:
    for value in values:
        deck.append(f"{value} of {suit}")

print(random.choice(deck))