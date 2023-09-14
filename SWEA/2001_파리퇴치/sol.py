#
def mtotal(matrix, N, M):
    max_val = 0
    total = 0
    for i in range(0,N-M+1):
        if i == 0:
            for j in range(0, M):
                print(i,j,"IJ")
                print(matrix[i][j], "1p")

            total += matrix[i][j]
            print(total)
        total = 0
    return total

T = int(input())

N, M = list(map(int, input().split())) # N:전체 M:파리채 크기

matrix = [list(map(int, input().split())) for _ in range(N)]
#print(matrix[0][0:M])
#print(sum(matrix[0][0:M]))
mtotal(matrix,N,M)