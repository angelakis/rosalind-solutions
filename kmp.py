def make_failure_array_slow(dna):
    failureArray = [0] * len(dna)
    for i in range(1, len(dna)):
        for j in range(i, 0, -1):
            if dna[:i-j+1] == dna[j:i+1]:
                failureArray[i] = i-j+1
    return(failureArray)



def make_failure_array(dna):
    failureArray = [0] * len(dna)
    for i in range(1, len(dna)):
        if not failureArray[i-1] and dna[i] != dna[0]:
            continue
        if not failureArray[i-1]:
            failureArray[i] = 1
            startingPoints = []
            continue
        if dna[i] == dna[failureArray[i-1]]:
            if dna[failureArray[i-1]] == dna[0]:
                startingPoints.append(i)
            failureArray[i] = failureArray[i-1] + 1
        else:
            for j in startingPoints:
                if dna[j:i+1] == dna[:i-j+1]:
                    failureArray[i] = i - j + 1
                    if dna[i] == dna[0]:
                        startingPoints.append(i)
                    break
            if not failureArray[i] and dna[i] == dna[0]:
                failureArray[i] = 1
                startingPoints = []
    return(failureArray)


if __name__ == "__main__":
    dnaString = ""
    with open("inputfiles/rosalind_kmp.txt") as f:
        for line in f.readlines():
            if line[0] != ">":
                dnaString += line.strip()
    failureArray = make_failure_array(dnaString)
    print(" ".join(map(str, failureArray)))
