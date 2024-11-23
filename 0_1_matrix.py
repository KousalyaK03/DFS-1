"""
        Approach: Use Breadth-First Search (BFS) starting from all 0 cells in the matrix.
        Update distances layer by layer to ensure each cell is processed only once.
        This guarantees the shortest distance to a 0 for each cell.
        
        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns. Each cell is visited once, and each neighbor is checked once.
        Space Complexity: O(m * n), where m * n accounts for the size of the queue and the storage for the result matrix.
        Did this code successfully run on Leetcode: Yes
        Any problem you faced while coding this: No
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # Dimensions of the matrix
        m, n = len(mat), len(mat[0])
        
        # Initialize result matrix with infinity for 1s
        result = [[float('inf')] * n for _ in range(m)]
        
        # Queue for BFS
        queue = deque()
        
        # Add all 0 cells to the queue and set their distance to 0 in result
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))  # Start BFS from all 0 cells
        
        # Direction vectors for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Perform BFS
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds and update if we find a shorter distance
                if 0 <= nx < m and 0 <= ny < n:
                    if result[nx][ny] > result[x][y] + 1:
                        result[nx][ny] = result[x][y] + 1
                        queue.append((nx, ny))
        
        return result
