from collections import defaultdict
import math
class similarityRanker:
    """
    class to perform similarity measure and ranking based on term doc matrix
    """
    def __init__(self):
        """
        constructor for reading doc matrix and query vector from the doc
        """
        self.TermVectors=defaultdict(dict)
        self.QueryVector=defaultdict(int)
        path="C:\\Users\HP\\Desktop\\IRSystem\\TermDocMat\\TermDocMatrix.txt"
        with open(path,"r") as current:
            lines=current.readlines()
            for line in lines:
                line=line.split()
                left,right=0,1
                while right<len(line)-1:
                    self.TermVectors[line[left]][line[-1]]=line[right]
                    left=left+2
                    right=right+2
        path="C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\ProcessedQuery.txt"
        with open(path,"r") as current:
            lines=current.readlines()
            for line in lines:
                line=line.split("|")
                self.QueryVector[line[0][:-1]]=line[-1][:-1]
    def computeDistance(self,vector):
        """
        compute Eculidean distance of the vectors by assuming each weights as comp
        :param vector:
        :return:distance
        """
        distance=0
        for word in vector:
            distance+=float(vector[word])**2
        return math.sqrt(distance)
    def computeDot(self,index,query):
        """
        compute the dot product between the doc vector and query vector
        :param index:
        :param query:
        :return: dot product
        """
        dot=0
        for term in index:
            dot+=float(index[term])*float(query[term])
        return dot
    def computeCosine(self,index,query):
        """
        compute the cosine value between the doc vector and the query vector
        :param index:
        :param query:
        :return: cosime value
        """
        dot=self.computeDot(index,query)
        dis1=self.computeDistance(index)
        dis2=self.computeDistance(query)
        if not dis1 or not dis2:
            return 0
        return (dot)/(dis1*dis2)
    def simMeasure(self):
        """
        Ranking/arranges based on their similarity values
        :return:mesured
        """
        measured=[]
        for doc in self.TermVectors:
            current=self.computeCosine(self.TermVectors[doc],self.QueryVector)
            if current>0.00:
                measured.append((current,doc))
        measured.sort(reverse=True)
        return measured
    def docRanker(self):
        """
        compute futher modification of the doc
        :return:
        """
        measured=self.simMeasure()
        rankedDocs=[]
        for _,path in measured:
            path=path.replace("Tokenized","Documents")
            with open(path,"r",encoding='utf-8') as current:
                line=current.readlines(1)
                rankedDocs.append((path[39:-4],line))
        return rankedDocs
app=similarityRanker()
