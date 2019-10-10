class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        size = len(words)
        i, j = size, size
        ans = size
        for n in range(size):
            if words[n] == word1:
                i = n
                ans = min(ans, abs(i - j))
            elif words[n] == word2:
                j = n
                ans = min(ans, abs(i - j))
        return ans


if __name__ == "__main__":
    words = ["this","is","a","long","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday","this","sentence","run","running","rainy"]
    word1 = "sentence"
    word2 = "a"
    print(Solution().shortestDistance(words, word1, word2))