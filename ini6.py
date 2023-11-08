if __name__ == "__main__":
    with open("inputfiles/rosalind_ini6.txt") as f:
        str = f.readline().split()
    words = {}
    for w in str:
        words[w] = words.get(w, 0) + 1
    for w, num in words.items():
        print(w, num)
