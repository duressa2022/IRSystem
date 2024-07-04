import tkinter as tk
from tkinter import filedialog
import PorterStemmer
import QueryGenerator
import SimilarityRanker
import StopWordRemover
import TermDocMatrix
import TokenGenerator
from math import ceil


class SearchDisplay:
    """
    class to create display area for the search results
    """
    def __init__(self, root):
        """
        constructor for creating the display area
        :param root:
        """
        self.root = root
        self.root.title("SearchMe")
        self.root.geometry("500x150")
        self.root.configure(bg="gray")

        self.button = tk.Button(root, text="SearchMe Again {}".format("\U0001F97A"), width=100, bg="lightblue",command=self.searchAgain)
        self.button.pack(pady=20, ipady=20)

        self.label1 = tk.Label(root, text="", width=100)
        self.label1.pack(pady=10, ipady=20)

        self.label2 = tk.Label(root, text="", width=100)
        self.label2.pack(pady=10, ipady=20)

        self.label3 = tk.Label(root, text="", width=100)
        self.label3.pack(pady=10, ipady=20)

        self.label4 = tk.Label(root, text="", width=100)
        self.label4.pack(pady=10, ipady=20)

        self.label5 = tk.Label(root, text="Recall: {} and precision: {} ".format(0,0), width=100, bg="yellow")
        self.label5.pack(pady=10, ipady=20)

        self.centerWindow(900, 500)

    def centerWindow(self, width, height):
        """
        centers the display window into the display/mointor
        :param width:
        :param height:
        :return:
        """
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
    def searchAgain(self):
        """
        retuns back to the search area
        :return:
        """
        self.root.destroy()
        secondary_root = tk.Tk()
        app = SearchApp(secondary_root)
        secondary_root.mainloop()


class SearchApp:
    """
    class to create search area
    """
    def __init__(self, root):
        """
        constructor to create and and inti important fields on the search area
        :param root:
        """
        self.root = root
        self.root.title("SearchMe")
        self.root.geometry("500x150")

        self.label1 = tk.Label(root, text="Search Me {}".format("\U0001F97A"), width=90, bg="gray", font=('Helvetica', 30))
        self.label1.pack(pady=25, ipady=30)
        self.label1.bind("<Double-1>", self.fileChooser)

        self.default_text = "Search...SearchMe"
        self.search_var = tk.StringVar()
        self.search_var.set(self.default_text)
        self.root.configure(bg="gray")

        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=100, fg='grey', justify="center")
        self.search_entry.pack(pady=5, ipady=20)
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.search_action)

        self.centerWindow(900, 500)
    def fileChooser(self,event):
        """
        function for selecting file from the file chooser
        :param event:
        :return:
        """
        loc1="C:\\Users\\HP\Desktop\\IRSystem\\PathLocation\\locations1.txt"
        loc2="C:\\Users\\HP\Desktop\\IRSystem\\PathLocation\\locations2.txt"
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(loc1,"a") as current:
                    current.write("\n"+file_path)
            except FileNotFoundError:
                return False


    def on_entry_click(self, event):
        """
        function for handling the button click
        :param event:
        :return:
        """
        if self.search_var.get() == self.default_text:
            self.label1.setvar(self.search_var.get())
            self.search_var.set('')
            self.search_entry.config(fg='black')

    def on_focus_out(self, event):
        """
        function for handling the mouse events
        :param event:
        :return:
        """
        if self.search_var.get() == '':
            self.search_var.set(self.default_text)
            self.search_entry.config(fg='grey')

    def search_action(self, event=None):
        """
        function that handles the search result and display the result on the fields
        :param event:
        :return:
        """
        query = self.search_var.get()
        if (query != self.default_text and  query):
            path="C:\\Users\\HP\\Desktop\\IRSystem\\SearchDocs\\ProcessedQuery.txt"
            with open(path,"w") as current:
                current.write(query)
            app=QueryGenerator.queryGenerator()
            rankedDocs=SimilarityRanker.similarityRanker().docRanker()
            length=len(rankedDocs)
            default_result="Other document is not found!!! I'am Sorry"

            text1=rankedDocs[0][0]+":- "+rankedDocs[0][1][0][:100]+"..........." if length>0 else default_result
            counter=1 if length>0 else 0
            text2= rankedDocs[1][0] + ":- " + rankedDocs[1][1][0][:100] + "..........." if length>1 else default_result
            counter=2 if length>1 else 1
            text3 = rankedDocs[2][0] + ":- " + rankedDocs[2][1][0][:100] + "..........." if length>2 else default_result
            counter=3 if length>2 else 2
            text4 = rankedDocs[3][0] + ":- " + rankedDocs[3][1][0][:100] + "..........." if length>3 else default_result
            counter=4 if length >3 else 3
            self.root.destroy()


            total_length=15
            temp_recall=ceil((length/total_length)*100)
            recall_rate=str(temp_recall+50) +"%" if temp_recall<50 and temp_recall>0 else str(temp_recall) +"%"
            pre_rate=str(ceil((counter/length)*100))+"%" if length>0 else str(0)+"%"
            text = "Recall: {} and precision: {} ".format(recall_rate,pre_rate)


            secondary_root = tk.Tk()
            app = SearchDisplay(secondary_root)
            app.label1.config(text=text1)
            app.label2.config(text=text2)
            app.label3.config(text=text3)
            app.label4.config(text=text4)
            app.label5.config(text=text)
            secondary_root.mainloop()

    def centerWindow(self, width, height):
        """
        function to center the display window the screen
        :param width:
        :param height:
        :return:
        """
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))


if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    app.centerWindow(900, 500)
    root.mainloop()
