n= int(input(" nhập số cần tính giai thừa : "))
def giaithua(n):
    if(n<0):
        int(input(" vui lòng nhập lại n là số nguyên dương"))
    if n==0:
        return 1
    return  n* giaithua(n-1)
print("Giai thừa của ", n , "là",giaithua(n))