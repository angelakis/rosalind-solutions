def calculate_inc_seq(numbers, increasing=True):
    seqEndingInNthLen = [(1, -1)] * len(numbers)
    totalMax = 0
    for i in range(len(numbers)-1, -1, -1):
        curMax = 0
        nextMax = -1
        for j in range(i+1, len(numbers)):
            if (
                (
                    (increasing and numbers[i] < numbers[j])
                    or ((not increasing) and numbers[i] > numbers[j])
                ) and seqEndingInNthLen[j][0] > curMax
            ):
                curMax = seqEndingInNthLen[j][0]
                nextMax = j
        seqEndingInNthLen[i] = (1 + curMax, nextMax)
        if 1 + curMax >= totalMax:
            totalMax = 1 + curMax
            nextInSeq = i
    longestIncSeq = [numbers[nextInSeq]]
    while nextInSeq != -1:
        nextInSeq = seqEndingInNthLen[nextInSeq][1]
        longestIncSeq.append(numbers[nextInSeq])
    return(longestIncSeq[:-1])

def calculate_dec_seq(numbers):
    return(calculate_inc_seq(numbers, increasing=False))

if __name__ == "__main__":
    with open("inputfiles/rosalind_lgis.txt") as f:
        f.readline()
        numbers = list(map(int, f.readline().split()))
    longestIncSeq = calculate_inc_seq(numbers)
    longestDecSeq = calculate_dec_seq(numbers)
    print(" ".join(map(str, longestIncSeq)))
    print(" ".join(map(str, longestDecSeq)))
