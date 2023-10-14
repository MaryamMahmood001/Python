def add(n1, n2):
    x  = n1 + n2
    return x

def subtr(n1, n2):
    if n1 >= n2:
        x = n1 - n2
    else:
        x = n2 - n1
    return x

def prod(n1, n2):
    x = n1 * n2
    return x

def div(n1, n2):
    if n1 >= n2:
        x = n1 / n2
    else:
        x = n2 / n1
    return x

n = int(input())
n1 = int(input())
n2 = int(input())
if n == 1:
    ans = add(n1, n2)
    print(ans)
elif n == 2:
    ans = subtr(n1, n2)
    print(ans)
elif n == 3:
    ans = prod(n1, n2)
    print(ans)
elif n == 4:
    ans = div(n1, n2)
    print(ans)
else:
    print("Invalid option")





    
