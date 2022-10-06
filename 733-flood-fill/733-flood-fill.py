class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source = image[sr][sc]
        if color == source:
            return image
        height = len(image)
        width = len(image[0])
        self.dfs(image, sr, sc, color, height, width, source)
        return image

    def dfs(self, image, sr, sc, newColor, height, width, source):
        if sr < 0 or sr >= height or sc < 0 or sc >= width:
            return
        elif image[sr][sc] != source:
            return
        image[sr][sc] = newColor
        self.dfs(image, sr-1, sc, newColor, height, width, source)
        self.dfs(image, sr+1, sc, newColor, height, width, source)
        self.dfs(image, sr, sc-1, newColor, height, width, source)
        self.dfs(image, sr, sc+1, newColor, height, width, source)