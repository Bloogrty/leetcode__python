# link: https://leetcode.com/problems/merge-strings-alternately/submissions/1649562739/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)


        #merge
        while i < len1 and j < len2:
            result.append(word1[i])
            result.append(word2[j ])
            i += 1
            j += 1

        #remaining char
        if i < len1:
            result.append(word1[i:])
        if j < len2:
            result.append(word2[j:])

        return ''.join(result)