# library
# list_of_books = ("bangedara" , "shikwae hind" , "islam" , "suriya ka perkash" )
class library:#class
    def __init__(self):#constructor
    #  """ intialize library with books and their locations (cupboad , column)."""
     self.books = {
        "python basics":(1, "a"),
        "bangedara":(2 , "h"),
        "shikwae hind ":(4,"b"),
        "islam":(1,"a"),
        "suriya ka perkash":(4,"c"),
        }#object or user input the books names
    def find_book(self, book_name):#exists of book
        # """find the book and returns its cupboad and column."""
        if book_name in self.books : 
            cupboad, column = self.books[book_name]#if found, it display the location of book.
            print(f" '{book_name}' is in cupboad {cupboad}. column {column}. ")
        else:
            print("book not found in the library.")#otherwise, it prints "book not found"
lib = library()#exchanging library to lib
book_name = input("enter book name :")#user input
lib.find_book(book_name)#indexing

