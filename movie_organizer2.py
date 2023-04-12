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





def movie_organizer(*movies):
    genre_dict = {}

    for movie in movies:
        movie_name, genre = movie
        if genre in genre_dict:
            genre_dict[genre].append(movie_name)
        else:
            genre_dict[genre] = [movie_name]

    for genre in genre_dict:
        genre_dict[genre].sort()

    sorted_genres = sorted(genre_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for genre, movie_names in sorted_genres:
        result.append(f"{genre} - {len(movie_names)}")
        for movie_name in movie_names:
            result.append(f"* {movie_name}")

    return "\n".join(result)
