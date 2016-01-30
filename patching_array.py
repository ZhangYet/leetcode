class Solution(object):
    
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        self.init_len = len(nums)
        self.nums = nums
        init_sum = sum(nums)
        res = []
        temp = n - init_sum

        while temp > 0:
            res.append(temp)
            temp -= init_sum
        self.refresh(init_sum)

        return len(res) + len(self.nums) - self.init_len
            
    def refresh(self, n):
        table = [0 for x in xrange(0, n)]
        for x in self.nums:
            for i in xrange(0, n):
                if table[i]>0 and table[i]+x-1<n:
                    table[table[i]+x-1] = table[i] + x
                    
        for i in range(0, n):
            if i not in table:
                self.nums.append(i)
                for j in range(0, n):
                    if table[j]>0 and table[j]+i-1<n:
                        table[table[j]+i-1] = table[j] + i
                table[i-1] = i
        
def test():
    nums = [1, 5, 10]
    n = 20
    t = Solution()
    print t.minPatches(nums, n)
    
test()