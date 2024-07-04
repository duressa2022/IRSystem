"""
  This is python class that generates tokens from the documents, This class implements two
  important methods which are reader and writer method to read and write datas.
  Token Generator class implemented simply without considering advanced ruled for tokenization
"""
class TokenGenerator:
    def __init__(self,loc1,loc2):
        """
        consturctor for token generator class
        """
        self.loc1=loc1
        self.loc2=loc2
        self.tokens=[]

    def reader(self):
        """
        A method takes curated  paths as input and reads data from that file.
        :param paths:
        :return: True if correctly reads data else False
        """
        paths=self.pathReader(self.loc1)
        self.tokens=[]
        for path in paths:
            docs=[]
            try:
                with open(path,"r") as current:
                    lines=current.readlines()
                    for line in lines:
                        docs.extend(line.split())
            except FileNotFoundError:
                return False
            self.tokens.append(docs)
        return True

    def writer(self):
        """
        A method takes curated  paths as input and write tokens into the file.
        :param paths:
        :return: True if correctly reads data else False
        """
        paths=self.pathReader(self.loc2)
        for path,doc in zip(paths,self.tokens):
            try:
                with open(path,"w") as current:
                    for token in doc:
                        current.write(self.curateWord(token.lower())+"\n")
            except FileNotFoundError:
                return False
        return True
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
                    paths.append(line[:-1])

        except FileNotFoundError:
            return None
        return paths
    def curateWord(self,word):
        """
        curate every word
        :param word:
        :return:
        """
        if len(word)>0 and not word[-1].isalpha():
            return self.curateWord(word[:-1])
        if len(word)>0 and not word[0].isalpha():
            return self.curateWord(word[1:])
        return word

    def ____Excute____(self):
        self.reader()
        self.writer()
class QueryTokenizer:
    def __init__(self,loc):
        self.loc=loc
    def ____EXCUTE____(self):
        tokens=TokenGenerator(self.loc,self.loc)
        tokens.____Excute____()
apps=TokenGenerator("C:\\Users\\HP\\Desktop\\IRSystem\\PathLocation\\locations1.txt",
                    "C:\\Users\\HP\\Desktop\\IRSystem\\PathLocation\\locations2.txt")
apps.____Excute____()




