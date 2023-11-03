class Book:
    def __init__(self, bookid=None,title=None,price=None):
        self.bookid=bookid
        self.title=title
        self.price=price

    def showBook(self):
        return ({
            "book_id":self.bookid,
            "title": self.title,
            "price": self.price
            })
    

try:
    b1 = Book(129,"Alice in the Wonderland", 69)
    print(b1.showBook())
    print(f"Title of book is {b1.showBook()['price']}")
except Exception as e:
    print('Your code or input messed up!')
    print(f"\n here is detail:\n{e}")