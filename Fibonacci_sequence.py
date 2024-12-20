n_terms=int(input("enter the no of n terms"))
n1,n2=0,1
count=0
if n_terms<=0:
    print("enter the positive integer")
elif n_terms==1:
    print("Fibonacci sequence upto:",n_terms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<n_terms: #0<4 1<4  2<4  3<4   4<4 x
        print(n1) #0  1  1  2
        nth=n1+n2 #0+1=1  1+1=2 1+2=3  2+3=5
        n1=n2  #1      1         2     3
        n2=nth #1      2         3     5
        count+=1 #0+1=1 1+1=2    2+1=3 3+1=4
