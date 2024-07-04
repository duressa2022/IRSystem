class StopWordRemover:
    def __init__(self,loc):
        """
        StopWordRemover class constructor when this method is class....
        set of words which contains the set of stop words and list of tokens will be..
        created..
        """
        self.loc=loc
        self.words=set()
        self.tokens=[]
        with open("C:\\Users\\HP\Desktop\\IRSystem\\StopWords\\stopWords.txt","r") as current:
            lines=current.readlines()
            for line in lines:
                self.words.add(line.strip("\n"))
    def wordReducer(self):
        """
        A main method of stop word remover class which will remove the most common words from the..
        the documents.
        :return:
        """
        self.tokenReader()
        reducedToken=[]
        for doc in self.tokens:
            new_token=[]
            for token in doc:
                if token not in self.words:
                    new_token.append(token)
            reducedToken.append(new_token)
        self.tokens=reducedToken
        self.tokenWriter()

    def tokenReader(self):
        """
        A method reads tokens from  the token file
        :param :
        :return:
        """
        paths = self.pathReader(self.loc)
        self.tokens = []
        for path in paths:
            docs = []
            with open(path, "r") as current:
                lines = current.readlines()
                for line in lines:
                    docs.extend(line.split())
            self.tokens.append(docs)
    def tokenWriter(self):
        """
         A writes the given tokens on the token file.
         :param :
         :return:
        """
        paths = self.pathReader(self.loc)
        for path,doc in zip(paths,self.tokens):
            with open(path,"w") as current:
                for token in doc:
                    current.write(token.lower() + "\n")
    def pathReader(self,location):
        """
        This method reads every paths from give location and return them
        that are understandable by python
        :param :
        :return:paths
        """
        paths=[]
        try:
            with open(location,"r") as current:
                lines=current.readlines()
                for line in lines:
                    if not line=="":
                        paths.append(line[:-1])
        except FileNotFoundError:
            print("File is not Found!")
        return paths
    def ____Excute___(self):
        self.tokenReader()
        self.wordReducer()
class QueryProcesser:
    def __init__(self,loc):
        self.loc=loc
    def ____EXCUTE____(self):
        tokens=StopWordRemover(self.loc)
        tokens.____Excute___()
apps=StopWordRemover("C:\\Users\\HP\\Desktop\\IRSystem\\PathLocation\\locations2.txt")
apps.____Excute___()








