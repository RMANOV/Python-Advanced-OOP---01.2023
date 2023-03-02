# Class Library
# In the library.py create a class Library. Upon initialization, it will not receive anything, 
# but it should have the following instance attributes: 
# o	user_records - an empty list that will store the users (users objects) of the library
# o	books_available - an empty dictionary that will keep information regarding the authors (key: str) and the books available for each of the authors (list of strings)
# o	rented_books - an empty dictionary that will keep information regarding the usernames (key: str) and nested dictionary as a value in which will keep information regarding the book names (key: str) and days left before returning the book to the library (int) - ({usernames: {book names: days to return}}).
# You should also create 2 additional instance methods:
# -	get_book(author: str, book_name: str, days_to_return: int, user: User):
# o	If the book is available in the library adds it to the books list for this user, 
# updates the library records (rented_books and available_books dicts), 
# and returns the following message: "{book_name} successfully rented for the next {days_to_return} days!"
# o	If it is already rented, returns the following message "The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!"
# -	return_book(author:str, book_name:str, user: User):
# o	If the book is in the user's books list, returns it in the library (update books_available and rented_books class attributes) and removes it from the books list for this user
# o	Otherwise, returns the following message "{username} doesn't have this book in his/her records!"


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}
    
    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
    
    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
    
    def change_username(self, user_id, new_username):
        for user in self.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    user.username = new_username
                    return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"
    
    def get_book(self, author, book_name, days_to_return, user):
        if book_name in self.books_available:
            user.books.append(book_name)
            self.books_available.pop(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user, books in self.rented_books.items():
            for book, days in books.items():
                if book == book_name:
                    return f"The book \"{book_name}\" is already rented and will be available in {days} days!"
    
    def return_book(self, author, book_name, user):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[book_name] = book_name
        else:
            return f"{user.username} doesn't have this book in his/her records!"
    
    def info(self):
        books = sorted(self.books)
        return ", ".join(books)
    
    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
