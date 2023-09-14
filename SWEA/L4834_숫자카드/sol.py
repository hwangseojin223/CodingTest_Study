# a = '1234' => list(a) = ['1','2','3','4']

T = int(input())

for t in range(T):
    N = int(input())
    M = list(map(int, list(input())))

    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for num in M:
        count[num] += 1

    max_val = count[0]
    idx = 0
    for i in range(len(count)):
        if count[i] > max_val:
            max_val = count[i]
            idx = i
        elif count[i] == max_val:
                if i>idx:
                    max_val = count[i]
                    idx = i
    print(f'#{t+1} {idx} {max_val}')

'''
풀이
import sys
sys.stdin = open('input.txt')

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    counter = [0] * 10
    
    for card in cards:
        counter[card] += 1
    
    max_card = 0
    max_count = counter[max_card]
    
    for idx in range(10):
        if counter[idx] >= max_count:
            max_count = counter[idx]
            max_card = idx
print('#{tc} {max_card} {max_count}')
'''