# The Band class should receive a name (string) upon initialization. It also has an attribute albums (an empty list). 
# The class has three methods:
# -	add_album(album: Album)
# o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
# o	If the album is already added, returns "Band {band_name} already has {album_name} in their library."
# -	remove_album(album_name: str)
# o	Removes the album from the collection and returns "Album {name} has been removed."
# o	If the album is published, returns "Album has been published. It cannot be removed."
# o	If the album is not in the collection, returns "Album {name} is not found."
# -	details()
# o	Returns the information of the band, with their albums, in this format: 
# "Band {name}
#  {album details}
#  ...
#  {album details}"



class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}"
        return result