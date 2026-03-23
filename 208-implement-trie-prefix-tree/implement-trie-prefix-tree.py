class Node:
    def __init__(self):
        self.links = [None]*26 
        self.flag = False 
    def containsKey(self,ch):
        if(self.links[ord(ch)-ord('a')]!=None):
            return True 
        return False 
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')] = node
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        node = self.root 
        for ch in word:
            if(node.containsKey(ch)==False):
                node.put(ch,Node())
            node = node.get(ch)
        node.flag = True 
    def search(self, word: str) -> bool:
        node = self.root 
        for ch in word:
            if(node.containsKey(ch) == False):
                return False 
            node = node.get(ch) 
        if(node.flag == True):
            return True 
        return False 
    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for ch in prefix:
            if(node.containsKey(ch) == False):
                return False 
            node = node.get(ch)
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)