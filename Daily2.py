class Solution(object):
    def isPalindrome(self, num):
    #check if a number is palindrome     
     
     if(num<0):
        return False

     else:
        reverse = 0
        temp = num

        while temp>0:
            digit=temp%10
            reverse = reverse*10+digit
            temp/=10

        return reverse == num