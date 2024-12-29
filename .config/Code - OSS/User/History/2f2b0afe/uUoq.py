class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        x=list(x)
        input=x
        new_list=[]
        for i in range(len(x)):
            new_list.append(x[-i-1])
            #    if a[i]==a[-i-1]:
            #     print('true')
            #    else:
                # print('false') 
        return input==new_list
a=Solution()
a.isPalindrome(121)