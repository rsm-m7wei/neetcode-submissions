class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # #首先我们把它绕着左上到右下的轴交换位置
        # n =len(matrix)
        # for i in range(n):
        #     for j in range(1+i,n):
        #         # Python 交换必须用同时赋值，否则前一次赋值会覆盖原值，导致交换失败
        #         matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # for i in range(n):
        #     matrix[i].reverse()





        #接下来我们通过观察规律可以写出另一种方法
        # 01-12
        # 22-02
        # 20-00
        # 10-01
        #接下来我们通过观察规律可以写出另一种方法
        # 01-12
        # 22-02
        # 20-00
        # 10-01

        n =len(matrix)-1
        

        for row in range((n+1)//2):
            #range包含起点不包含终点
            for col in range(row,n-row):
                orig= matrix[row][col]
                matrix[row][col] = matrix[n-col][row]
                matrix[n-col][row] = matrix[n-row][n-col]
                matrix[n-row][n-col]=  matrix[col][n-row]
                #此时[row][col]的数值已经被修改过了，所以我们用orig来代替
                matrix[col][n-row] = orig
        
