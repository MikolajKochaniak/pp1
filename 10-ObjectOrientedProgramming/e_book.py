class E_book():
    def __init__(self, title, author, no_of_pages):
        self.title = title
        self.author = author
        self.pages = no_of_pages
        self.current_page = 0
        self.is_open = False
    def open(self): 
        self.is_open = True
    def close(self):
        self.is_open = False
    def next_page(self):
        if not self.is_open:
            print("Książka jest zamknięta")
            return None
        if self.current_page<self.pages:
            self.current_page+=1 
    def previous_page(self):
        if not self.is_open:
            print("Książka jest zamknięta")
            return None
        if self.current_page>0:
            self.current_page-=1    
    def status(self):
        print(f'Autor:{self.author},Tytuł:{self.title},Liczba stron:{self.pages}, Aktualna strone: {self.current_page}')







