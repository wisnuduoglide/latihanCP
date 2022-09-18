x = range(1,100)
y= range(1,100)
x, y = map(int, input().split())


x = x*x
y = y*y

if (x+y+1)%4 ==0:
    print((x+y+1)//4)
else :
    print(-1)    