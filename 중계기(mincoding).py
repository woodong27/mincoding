import math

'''
중계기의 위치와 마을에 위치한 집들의 위치를 찾아서
각 집에서 중계기까지의 거리를 계산한다.
가장 먼 거리의 제곱이 중계기의 반지름의 제곱보다 작거나 같을 때
통신 범위에 포함되기 때문에
중계기에서 가장 먼 거리의 제곱근을 구해서 올림을 해주었다.
'''

T=int(input())

for tc in range(T):
    N=int(input())
    N+=1

    village=[list(map(int,input().split()))for _ in range(N)]

    houses=[]
    ri,rj=0,0
    for i in range(N):
        for j in range(N):
            if village[i][j]==2:
                ri,rj=i,j
            if village[i][j]==1:
                houses.append((i,j))

    d=0
    for house in houses:
        distance=(house[0]-ri)**2+(house[1]-rj)**2
        if distance>d:
            d=distance

    ans=math.ceil(d**(1/2))
    print(f'#{tc+1} {ans}')