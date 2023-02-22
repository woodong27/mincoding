board=[list(map(int,input().split()))for _ in range(19)]
from pprint import pprint

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,-1,1]
pprint(board)

ans=0
winp=[]
for i in range(19):
    for j in range(19):
        if board[i][j]!=0:
            color=board[i][j]
            print(i,j)
            cnt=0
            for k in range(8):
                for m in range(1,7):
                    ni=i+di[k]*m
                    nj=j+dj[k]*m
                    if 0<=ni<19 and 0<=nj<19:
                        if board[ni][nj]==color:
                            cnt+=1
                        else:
                            break

            if cnt==5:
                ans+=1

                print(i,j)
                winp.append((i+1,j+1))

print(ans)
print(winp[0][0],winp[0][1])



