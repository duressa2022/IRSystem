from collections import Counter,defaultdict
import PorterStemmer
import StopWordRemover
import TokenGenerator
class queryGenerator:
    def __init__(self):
        self.Unique_idf = defaultdict(int)
        self.tokens=[]
        token=TokenGenerator.QueryTokenizer("C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\QueryPath.txt")
        token.____EXCUTE____()
        token=StopWordRemover.QueryProcesser("C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\QueryPath.txt")
        token.____EXCUTE____()
        token=PorterStemmer.QueryStemmer("C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\QueryPath.txt")
        token.____EXCUTE____()
        paths=TokenGenerator.TokenGenerator("C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\QueryPath.txt",
                                             "C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\QueryPath.txt").pathReader("C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\QueryPath.txt")

        path="C:\\Users\\HP\\Desktop\\IRSystem\\TermDocMat\\TF_IDF_Unique.txt"
        with open(path,"r") as current:
            lines=current.readlines()
            left,right=0,1
            while right<len(lines):
                self.Unique_idf[lines[left][:-1]]=lines[right][:-1]
                left=left+1
                right=right+1

        for path in paths:
            with open(path,"r") as current:
                lines=current.readlines()
                for line in lines:
                    self.tokens.append(line[:-1])
        word_counter=Counter(self.tokens)
        for path in paths:
            with open(path,"w") as current:
                for word,freq in word_counter.items():
                    current.write(word+ " |"+str(float(freq)*float(self.Unique_idf[word]))+"\n")

q=queryGenerator()


