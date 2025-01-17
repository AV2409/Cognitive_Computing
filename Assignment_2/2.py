# 2
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

# 2-i
maxi=max(scores)
print("Max Score: ", maxi)
print("Max Score index: ", scores.index(maxi))
print()

# 2-ii
mini=min(scores)
print("Min Score: ", mini)
print("Min Score count: ", scores.count(mini))

# 2-iii
l = list(scores[::-1])
print(l)

# 2-iv
key=int(input("Enter the key: "))
if key in scores:
    print(f"First occurance of {key} at:", scores.index(key))
else:
    print(f"{key} not found in the list")