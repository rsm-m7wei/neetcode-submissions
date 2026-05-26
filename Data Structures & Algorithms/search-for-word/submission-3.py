class Solution:
    def dfs(self, board, word, i, j, curr): #3对于dfs函数，我们首先需要想他的功能是什么！
    # 这里的功能室往上下左右扩展，看他是否和下一个字母相等，所以我们需要传入： board，word， ij（是在board里面的第几个）， curr（现在是在在word的第几个）
        if curr ==len(word):
            return True # 接着考虑结束条件： 如果所有word都找到了，也就是curr== len 就返回true
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[curr]: #注意这里一定是>= 
            return False # 4如果超出边界就返回false，并且在边界之内但是不相等也返回false
        letter = board[i][j]  #5因为我们不能让他重复出现，所以这里对我们现在的点要存在letter里面，并且去掉，最后回溯的时候再放回来
        board[i][j] = ''
        found = self.dfs(board, word, i+1, j, curr+1) or  self.dfs( board, word, i-1, j, curr+1) or  self.dfs( board, word, i, j+1, curr+1) or self.dfs( board, word, i, j-1, curr+1)
       
        board[i][j] = letter # 这里是我们还是对内部的四个方位再调用同样的函数
        return found# 之后放回letter来回溯，并且返回结果，来判断这个是不是能接得上
    def exist(self, board: List[List[str]], word: str) -> bool:
        # rows =len(board) #1我们要遍历这里面的每一个元素，并且找到起点，所以我们需要两个for循环
        # cols = len(board[0]) 
        # for i in range(rows):
        #     for j in range(cols):
        #         if board[i][j] == word[0] and self.dfs(board, word, i, j, 0): # 2对于里面满足要求的点，我们作为起点，并且放到dfs函数里查找是不是能找到
        #             return True # 能找到就返回true
        # return False #遍历完之后都找不到就返回false
        


        #define the bound ot our board,and use dfs function for qualified cell
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                #if this cell is qualified we can apply our dfs rules to find the word,
                #if we can not find it, we can just return false
                #we need board, word, i, j and 0to find !!location of word and boardand start our dfs
                if board[i][j] ==word[0] and self.dfs(board,word,i,j,0):
                    return True
        return False
        