from collections import Counter
class Sol:
    def longest_palindrome(self,s):
        arr=list(Counter(s).values())
        result=0
        r1=0
        for n in arr:
            if n%2!=0:
                result+=n-1
                r1+=1
            else:
                result+=n
        if r1==0:
            return result
        else:
            return result+1

if __name__ == '__main__':
    p1=Sol()
    print(p1.longest_palindrome('abccccdd'))
