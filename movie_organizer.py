# Movie Organizer
# Mary has a large collection of films, from old black-and-white classics to the newest blockbusters. But her collection is an unorganized jumble. She spends hours searching for a particular movie, only to find it in the most unexpected place. Mary needs your help to organize her movies.
# Write a function called "movie_organizer" that groups movies by genre. The function will receive a different number of arguments, passed as tuples containing two elements: the first one is the movie's name, and the second is the genre for example ("Movie Name", "Genre").
# The function should sort the movies by their genre. Arrange Mary's collection by the number of movies in each genre in descending order. If two or more genres have the same number of movies, return them in ascending order (alphabetically) by genre.
# Each genre group should be sorted in ascending order (alphabetically) by the movie's name.
# To help Mary keep track of her movies, add next to each genre the number of movies in the group.
# In the end, return the output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input from the console, just parameters passed to your function
# Output
# •	The output should look like this:
# "{genre_1} - {number_of_movies_in_the_genre_group}
# * {movie_name_1}
# * {movie_name_2}
# * {movie_name_3}
# …
# * {movie_name_n}
# {genre_2} - {number_of_movies_in_the_genre_group}
# * {movie_name_1}
# * {movie_name_2}
# …
# * {movie_name_n}
# {genre_n} - {number_of_movies_in_the_genre_group}
# * {movie_name_1}
# …
# * {movie_name_n}"
# Constraints
# •	Each tuple given will always contain a movie with its genre.
# •	You will never receive the same movie twice or more times.


def movie_organizer(*args):
    movies = {}
    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)
    result = []
    for genre, movies in sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{genre} - {len(movies)}")
        for movie in sorted(movies):
            result.append(f"* {movie}")
    return " ".join(result)

# print(movie_organizer(("The Matrix", "Action"), ("The Green Mile", "Drama"), ("Interstellar", "Sci-Fi"), ("Casablanca", "Drama"), ("The Notebook", "Romance"), ("The Godfather", "Crime"), ("Star Wars: Episode IV - A New Hope", "Sci-Fi"), ("The Wizard of Oz", "Family"), ("Citizen Kane", "Drama"), ("The Shawshank Redemption", "Crime"), ("The Godfather: Part II", "Crime"), ("The Dark Knight", "Action"), ("The Lord of the Rings: The Return of the King", "Action"), ("The Lord of the Rings: The Fellowship of the Ring", "Action"), ("The Lord of the Rings: The Two Towers", "Action"), ("The Avengers", "Action"), ("The Lion King", "Family"), ("The Dark Knight Rises", "Action"), ("The Wolf of Wall Street", "Crime"), ("The Prestige", "Sci-Fi"), ("The Departed", "Crime"), ("The Green Mile", "Crime"), ("The Usual Suspects", "Crime"), ("The Incredibles", "Family"), ("The Intouchables", "Drama"), ("The Pianist", "Drama"), ("The Departed", "Drama"), ("The Dark Knight", "Drama"), ("The Prestige", "Drama"), ("The Green Mile", "Drama"), ("The Usual Suspects", "Drama"), ("The Intouchables", "Crime"), ("The Pianist", "Crime"), ("The Departed", "Crime"), ("The Dark Knight", "Crime"), ("The Prestige", "Crime"), ("The Green Mile", "Crime"), ("The Usual Suspects", "Crime"), ("The Intouchables", "Sci-Fi"), ("The Pianist", "Sci-Fi"), ("The Departed", "Sci-Fi"), ("The Dark Knight", "Sci-Fi"), ("The Prestige", "Sci-Fi"), ("The Green Mile", "Sci-Fi"), ("The Usual Suspects", "Sci-Fi"), ("The Intouchables", "Romance"), ("The Pianist", "Romance"), ("The Departed", "Romance"), ("The Dark Knight", "Romance"), ("The Prestige", "Romance"), ("The Green Mile", "Romance"), ("The Usual Suspects