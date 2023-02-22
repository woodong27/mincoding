board=[list(map(int,input().split()))for _ in range(5)]

numbers=[]
for i in range(5):
    numbers.extend(list(map(int,input().split())))

cnt,now=0,0
while cnt<3 and numbers:
    now=numbers.pop(0)
    for i in range(5):
        for j in range(5):
            if board[i][j]==now:
                board[i][j]=0

    cnt=0
    board_t=list(map(list,zip(*board)))
    for i in range(5):
        if board[i].count(0)==5:
            cnt+=1
        if board_t[i].count(0)==5:
            cnt+=1

    cntd1,cntd2=0,0
    for i in range(5):
        if board[i][i]==0:
            cntd1+=1
        if board[4-i][i]==0:
            cntd2+=1

    if cntd1==5:
        cnt+=1
    if cntd2==5:
        cnt+=1

print(now)