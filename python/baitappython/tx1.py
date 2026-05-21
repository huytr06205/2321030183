n=int(input ("n="))
for i in range (1,n):
    s= 0
    for j in range (1,i):
        if i%j ==0:
            s=s+j


    if s==i:
        print(s)
        1000        