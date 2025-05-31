# https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1649573114/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def gcdOfStrings(self, str1, str2):
      # check compatible
      if str1 + str2 != str2 + str1:
         return ""
      
      # check possible prefix
      min_len = min(len(str1), len(str2))
      for i in range(min_len, 0, -1):
        result = str1[:i]
        if str1 == result * (len(str1) // len(result)) and \
               str2 == result * (len(str2) // len(result)):
                return result
        return ""