import heapq
N=int(input())
l=list(map(int,input().rstrip().split()))
#2
# 6 5 1 10 9 2

l1=l[:N]
l2=l[N:]
l2=list(map(lambda x:-x,l2))
heapq.heapify(l1)
heapq.heapify(l2)

a=heapq.nlargest(N,l1)
b=heapq.nlargest(N,l2)
s=sum(a)+sum(b)
for x in range(N,2*N):

    heapq.heappush(l1,l[x])
    l2.remove(-l[x])
    heapq.heapify(l2)
    #print(l1,l2)
    s=max(s,sum(heapq.nlargest(2,l1))+sum(heapq.nlargest(2,l2)))  

print(s)


