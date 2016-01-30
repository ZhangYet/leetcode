class Solution(object):
    def __init__(self):
        self.table = None
        self.init_len = 0
    
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        self.init_len = len(nums)
        self.table = [0 for x in xrange(0, n)]
        self.nums = nums
        
        for x in self.nums:
            for i in xrange(0, n):
                if self.table[i] > 0 and self.table[i]+x-1<n:
                    self.table[self.table[i]+x-1] = self.table[i] + x
            self.table[x-1] = x

        for i in xrange(1, n+1):
            if i not in self.table:
                self.refresh(i, n)
        return len(self.nums) - self.init_len
            
    def refresh(self, i, n):
        self.nums.append(i)

        for j in xrange(0, n):
            if self.table[j] > 0 and self.table[j]+i-1<n:
                self.table[self.table[j]+i-1] = self.table[j] + i
        self.table[i-1] = i
        
        
def test():
    nums = [1, 5, 10]
    n = 20
    t = Solution()
    print t.minPatches(nums, n)
    
test()