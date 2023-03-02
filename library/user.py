# Class User
# In the user.py file, create class User. Upon initialization, it should receive user_id (int) and username (string). 
# The class should also have an instance attribute books that is an empty list. You should also create 2 instance methods:
# -	info() - returns a string containing the books currently rented by the user in ascending order separated by comma and space.
# -	__str__() - override the method to get a string in the following format "{user_id}, {username}, {list of rented books}"



class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []
    
    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available:
            self.books.append(book_name)
            library.books_available.remove(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user, books in library.rented_books.items():
            for book, days in books.items():
                if book == book_name:
                    return f"The book \"{book_name}\" is already rented and will be available in {days} days!"
    
    def return_book(self, author, book_name, library):
        if book_name in self.books:
            self.books.remove(book_name)
            library.books_available.append(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"
    
    def info(self):
        books = sorted(self.books)
        return ", ".join(books)
    
    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"