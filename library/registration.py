# Class Registration 
# In the registration.py, create a class called Registration. Upon initialization, 
# It will not receive anything, but we'll have these three methods.
# -	add_user(user: User, library: Library):
# o	Adds the user if we do not have them in the library's user records already
# o	Otherwise, returns the message "User with id = {user_id} already registered in the library!"
# -	remove_user(user: User, library: Library):
# o	Removes the user from the library records if present
# o	Otherwise, returns the message "We could not find such user to remove!"
# -	change_username(user_id: int, new_username: str, library: Library):
# o	If there is a record with the same user id in the library and the username is different than the provided one, 
# changes the username with the new one provided and returns the message "Username successfully changed to: {new_username} for user id: {user_id}". Changes his username in the rented_books dictionary as well (if present).
# o	If the new username is the same for this id, returns the following message "Please check again the provided username - it should be different than the username used so far!".
# o	If there is no record for the provided id returns "There is no user with id = {user_id}!"



class Registration:
    def __init__(self):
        pass
    
    def add_user(self, user, library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"
    
    def remove_user(self, user, library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"
    
    def change_username(self, user_id, new_username, library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    user.username = new_username
                    if user.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(user.username)
                    return f"Username successfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"
    
    def get_book(self, author, book_name, days_to_return, user):
        if book_name in library.books_available:
            user.books.append(book_name)
            library.books_available.remove(book_name)
            if user.username not in library.rented_books:
                library.rented_books[user.username] = {}
            library.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for user, books in library.rented_books.items():
            for book, days in books.items():
                if book == book_name:
                    return f"The book \"{book_name}\" is already rented and will be available in {days} days!"
    
    def return_book(self, author, book_name, user):
        if book_name in user.books:
            user.books.remove(book_name)
            library.books_available.append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
    
    def info(self):
        return f"{', '.join(sorted(self.user_records))}"
    
    def __repr__(self):
        return f"{self.user_records} library: {self.books_available}"
    
    def __str__(self):
        return f"{self.user_records} library: {self.books_available}"


