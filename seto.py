if __name__ == "__main__":
    with open("inputfiles/rosalind_seto.txt") as f:
        n = int(f.readline().strip())
        setA  = eval(f.readline().strip())
        setB  = eval(f.readline().strip())
    fullSet = set(range(1, n+1))
    print(setA | setB)
    print(setA & setB)
    print(setA - setB)
    print(setB - setA)
    print(fullSet - setA)
    print(fullSet - setB)
