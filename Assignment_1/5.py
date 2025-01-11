# 5.1 
numbers = [3,8,66,44,99]
print(max(numbers))
print(min(numbers))
print("------------------------")

# 5.2 
dict_example = {"a": 13, "b": 21, "c": 35}
print(dict_example.get("c"))
print("------------------------")

# 5.3
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print("------------------------")

# 5.4
dict1 = {"x": 10, "y": 20}
dict2 = {"z": 30}

dict3 = dict1.copy()
for key, value in dict2.items():
    dict3[key] = value

print(dict3)

