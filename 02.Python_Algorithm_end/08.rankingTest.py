def ranking(scoreData):
    rank = []
    for i in range(len(scoreData)):
        rank.append(1)
    for i in range(len(scoreData) - 1):
        for j in range(i + 1, len(scoreData)):
            if scoreData[i] > scoreData[j]:
                rank[j] += 1
            elif scoreData[i] < scoreData[j]:
                rank[i] += 1
    for i in range(len(scoreData)):
        print("{0:3d}점은 {1}등 입니다.".format(scoreData[i], rank[i]))

if __name__ == "__main__":
    scoreData = [70, 100, 90, 80, 100]
    ranking(scoreData)

