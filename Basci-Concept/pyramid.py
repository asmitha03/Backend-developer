def print_pyramid(s):
    for i in range(s):
        print(" " * (s - i - 1) + "*" * (2 * i + 1))
num=int(input("Enter number of rows:"))
print_pyramid(num)