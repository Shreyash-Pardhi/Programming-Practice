'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''


def isPalindrome(x):
        if(x<0):
            return False
        temp=x
        rem=0
        while(temp!=0):
            digit = temp % 10
            rem = rem*10+digit       
            temp//=10
        return rem==x