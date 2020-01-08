from tkinter import *
import urllib.request
import json


class ResultWindow():

    def __window(self):
        self.window = Tk()
        self.window.title("Results")
        self.window.geometry('350x200')

    def _scrollbar_searchValue(self):
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side=LEFT, fill=Y)

        self.searchValueLabel = Label(self.window, text=self.searchValue)
        self.searchValueLabel.pack(side=TOP, pady=10)

    def __get_results(self):
        with urllib.request.urlopen("http://localhost:3000/search/" + self.searchValue) as url:
            results = json.loads(url.read().decode())

        self.__render_results(results)

    def __render_results(self, results):
        mylist = Listbox(self.window, yscrollcommand=self.scrollbar.set)

        for result in results:
            mylist.insert(END, result.get("title"))

        mylist.pack(side=TOP, fill=BOTH)
        self.scrollbar.config(command=mylist.yview)

    def __init__(self, searchValue):
        self.searchValue = searchValue

        self.__window()
        self._scrollbar_searchValue()
        self.__get_results()
        self.window.mainloop()
