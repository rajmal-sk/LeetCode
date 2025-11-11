class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end = False

    def contains_key(self, ch : str) -> bool:
        return self.links[ord(ch) - ord('a')] is not None
    
    def get(self, ch : str) -> 'TrieNode':
        return self.links[ord(ch) - ord('a')]
    
    def put(self, ch: str, node : 'TrieNode') -> None:
        self.links[ord(ch) - ord('a')] = node
    
    def is_end(self):
        return self.end

    def set_end(self):
        self.end = True

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def helper(self, word: str, node: 'TrieNode', idx: int) -> bool:
        if idx == len(word):
            return node.is_end()

        ch = word[idx]

        if ch == '.':
            for ref in node.links:
                if ref is not None and self.helper(word, ref, idx + 1):
                    return True
            return False
        else:
            ref = node.get(ch)
            if ref is None:
                return False
            return self.helper(word, ref, idx + 1)
        

    def search(self, word: str) -> bool:
        node = self.root
        return self.helper(word, node, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)