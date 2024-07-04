from collections import Counter,defaultdict
import math
class TermDocumentMapper:
    """
    This class implements term document mapping for the index terms
    """
    def __init__(self):
        self.termDocument=defaultdict(list)
        self.uniqueTerms=set()
        self.TF_IDF=defaultdict(int)
        #Reads unique terms form the given document locations
        paths=self.pathFinder("C:\\Users\\HP\\Desktop\\IRSystem\\PathLocation\\locations2.txt")
        for path in paths:
            if path=="":
                continue
            with open(path,"r") as current:
                lines=current.readlines()
                for line in lines:
                    self.uniqueTerms.add(line)
        paths=self.pathFinder("C:\\Users\\HP\\Desktop\\IRSystem\\PathLocation\\locations2.txt")
        #Counts the frq... of each unique terms in their respective docs.
        for path in paths:
            if path=="":
                continue
            with open(path,"r") as current:
                lines=current.readlines()
                line_counter=Counter(lines)
                for word,freq in line_counter.items():
                    self.termDocument[word].append((path,freq))
        # compute idf and Writes what  it reads into the the given docs.. location.
        path="C:\\Users\\HP\Desktop\\IRSystem\\TermDocMat\\TermDocMatrix.txt"
        total_docs=len(paths)
        with open(path,"w") as current:
            for word in self.uniqueTerms:
                items=self.termDocument[word]
                idf = math.log(len(items) / total_docs)
                self.TF_IDF[word]=idf
                lines=[]
                for path,freq in items:
                    lines.append(path+" " +str(freq*idf)+" ")
                curated_res=" ".join(lines)+ " "+word
                current.write(curated_res+"\n")
        #write computed idf for later use ....  in search case.
        path="C:\\Users\\HP\\Desktop\\IRSystem\\TermDocMat\\TF_IDF_Unique.txt"
        with open(path,"w") as current:
            for word in self.TF_IDF:
                current.write(word+" "+str(self.TF_IDF[word])+"\n")

    def pathFinder(self,location):
        """
        Generates all paths that stores the given docs
        :param location:
        :return: paths
        """
        paths=[]
        try:
            with open(location,"r") as current:
                lines=current.readlines()
                for line in lines:
                    if not line=="":
                        paths.append(line[:-1])
        except FileNotFoundError:
            return False
        return paths
apps=TermDocumentMapper()
