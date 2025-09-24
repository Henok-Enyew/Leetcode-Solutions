# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = [] 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def searchPrefix(self, prefix: str):
        node = self.root
        result = []
        for ch in prefix:
            if ch not in node.children:
                return [] 
            node = node.children[ch]
        return node.suggestions
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  
        trie = Trie()
        for product in products:
            trie.insert(product)

        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            res.append(trie.searchPrefix(prefix))
        return res