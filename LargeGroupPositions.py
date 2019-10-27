class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(S)-1:
            count = 1
            j = i + 1
            while j < len(S):
                if S[i] == S[j]:
                    count += 1
                    j += 1
                else:
                    break
            if count >= 3:
                ans.append([i,j-1])
            i = j
        return ans


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(S)-1:
            # count = 1
            j = i + 1
            while j < len(S) and S[i] == S[j]:
                # count += 1
                j += 1
            if j-i >= 3:
                ans.append([i,j-1])
            i = j
        return ans
                