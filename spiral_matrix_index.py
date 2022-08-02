def spiralindex(xlen,ylen):
    def equal(xdiff,ydiff,xstart,ystart):
        x=xdiff#diff of x
        y=ydiff# diff of y
        l=[]
        x1=xstart#starting x
        y1=ystart#starting y
        s=set()
        for y2 in range(x):
            l.append((x1,y1))
            y1+=1
        y1-=1
        x1+=1
        for x2 in range(y-1):
            l.append((x1,y1))
            x1+=1
        y1-=1
        x1-=1
        for x2 in range(x-1):
            l.append((x1,y1))
            y1-=1
        y1+=1
        x1-=1
        for y2 in range(x-2):
            l.append((x1,y1))
            x1-=1
        return l
    #equal(4,4,2,2)
    def unequal(xdiff,ydiff,xstart,ystart):
        l=[]
        for x in range(ydiff):
            l.append((xstart,ystart+x))
        ypar=l[-1][1]
        for x in range(xdiff-1):
            l.append((xstart+1+x,ypar))
        if len(l)==xdiff*ydiff:
            return l
        xpar=l[-1][0]
        for x in range(ydiff-1):
            l.append((xpar,ystart+ydiff-2-x))
        for x in range(xdiff-2):
            l.append((xstart+xdiff-2-x,ystart))
        return l


    m,n=xlen,ylen
    xini,yini=0,0
    l=[]
    for x in range(max(m,n)):
        if (x,x) in l:
            break
        if m==n:
            l+=equal(m-2*x,n-2*x,xini,yini)
        else:
            l+=unequal(m-2*x,n-2*x,xini,yini)
        xini+=1
        yini+=1
    return l
