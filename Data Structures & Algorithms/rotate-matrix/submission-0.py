class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #首先我们把它绕着左上到右下的轴交换位置
        n =len(matrix)
        for i in range(n):
            for j in range(1+i,n):
                # Python 交换必须用同时赋值，否则前一次赋值会覆盖原值，导致交换失败
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
