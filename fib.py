from math import comb

def modified_fib(n, k):
    fib_values = {
        1: 1,
        2: 1
    }
    for i in range(3, n+1):
        fib_values[i] = k * fib_values[i-2] + fib_values[i-1]
    return(fib_values[n])

if __name__ == "__main__":
    with open("rosalind_fib.txt") as f:
        n, k = [int(x) for x in f.readline().strip().split()]
    print(modified_fib(n, k))
