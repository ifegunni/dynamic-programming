def fibonnaci(num):  #:: Top to Bottom
    lookUp = {}
    if num not in lookUp:
        if num <= 1:
            lookUp[num] = num
        else:
            lookUp[num] = fibonnaci(num-1) + fibonnaci(num-2)
    return lookUp[num]

def fib(n):   #::bottom to Top approach
    lookUp = [0]*(n+1)
    lookUp[0], lookUp[1] = 0, 1

    for i in range(2, n+1):
        lookUp[i] = lookUp[i-2] + lookUp[i-1]
    return lookUp[n]


x = fibonnaci(4)
y = fib(4)
print(x)
print(y)
