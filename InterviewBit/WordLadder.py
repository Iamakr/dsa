# https://www.interviewbit.com/problems/word-ladder-i/


# Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

# You must change exactly one character in every transformation.
# Each intermediate word must exist in the dictionary.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.


# Input Format:

# The first argument of input contains a string, A.
# The second argument of input contains a string, B.
# The third argument of input contains an array of strings, C.
# Output Format:

# Return an integer representing the minimum number of steps required to change string A to string B.
# Constraints:

# 1 <= length(A), length(B), length(C[i]) <= 25
# 1 <= length(C) <= 5e3
# Example :

# Input 1:
#     A = "hit"
#     B = "cog"
#     C = ["hot", "dot", "dog", "lot", "log"]

# Output 1:
#     5

# Explanation 1:
#     "hit" -> "hot" -> "dot" -> "dog" -> "cog"




from collections import defaultdict
from collections import deque
class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        beginWord, endWord, wordList = A, B, C
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word) 
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0