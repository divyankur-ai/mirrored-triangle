rows = int(input("enter the number of rows: "))
for i in range(2, rows +2):
    print(" " *(rows - 1), end="")
    print("*" * i)