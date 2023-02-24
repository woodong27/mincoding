board=[list(map(int,input().split()))for _ in range(19)]

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,-1,1]

wincolor=0
for i in range(19):
    for j in range(19):
        if board[i][j]!=0:
            for k in range(8):
                position = [(i, j)]
                m=1
                while 0<=i+di[k]*m<19 and 0<=j+dj[k]*m<19 and board[i][j]==board[i+di[k]*m][j+dj[k]*m]:
                    m+=1

                if m==5:

                    wincolor=board[i][j]
                    position.append((i+di[k]*m,j+dj[k]*m))
                    ansp=position

print(wincolor)
print(ansp)




