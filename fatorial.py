def fatorial (n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fatorial(n-1)

fatorial(2)
fatorial(3)
fatorial(4)
fatorial(5)