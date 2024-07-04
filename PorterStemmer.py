class PorterStemmer:
    def __init__(self,loc):
        self.loc=loc
        self.vowels = "aeiou"
        self.double_consonants = ["bb", "dd", "ff", "gg", "mm", "nn", "pp", "rr", "tt"]
        self.li_ending = ["c", "d", "e", "g", "h", "k", "m", "n", "r", "t"]
    def isConsonants(self,word,index):
        """
        This method or function will check wether the current index or char is cons or not.
        :param word:
        :param index:
        :return: True if cons.. else False
        """
        if word[index] in self.vowels:
            return False
        if word[index]=="y":
            return index==0 or not self.isConsonants(word,index-1)
        return True
    def measure(self,word):
        """
        This method or function will calculate the number of group of consecutive cons..
        :param word:
        :return: number of group of consecutive cons...
        """
        length=len(word)
        index=counter=0
        while index<length:
            while index<length and not self.isConsonants(word,index):
                index=index+1
            if index<length:
                index=index+1
                counter=counter+1
            while index<length and self.isConsonants(word,index):
                index=index+1
        return counter
    def containsVowels(self,word):
        """
        This method or function checks wether the given word contains at least one vowel or not
        :param word:
        :return: True if it contains otherwise false
        """
        length=len(word)
        for index in range(length):
            if word[index] in self.vowels:
                return True
        return False
    def endWithDoubleConsonants(self,word):
        """
        This method or function checks wether th given word will end with double consonants or not.
        :param word:
        :return:True if it ends otherwise False
        """
        length=len(word)
        if length>2 and word[-1]==word[-2]:
            return self.isConsonants(word,length-1)
        return False
    def endsWithCVC(self,word):
        """
        This method function checks wether the given word will ends with cvc pattern
        :param word:
        :return:True if it end other wise False
        """
        length=len(word)
        if length<3:
            return False
        if not self.isConsonants(word,-1) or self.isConsonants(word,-2) or not self.isConsonants(word,-3):
            return False
        if word[-1] in "xyz":
            return False
        return True
    def firstStep(self,word):
        """
        This method or function perform the first step in porter stemmer method that is removed
         number and tense indicator suffixs.
        :param word:
        :return:word
        """
        #removal of number indicator suffices
        if word.endswith("esses"):
            word=word[:-2]
        elif word.endswith("ies"):
            word=word[:-2]
        elif word.endswith("ss"):
            pass
        elif word.endswith("s"):
            word=word[:-1]
        #removal of tense indicator suffices
        if word.endswith("eed"):
            if self.measure(word[:-3])>0:
                word=word[:-1]
        elif (word.endswith("ed") and self.containsVowels(word[:-2]) or word.endswith("ing") and self.containsVowels(word[:-3])):
            word=word[:-2] if word.endswith("ed") else word[:-3]
            if word.endswith("at") or word.endswith("bl") or word.endswith("iz"):
                word=word+"e"
            elif self.endWithDoubleConsonants(word) and word[-1] in "lsz":
                word=word[:-1]
            elif self.measure(word)==1 and self.endsWithCVC(word):
                word=word+"e"
        return word
    def secondStep(self,word):
        """
        This method or function implements the second step that is replecement of y by using i.
        :param word:
        :return:word
        """
        if word.endswith("y") and self.containsVowels(word[:-1]):
            word=word[:-1]+"i"
        return word
    def thirdStep(self,word):
        """
        This method or function implements the second steps in portet stemmer method which involves..
        removal of suffices or replacement of suffices.
        :param word:
        :return:word
        """
        suffixes = {
            "ational": "ate",
            "tional": "tion",
            "enci": "ence",
            "anci": "ance",
            "izer": "ize",
            "abli": "able",
            "alli": "al",
            "entli": "ent",
            "eli": "e",
            "ousli": "ous",
            "ization": "ize",
            "ation": "ate",
            "ator": "ate",
            "alism": "al",
            "iveness": "ive",
            "fulness": "ful",
            "ousness": "ous",
            "aliti": "al",
            "iviti": "ive",
            "biliti": "ble"
        }
        for suff,replace in suffixes.items():
            if word.endswith(suff) and self.measure(word[:-len(suff)])>0:
                word=word[:-len(suff)]+replace
                break
        return word
    def fourthStep(self,word):
        """
        This method will perform additional replacement of suffices according to porter algorithem
        :param word:
        :return: word
        """
        suffixes = {
            "icate": "ic",
            "ative": "",
            "alize": "al",
            "iciti": "ic",
            "ical": "ic",
            "ful": "",
            "ness": ""
        }
        for suff,replace in suffixes.items():
            if word.endswith(suff) and self.measure(word[:-len(suff)])>0:
                word=word[:-len(suff)]+replace
                break
        return word
    def fifthStep(self,word):
        """
        This method will remove suffices when the remaining part has measure of cons..groups >1
        :param word:
        :return:word
        """
        suffixes = ["al", "ance", "ence", "er", "ic", "able", "ible", "ant", "ement", "ment", "ent", "ou", "ism", "ate",
                    "iti", "ous", "ive", "ize"]
        for suff in suffixes:
            if word.endswith(suff) and self.measure(word[:-len(suff)])>1:
                word=word[:-len(suff)]
                return word
        if word.endswith("ion") and self.measure(word[:-3])>1 and word[-4] in "st":
            word=word[:-3]
        return word
    def finalStage(self,word):
        """
        This method will handle the word that ends with e or double cons..
        :param word:
        :return:word
        """
        if word.endswith("e"):
            if self.measure(word[:-1])>1 or (self.measure(word[:-1])==1 and not self.endsWithCVC(word[:-1])):
                word=word[:-1]
        if self.endWithDoubleConsonants(word) and self.measure(word)>1 and word.endswith("l"):
            word=word[:-1]
        if len(word)>0 and not word[-1].isalpha():
            return self.finalStage(word[:-1])
        if len(word)>0 and not word[0].isalpha():
            return self.finalStage(word[1:])
        return word
    def stemmer(self,word):
        """
        This is the main method that will combine all functionality of the stemming..
        :param word:
        :return:word
        """
        if len(word)<2:
            return  word
        word=self.firstStep(word)
        word=self.secondStep(word)
        word=self.thirdStep(word)
        word=self.fourthStep(word)
        word=self.fifthStep(word)
        word=self.finalStage(word)
        return word
    def tokenWriter(self):
        """
         A writes the given tokens on the token file.
         :param :
         :return:
        """
        paths = self.pathReader()
        for path,doc in zip(paths,self.tokens):
            with open(path, "w") as current:
                for token in doc:
                    current.write(self.stemmer(token) + "\n")
    def tokenReader(self):
        """
        A method reads tokens from  the token file
        :param :
        :return:
        """
        paths = self.pathReader()
        self.tokens = []
        for path in paths:
            docs = []
            with open(path, "r") as current:
                lines = current.readlines()
                for line in lines:
                    docs.extend(line.split())
            self.tokens.append(docs)
    def pathReader(self):
        """
        This method reads every paths from give location and return them
        that are understandable by python
        :param :
        :return:paths
        """
        paths=[]
        try:
            with open(self.loc,"r") as current:
                lines=current.readlines()
                for line in lines:
                    if not line=="":
                        paths.append(line[:-1])
        except FileNotFoundError:
            print("File is not Found!")
        return paths
    def ____Excute____(self):
        self.tokenReader()
        self.tokenWriter()

class QueryStemmer:
    def __init__(self,loc):
        self.loc=loc
    def ____EXCUTE____(self):
        tokens=PorterStemmer(self.loc)
        tokens.____Excute____()
apps=PorterStemmer("C:\\Users\\HP\\Desktop\\IRSystem\\PathLocation\\locations2.txt")
apps.____Excute____()



