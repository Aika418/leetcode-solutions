
class Solution(object):
    def romanToInt(self, s):
        lists = list(s)
        sum = 0
        for i in range(len(lists)): 
            if i>0 and lists[i-1]=='I' and (lists[i] == 'V' or lists[i] == 'X'):
                sum -= 2
            elif i>0 and lists[i-1]=='X'and (lists[i] == 'L' or lists[i] == 'C'):
                sum -= 20
            elif i>0 and lists[i-1]=='C'and (lists[i] == 'D' or lists[i] == 'M'):
                sum -= 200
            if lists[i] == 'I':
                sum += 1
            elif lists[i] == 'V':
                sum += 5
            elif lists[i] == 'X':
                sum += 10
            elif lists[i] == 'L':
                sum += 50
            elif lists[i] == 'C':
                sum += 100
            elif lists[i] == 'D':
                sum += 500
            elif lists[i] == 'M':
                sum += 1000
        return sum

        """
        :type s: str
        :rtype: int
        """
        