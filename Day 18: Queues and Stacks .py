import sys

class Solution:

    def __init__(self):
        self.stack, self.queue = [], []
        
    def pushCharacter(self,a):
        self.stack.append(a)
        
    def popCharacter(self):
        return self.stack.pop()
        
    def enqueueCharacter(self,a):
        self.queue.append(a)
        
    def dequeueCharacter(self):
        return self.queue.pop(0)

s=input()

obj=Solution()   

l=len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 

for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
    
else:
    print("The word, "+s+", is not a palindrome.")    
