class Trie:

    class TrieNode:

        def __init__(self):
            self.children = {}
            self.endOfTheWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = self.TrieNode()
            cur = cur.children[c]
        cur.endOfTheWord = True


    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfTheWord

    def list_words(self,trie,str):
        my_list = []
        if trie.endOfTheWord:
            my_list.append(str)
            
        for i in trie.children:
            ls = self.list_words( trie.children[i] , str+i )
            if len(ls)!=0:
                my_list +=ls
        return my_list


    def get_all(self):
        return sorted(self.list_words(self.root,""))

    def list_pre(self,trie,pre,str,p):
        my_list = []
        if trie.endOfTheWord and p >= len(pre):
            my_list.append(str)
        
        for i in trie.children:
            if p >= len(pre) or i == pre[p]:
                ls = self.list_pre( trie.children[i] , pre , str+i , p+1 )
                if len(ls)!=0:
                    my_list +=ls
        return my_list

    def begins_with(self, prefix):
        return sorted(self.list_pre(self.root,prefix,"",0))



