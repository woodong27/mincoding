N,M=map(int,input().split()) #N:세로, M:가로
K=int(input())
area=[list(input())for _ in range(N)]

di=[-1,1,0,0]
dj=[0,0,-1,1]

'''
폭탄이 위치한 시작점을 찾아서
각 시작점에서 방향배열을 사용한 탐색을 해주었다.
선택한 방향으로 뻗어나가다가 벽을 만나면 break를 통해 멈추고
다른방향으로 뻗어나가며 폭탄이 터진다.
@:폭탄, #:벽, _:빈칸, %:폭탄이 터진 자리
'''

spoint=[]
for i in range(N):
    for j in range(M):
        if area[i][j]=='@':
            spoint.append((i,j))

while spoint:
    ci,cj=spoint.pop()
    area[ci][cj]='%'
    for k in range(4):
        for i in range(1,K+1):
            ni,nj=ci+di[k]*i,cj+dj[k]*i
            if 0<=ni<N and 0<=nj<M:
                if area[ni][nj]=='#':
                    break
                else:
                    area[ni][nj]='%'

for i in range(N):
    print(*area[i],sep='')