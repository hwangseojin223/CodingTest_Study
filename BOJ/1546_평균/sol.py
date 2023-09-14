N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
total = 0

for i in range(len(scores)):
    scores[i] = scores[i]/M*100
    total += scores[i]
print(total/N)    