
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_val = min_val = sum(numbers[0:M])

    for first in range(0, N-M+1):
        total = sum(numbers[first:first+M])
        if total > max_val:
            max_val = total
        elif total < min_val:
            min_val = total
    sub = max_val - min_val
    print(f'#{i+1} {sub}')
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    max_sum = min_sum = sum(numbers[:M])
    
    for start in range(N-M+1):
        end = start + M
        total = sum(numbers[start:end])
        
        if total > max_sum:
            max_sum = total
        
        if total < min_sum:
            mim_sum = total
    ans = max_sum - min_sum
    print(f'#{tc} {ans}')
'''