def find_longest_common_string(fasta_dna_strings):
    dnaStrings = list(fasta_dna_strings.values())
    substringDict = longest_common_substrings(dnaStrings[0], dnaStrings[1])
    longestSubstrings = sorted(substringDict.items(), reverse=True)
    for (substrLen, substringSet) in longestSubstrings:
        for substring in substringSet:
            existsInAll = True
            for dna in dnaStrings[2:]:
                if substring not in dna:
                    existsInAll = False
                    break
            if existsInAll:
                return(substring)


def longest_common_substrings(a, b):
    substrings = {}
    substringArray = [len(b) * [0] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != b[j]:
                continue
            if 0 in (i, j):
                substringArray[i][j] = 1
                substrings[1] = substrings.get(1, set()) | set([a[i]])
            else:
                newLen = substringArray[i-1][j-1] + 1
                substringArray[i][j] = newLen
                substrings[newLen] = substrings.get(newLen, set()) | set([a[i-newLen+1:i+1]])
    return(substrings)


if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_lcsm.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    print(find_longest_common_string(fasta_dna_strings))
