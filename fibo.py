def calculate_fib(n):
    fibo = [1, 1]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])
    return(fibo[n-1])

if __name__ == "__main__":
    with open("inputfiles/rosalind_fibo.txt") as f:
        n = int(f.readline().strip())
    print(calculate_fib(n))
