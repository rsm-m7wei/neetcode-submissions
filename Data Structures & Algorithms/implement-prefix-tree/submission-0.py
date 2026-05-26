class PrefixTree:
    def __init__(self):
        self.children ={}
        self.word = False

    def insert(self, word: str) -> None:
        root =self
        for i in word:
            if i not in root.children:
                root.children[i] =PrefixTree()
            root = root.children[i]
        root.word =True


    def search(self, word: str) -> bool:
        root= self
        for i in word:
            if i not in root.children:
                return False
            root =root.children[i]
            
        return root.word


        

    def startsWith(self, prefix: str) -> bool:
        root =self
        for i in prefix:
            if i not in root.children:
                return False
            root = root.children[i]
        return True
        
        