##思路1.
##先将所有的点遍历一遍，把所有入度为0的点找出来。
##从某个入度为0的点A出发，找周边所有的点，如果周边的点入度为1的话，把这个点的入度减去1（即减去原先入度为0的那个点）。
##得到从A出发的点得到的点集S，再从S中选取一点，重新出发。
##直到所有入度为0的点都标记完了。
##典型的拓扑排序的思路。

##思路2
##深度优先遍历

class Solution(object):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def longestIncreasingPath(self, matrix):
        if len(matrix)==0 or len(matrix[0])==0:
            return 0

        res = 0
        col_len = len(matrix[0])
        row_len = len(matrix)
        dis = [[0 for x in xrange(0, col_len)] for x in xrange(0, row_len)]
        
        for i in xrange(0, row_len):
            for j in xrange(0, col_len):
                res = max(res, self.dfs(dis, row_len, col_len, i, j, matrix))
                
        return res
        
    def dfs(self, dis, row_len, col_len, x, y, matrix):
        if dis[x][y] != 0:
            return dis[x][y]
            
        for i in xrange(0, 4):
            newX = x + Solution.dx[i]
            newY = y + Solution.dy[i]

            if newX>=0 and newY>=0 and newX<row_len and newY<col_len and matrix[x][y]<matrix[newX][newY]:
                dis[x][y] = max(dis[x][y], self.dfs(dis, row_len, col_len, newX, newY, matrix))
                
        dis[x][y] += 1
        return dis[x][y]
            