from math import comb

def modified_fib_deaths(n, m):
    fib_values = {
        0: 1,
        1: 1,
        2: 1
    }
    for i in range(3, n+1):
        fib_values[i] = fib_values[i-2] + fib_values[i-1] - fib_values.get(i-m-1, 0)
    return(fib_values[n])

if __name__ == "__main__":
    with open("inputfiles/rosalind_fibd.txt") as f:
        n, m = [int(x) for x in f.readline().strip().split()]
    print(modified_fib_deaths(n, m))
