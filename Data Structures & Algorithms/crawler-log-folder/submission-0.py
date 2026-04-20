class Solution:
    def minOperations(self, logs: List[str]) -> int:
        total = 0
        n = len(logs)

        for i in range(n):
            if logs[i] == "../":
                if total > 0:
                    total -= 1
            elif logs[i] == "./":
                continue
            else:
                total += 1
        return total