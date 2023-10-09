if __name__ == "__main__":
    with open("inputfiles/rosalind_inod.txt") as f:
        leaves = int(f.readline().strip())
    print(f"{leaves - 2}")
