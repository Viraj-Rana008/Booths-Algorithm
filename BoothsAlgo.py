def main():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    ans = booth(a,b)
    print("\nAnswer : ",ans)


def booth(a,b):
    a1 = convert_To_binary(a)
    b1 = convert_To_binary(b)
    n = max(len(a1),len(b1))+1
    q = "0"
    A = "0"*n
    Q = balance(a, a1, n)
    i=n 
    if b>0:
        M2 = balance(b, convert_To_binary(b), n)
        M1 = balance(-b, convert_To_binary(b), n)
    else:
        M2 = balance(-b, convert_To_binary(b), n)
        M1 = balance(b, convert_To_binary(b), n)
    print()
    print(A, Q, q)
    while(i>0):
        if Q[-1]+q=="00" or Q[-1]+q=="11":
            A, Q, q = rightShift(A, Q, q)
            print(A, Q, q, "\tR Shift")

        elif Q[-1]+q =="10" :
            A = add(A, M1)               #M1 means -M
            print(A, Q, q, "\tA = A-M")

            A, Q, q = rightShift(A, Q, q)
            print(A, Q, q, "\tR Shift")

        elif Q[-1]+q == "01":
            A = add(A, M2)               #M2 means +M
            print(A, Q, q, "\tA = A+M")

            A, Q, q = rightShift(A, Q, q)
            print(A, Q, q, "\tR Shift")
        i-=1
    return a*b
    


def rightShift(A, Q, q):
    q = Q[-1]
    Q = A[-1]+Q[:-1]
    if A[0]=="0":
        A = "0"+A[:-1]
    else:
        A = "1"+A[:-1]

    return A, Q, q


def balance(a, a1, n):          #return string of binary representation of a upto n-bits (a1 = binary of |a| )
    d = {-1:"1", -2: "10", -3:"01", -4:"100", -5:"011", -6:"010", -7:"001"}
    if a in d:
        ans = "1"*(n-len(d[a]))+d[a]
    elif a<0 and len(a1)<n:
        a1 = balance(a, a1, len(a1))
        ans = "1"*(n-len(a1))+a1
    elif a<0 and len(a1)==n:
        a1 = convert_To_binary(twos_comp(abs(a), len(a1)))
        ans = "0"*(n-len(a1)) + a1
    elif a>0 and len(a1)<n:
        ans = "0"*(n-len(a1)) + a1
    elif a>0 and len(a1)==n:
        ans = a1
    elif a==0:
        ans = a1*n
    return ans


def add(A, M):          #adds two binary num; return result binary string;  A-> binary string of addend_1;  M-> binary string of addend_2
    A.split()
    M.split()
    added = []
    carry = 0
    for x in range(len(A)-1, -1, -1):
        if A[x]=="0" and M[x]=="0":
            if carry == 1:
                added.append("1")
                carry = 0
            else:
                added.append("0")
        elif (A[x]=="0" and M[x]=="1") or (A[x]=="1" and M[x]=="0"):
            if carry == 1:
                added.append("0")
            else:
                added.append("1")
        elif A[x]=="1" and M[x]=="1":
            if carry==1:
                added.append("1")
            else:
                added.append("0")
                carry = 1
    added.reverse()
    return "".join(added)


def convert_To_binary(x):           #returns  binary representation of |x|
    if x<0:
        return bin(x)[3:]
    else:
        return bin(x)[2:]

def twos_comp(val, bits):                   #
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: 
        val = val - (1 << bits)        
    return val        

''' def answer(s):              #returns int of binary string result computed in booth
    print(s)
    s = list(s)
    i=0
    while s[i]=="1":       
        i+=1
    s = s[i:]
    j = len(s)-1
    while s[j]!="1":
        j-=1
    for k in range(i,j):

        if s[k]=="0": s[k]= "1"
        else: s[k] = "0"
    s = "".join(s)
    print(int(s,2))
'''

if __name__=='__main__':
    main()
    
