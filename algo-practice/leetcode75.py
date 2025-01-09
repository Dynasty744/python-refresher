word1 = "ab"
word2 = "pqrs"

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      # O(n)
      # setup 2 variables to hold the length of the 2 strings
      # setup 2 pointers to use as indexes for the 2 strings
      # while the index of either string is smaller than length of either string
      # if index of first string is < than length of first string
      # then add the indexed char to res
      # then increment the index
      # perform same steps for the second string
      # return result
      l1 = len(word1)
      l2 = len(word2)
      p1 = 0
      p2 = 0
      res = []

      while p1 < l1 or p2 < l2:
        if p1 < l1:
          res += word1[p1]
          p1 += 1
        if p2 < l2:
          res += word2[p2]
          p2 += 1
          
      return ''.join(res)    

solution = Solution()
result = solution.mergeAlternately(word1, word2)
print(result)