from tkinter import *
from .result import ResultWindow

class SearchWindow:

    def search_click(self):
        ResultWindow(self.searchInput.get())

    def __window(self):
        self.window = Tk()
        self.window.title("Search Movie Database")
        self.window.geometry('350x200')

    def __label_search_button(self):
        self.topTitle = Label(self.window, text="Search Database")
        self.searchInput = Entry(self.window, width=30)
        self.searchButton = Button(
            self.window, text="Search", command=self.search_click)

        self.topTitle.pack(side=TOP, pady=10)
        self.searchInput.pack(side=TOP, pady=5)
        self.searchButton.pack(side=TOP, pady=5)

    def __init__(self):
        self.__window()
        self.__label_search_button()
        self.window.mainloop()
