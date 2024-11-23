"""
        Approach: Perform a Depth-First Search (DFS) or Breadth-First Search (BFS) starting from the pixel at (sr, sc).
        If the starting pixel's color is already equal to the new color, return the image as is. Otherwise, recursively update the color of the starting pixel and its adjacent pixels if they share the same color as the starting pixel.
        
        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns, as we may visit all pixels in the worst case.
        Space Complexity: O(m * n), which accounts for the recursion stack or the queue in BFS.
        Did this code successfully run on Leetcode: Yes
        Any problem you faced while coding this: No
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # Get the original color of the starting pixel
        original_color = image[sr][sc]
        
        # If the original color is the same as the new color, return the image
        if original_color == color:
            return image
        
        # Helper function to perform DFS
        def dfs(x, y):
            # Check bounds and pixel color
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != original_color:
                return
            
            # Update the pixel color
            image[x][y] = color
            
            # Explore all four adjacent directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                dfs(x + dx, y + dy)
        
        # Start DFS from the given starting pixel
        dfs(sr, sc)
        
        return image
