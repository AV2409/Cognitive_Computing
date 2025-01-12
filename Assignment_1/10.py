import sys

# 10.1 
if len(sys.argv) > 2:
    num1, num2 = int(sys.argv[1]), int(sys.argv[2])
    print(num1 + num2)
# to run the file type the following in the terminal for mac OS
# python3 10.py 10 20  

# 10.2 
if len(sys.argv) > 1:
    input_string = sys.argv[1]
    print(len(input_string))
# to run the file type the following in the terminal for mac OS
# python3 10.py abcd 