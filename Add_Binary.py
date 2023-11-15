'''
Given two binary strings a and b, return their sum as a binary string.
'''

def addBinary(self, a: str, b: str) -> str:
        maxl = max(len(a), len(b))
        a=a.zfill(maxl)
        b=b.zfill(maxl)
        result=''
        c=0

        for i in range(maxl-1,-1,-1):
            r=c
            r+=1 if a[i]=='1' else 0
            r+=1 if b[i]=='1' else 0
            result = ('1' if r%2==1 else '0') + result
            c = 0 if r<2 else 1
        if c!=0:
            result = '1'+result
        
        return result