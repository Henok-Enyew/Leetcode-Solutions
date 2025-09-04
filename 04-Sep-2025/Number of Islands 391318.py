# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis=[]
        for i in range(0,len(grid)):
            a=[]
            for j in range(0,len(grid[i])):
                a.append(-1)
            vis.append(a)
        def dfs(i,j):
            vis[i][j]=1
            dx=[-1,1,0,0]
            dy=[0,0,1,-1]
            for l in range(0,4):
                nx=i+dx[l]
                ny=j+dy[l]
                if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]):
                    pass
                elif grid[nx][ny]=="1" and vis[nx][ny]!=1:
                    dfs(nx,ny)
        count=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]=="1" and vis[i][j]==-1:
                    dfs(i,j)
                    count+=1
        return count
