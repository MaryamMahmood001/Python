n = int(input("Enter the number of terms: "))
a = 0
b = 1
if n == 1:
    print(a)
elif n == 2:
    print(a,b)
else:
    print(a,b,end = " ", sep = " ")
    for i in range(0, n+1):
        c = a + b
        print(c, end = " ")
        a = b
        b = c
        

