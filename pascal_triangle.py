n = int(input("Enter no. of rows: "))
for i in range(1, n + 1):
    x = 1
    for j in range(1, i + 1):
        print(x, end = " ")
        x = int(x * (i - j) / j)
    print()

