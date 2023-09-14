T = int(input())

for t in range(T):
    N = int(input())
    area = []
    red = []
    blue = []
    for i in range(N):
        area = list(list(map(int, input().split())))
        if area[4] == 1:
            for r in range(area[0],area[2]+1):
                for c in range(area[1], area[3]+1):
                    red.append([r,c])
        elif area[4] == 2:
            for r in range(area[0],area[2]+1):
                for c in range(area[1], area[3]+1):
                    blue.append([r,c])
    purple = []
    if len(red) > len(blue):
        for i in red:
            if i in blue:
                purple.append(i)
    else:
        for i in blue:
            if i in red:
                purple.append(i)
    print(f'#{t+1} {len(purple)}')