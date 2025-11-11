class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end = False
    
    def contains_key(self, ch:str) -> bool:
        return self.links[ord(ch) -ord('a')] is not None
    
    def get(self, ch: str) -> 'TrieNode':
        return self.links[ord(ch) - ord('a')]
    
    def put(self, ch:str, node: 'TrieNode') -> None:
        self.links[ord(ch) - ord('a')] = node
    
    def set_end(self) -> None:
        self.end = True
    
    def is_end(self) -> bool:
        return self.end
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def search_prefix(self, word:str) -> 'TrieNode':
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)