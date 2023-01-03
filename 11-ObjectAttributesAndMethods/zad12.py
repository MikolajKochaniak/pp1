class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"

class PaperBook(Book):
    def __init__(self,title,author,pages):
        Book.__init__(self, title, author)
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"
class Ebook(Book):
    def __init__(self,title,author,file):
        Book.__init__(self,title,author)
        self.file = file


book1 = Book("Masno","Masny ben")
book2 = PaperBook("Masno","Masny ben","44")



