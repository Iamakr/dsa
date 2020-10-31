# https://www.interviewbit.com/problems/word-ladder-ii/

# Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# If there are multiple such sequence of shortest length, return all of them. Refer to the example for more details.

# Note:

# All words have the same length.
# All words contain only lowercase alphabetic characters.
# Input Format

# The first argument is string start.
# The second argument is string end.
# The third argument is an array of strings dict
# Output Format

# Return all transformation sequences such that first word of each sequence is start and last word is end, all intermediate words belongs to dictionary(dict) and consecutive words had atmost 1 difference.  
# Example :

# :

# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return

#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
  


from collections import deque
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        dictV = set(dictV)
        dictV.add(end)
        queue = deque([(start, 1, [start])])
        visited = set()
        min_length = float('inf')
        ladders = []
        while queue:
            word, length, ladder = queue.popleft()
            visited.add(word)
            if word == end:
                if length == min_length:
                    ladders.append(ladder)
                elif length < min_length:
                    min_length = length
                    ladders = [ladder]
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in dictV and new_word not in visited:
                        queue.append((new_word, length+1, ladder+[new_word]))
        return ladders  # No sequence