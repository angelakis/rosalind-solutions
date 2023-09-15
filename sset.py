if __name__ == "__main__":
    with open("rosalind_sset.txt") as f:
        n = int(f.readline().strip())
    print(2**n % 1000000)
