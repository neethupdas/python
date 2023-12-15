class Publisher:
    def __init__(self, name):
        self.name = name
class Book(Publisher):
        def __init__(self, name, title, author):
            super().__init__(name)
            self.title = title
            self.author = author
        def show_Details(self):
            print(f"Publisher : {self.name}")
            print(f"Title : {self.title}")
            print(f"Author : {self.author}")
class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author) #Base class constructor invocation
        self.price = price
        self.no_of_pages = no_of_pages
    def show_Details(self): #Method Overriding.
        print(f"Publisher : {self.name}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price : {self.price}")
        print(f"Pages : {self.no_of_pages}")
b1 = Python("TMH", "Python for Beginners", "Peter", "Rs.350", 173)
b1.show_Details()
