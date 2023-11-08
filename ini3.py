if __name__ == "__main__":
    with open("inputfiles/rosalind_ini3.txt") as f:
        str = f.readline().strip()
        a, b, c, d = [int(x) for x in f.readline().split()]
    print(f"{str[a:b+1]} {str[c:d+1]}")
