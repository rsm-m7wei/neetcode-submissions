class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        


        par =[ i  for i in range(n)]
        rank =[1]* n
        def find(n1):
            res = n1
            while res !=par[res]:
                par[res]= par[par[res]]
                res =par[res]
            return res
        def union(n1,n2):
            r1 =find(n1)
            r2 = find(n2)
            if r1 == r2:
                return 0
            if rank[r1]>rank[r2]:
                par[r2] = r1
                rank[r1] +=rank[r2]
            else:
                par[r1] =r2
                rank[r2] += rank[r1]
            return 1
        
        treenumber =n
        for n1,n2 in edges:
            treenumber -= union(n1,n2)
        return treenumber
            

        

            