# 7.1 
file_name = "example.txt"
with open(file_name, "w") as file:
    file.write("Hello, this is the first line of the file.\n")

with open(file_name, "r") as file:
    content = file.read()

print("Content of the file:")
print(content)

# 7.2
with open(file_name, "a") as file:
    file.write("Appending a new line to the file.\n")

with open(file_name, "r") as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)

# 7.3
with open(file_name, "r") as file:
    line_count = sum(1 for line in file)

print(f"The file '{file_name}' contains {line_count} lines.")