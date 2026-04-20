class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        totSum = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                res.append(res[-1] + res[-2])
            
            elif operations[i] == "C":
                res.pop()

            elif operations[i] == "D":
                res.append(res[-1] * 2)
            
            else:
                res.append(int(operations[i]))

        for j in res:
            totSum += j 
        return totSum
