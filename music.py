# Music
# Create a class named Music that receives title (string), artist (string), and lyrics (string) upon initialization. 
# The class should also have two additional methods:
# •	The print_info() method should return the following: 'This is "{title}" from "{artist}"'
# •	The play() method should return the lyrics.

class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics
