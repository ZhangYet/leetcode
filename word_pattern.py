class Solution(object):

    def wordPattern(self, pattern, str):
        values = str.split(' ')
        if len(values) != len(pattern):
            return False

        pattern_dict = {}
        str_dict = {}
        for i in range(0, len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = values[i]
            else:
                if pattern_dict[pattern[i]] != values[i]:
                    return False

            if values[i] not in str_dict:
                str_dict[values[i]] = pattern[i]
            else:
                if str_dict[values[i]] != pattern[i]:
                    return False
        return True
                
                

pattern = "abba"            
str1 = "dog cat cat fish"
str2 = "dog dog dog dog"
str3 = "dog cat cat dog"
so = Solution()
print so.wordPattern(pattern, str1)
print so.wordPattern(pattern, str2)
print so.wordPattern(pattern, str3)

