a = [1,1,2,6,8,9,5,6,45,3,4,66,44,37,78]
b=[]
lenA= len(a)
for i in range( 0 , lenA-1):
    if(a[i]<30):
        b.append(a[i])
print(b)

print("\n")
B = [1,1,2,6,8,9,5,6,45,3,4,66,44,37,78]
C=[]
lenB=len(B)
n= int(input("nhập số bạn muốn tìm:"))
for x in range(0 , lenB-1):
    for y in range(x , lenB):
        if(B[x]>B[y]):
            temp=B[y]
            B[y]=B[x]
            B[x]=temp
for z in range (0 , lenB):
    if( B[z]> n):
        C.append(B[z])
print(C)