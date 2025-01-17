# 5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary":8000,
    "city": "New York"
}

print("Before changing:", sample_dict)
print()
sample_dict["location"] = sample_dict.pop("city")
print("After changing:", sample_dict)