# 6.1 
str1="This is a TEST STRING"
vowels = "aeiouAEIOU"
count = 0
for char in str1:
    if char in vowels:
        count += 1

print(count) 

# 6.2 
str2="abcd"
rev_str=str2[::-1]
print(rev_str)

# 6.3 
str3="abcdcba"
rev_s=str3[::-1]
if str3==rev_s:
    print("It is a palindrome")
else:
    print("It is not a palindrome")