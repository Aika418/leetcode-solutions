class Solution(object):
    def isValid(self, s):
        kakko = {'(':')','{':'}','[':']'}
        stack = []
        lists=list(s)
        for i in range(len(lists)):
            if lists[i]=='(' or lists[i]=='{' or lists[i]=='[':
                stack.append(lists[i])
            else :
                if len(stack)==0:
                    return False
                else :
                    popkakko = stack.pop()
                    if not kakko[popkakko] == lists[i]:
                        return False
        if len(stack)==0:
            return True
        else :
            return False

        """
        :type s: str
        :rtype: bool
        """
        