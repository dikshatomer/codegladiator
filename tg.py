def main():
    T = int(input())
    for n in range(T):
        N = int(input())
        tg = list(map(int,input().split()))
        op = list(map(int,input().split()))
        tg.sort(reverse=True)
        op.sort(reverse=True)
        i=0
        j=0
        cnt=0
        win=0
        for i in range(N):
            for j in range(cnt,N):
                if tg[i]>op[j]:
                    cnt=j+1
                    win+=1
                    break
        print(win)
           
main()
