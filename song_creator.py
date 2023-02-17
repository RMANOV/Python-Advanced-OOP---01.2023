# Song Creator
# Create a function called add_songs().
# It receives one or many tuples. Each tuple consists of exactly two elements - the song's title in the first position and a list in the second position. The list can consist of one, many, or no strings - each representing a line of the lyrics of the song. 
# The function collects the information and concatenates the lyrics for each song (each string on a different line). If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.
# In the end, it should return a string for each song with its lyrics in the format:
# "- {song_title}"
# "{first_line_of_lyrics}"
# "{second_line_of_lyrics}"
# …
# "{nth_line_of_lyrics}"
# If there are no lyrics given for a song, return just its title in the format shown above.
# For more clarification, see the examples below.
# Input
# •	There will be no input, just tuples passed to your function.
# Output
# •	Return the desired result as described above.
# Constraints:
# •	You will always have a song's name on the first position of the tuple.


# def add_songs(*args):
#     songs = {}
#     for song in args:
#         if song[0] not in songs:
#             songs[song[0]] = song[1]
#         else:
#             songs[song[0]] += song[1]
#     result = []
#     for song in songs:
#         result.append(f"- {song}")
        
#     for song in songs:
#         for line in songs[song]:
#             result.append(line)
    
#     return "\n".join(result)

def add_songs(*songs):
    song_lyrics = {}
    for song, lyrics in songs:
        if song not in song_lyrics:
            song_lyrics[song] = []
        song_lyrics[song].extend(lyrics)
    
    results = []
    for song, lyrics in song_lyrics.items():
        results.append(f"- {song}")
        if lyrics:
            results.extend(lyrics)
    
    return "\n".join(results)



print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
