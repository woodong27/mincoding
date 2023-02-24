'''
판에 입력받은 좌표와 색깔을 칠해주고
차례대로 순회하여 색칠되어있는 칸을 만나면
모양이 정사각형일때까지 대각선으로 탐색하고
찾은 모양 중 가장 큰 정사각형의 크기를 출력하였다.
'''
N=int(input())

board=[[0 for _ in range(N)]for _ in range(N)]

Q=int(input())
for _ in range(Q):
    color,i1,j1,i2,j2=map(int,input().split())
    if i1>i2:
        i1,i2=i2,i1
    if j1>j2:
        j1,j2=j2,j1
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            if color>board[i][j]:
                board[i][j]=color

result=0
for i in range(N):
    for j in range(N):
        if board[i][j]!=0:
            k=1
            while i+k<N and j+k<N and board[i][j]==board[i+k][j+k]:
                k+=1

            if k>result:
                result=k

print(result**2)