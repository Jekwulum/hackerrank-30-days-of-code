from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(self):
        pass

class Mybook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price = price
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        

title=input()
author=input()
price=int(input())
new_novel=Mybook(title,author,price)
new_novel.display()
