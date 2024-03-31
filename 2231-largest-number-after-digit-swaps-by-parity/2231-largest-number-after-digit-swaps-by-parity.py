class Solution(object):
    def largestInteger(self, num):   
        odd_list = []
        even_list = []
        position_list = []
        final_num = 0

        for i in range(0, len(str(num))):
            temp = num % 10
            num = num//10
            if temp%2 == 0:
                even_list.append(temp)
                position_list.append(True)
            else:
                odd_list.append(temp)
                position_list.append(False)

        odd_list.sort()
        even_list.sort()
        for i in reversed(range(0,len(position_list))):
            isEven = position_list.pop()
            if isEven:
                final_num += even_list.pop()*(10**i)
            else:
                final_num += odd_list.pop()*(10**i)
        
        return final_num