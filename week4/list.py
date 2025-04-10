def creat_list(l,n):
    for i in range(n):
        temp=int(input())
        l.append(temp)
    return l
def even_sum(l):
    evensum=0
    for i in range(len(l)):
        if i%2==0:
            evensum+=l[i]

    return evensum
def odd_sum(l):
    oddsum=0
    for i in range(len(l)):
        if i%2==0:
            return oddsum
            
 
            
l1=[]
l2=[]
l3=[]
n1=int(input("enter lea "))
n1=creat_list(l1,n1)
k=even_sum(n1)
print(k)
