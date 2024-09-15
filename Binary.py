# program to convert
# decimal Number
# to binary

def binary(n):
    if n > 1:
        binary(n//2)
    print(n%2,end="") 
num = int(input("num: "))

bin = binary(num)
