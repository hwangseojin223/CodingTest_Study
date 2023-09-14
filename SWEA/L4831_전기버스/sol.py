
T  = int(input())
# N: 0~N 이동
# K: 최대 이동
# M: 충전기 설치 정류소 개수
for t in range(T):
    K, N, M = list(map(int, input().split()))

    load = [0] * N #크기가 N

    charge = list(map(int, input().split()))

    for i in range(M):
        load[charge[i]] += 1

    amount = K # 기름 수
    num = 0 # 충전 횟수
    loc = load.index()




    
    print(load)
    for i in range(1,N+1):
        print(i,"번멋")
        amount -= 1
        print(amount,"famount")
        if amount < N-i :
            next = load.index(1, i + 1)
            length = next - i
            print(next, length,"nl")
            if amount <= length and load[i] != 0:
                amount += K
                num += 1
                print(amount, num, "1p")
                if amount > N-i:

                    break
            elif amount < length and load[i] == 0:
                num = 0
                print(amount, num, "2p")
                break
    print(f'#{t+1} {num}')

'''못품'''
'''
import sys
sys.stdin = open

'''