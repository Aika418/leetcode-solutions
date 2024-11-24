class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""
        
        
        min_length = min(len(s) for s in strs)
        
       
        prefix = []
        
        
        for i in range(min_length):
            
            char_set = {s[i] for s in strs}
            if len(char_set) == 1:
                prefix.append(strs[0][i]) 
            else:
                break  
        
        return "".join(prefix)