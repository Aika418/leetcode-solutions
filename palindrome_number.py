class Solution(object):
    def isPalindrome(self, x):
        list_x = list(str(x));
        list_x_circle = []
        i = len(list_x)-1
        for j in range(len(list_x)):
            list_x_circle.append(list_x[i])
            i = i-1
        if list_x == list_x_circle :
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """
        