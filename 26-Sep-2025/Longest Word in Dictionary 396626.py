# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self, val):
        self.children = {}
        self.value = val
        self.endOfWord = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode(0)
        maxLen = 0
        res = ""
        for word in sorted(words):
            cur = root
            count = 0
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode(count)
                cur = cur.children[letter]
                if cur.endOfWord: count += 1
            cur.endOfWord = True
            cur.value += 1
            if cur.value == len(word) and cur.value > maxLen:
                maxLen = cur.value
                res = word
        return res