class PrefixTree:
    def __init__(self): # 这里是默认的函数，如果后续调用的时候不写.只有（）那默认的就是调用他
        self.children ={} # 作为默认函数的名字一定要是__init__,并且（）里面必须是self
        self.word = False #每一层都需要有一个{},和word，应为这是Trie的默认结构（相当于有很多分叉的树）

    def insert(self, word: str) -> None:
        root =self #初始化指针到root，初始节点，（self就是）
        for i in word: # 遍历这面的所有字母
            if i not in root.children: #对于第一个，如果他不在children的字典里面，就加入进去（并且由于最开始的根只有一个，所以不需要【】来指定）
                root.children[i] =PrefixTree() # 这里就是会自动创建一个，并给他PrefixTree 定一个类似树的结构
            root = root.children[i] #把指针移动到这个正在处理的节点（下一层）
        root.word =True #遍历完所有字母以后再返回这个最后node的word是不是true。


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



# (root)
#  ├── a
#  │    └── p
#  │         ├── p (word=True)              ← “app”
#  │         │     └── l
#  │         │          └── e (word=True)   ← “apple”
#  │         └── e (word=True)              ← “ape”
#  │
#  └── b
#       └── a
#            ├── t (word=True)              ← “bat”
#            └── d (word=True)              ← “bad”
        
        