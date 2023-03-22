# Photo Album
# Create a class called PhotoAlbum. Upon initialization, it should receive pages (int). It should also have one more attribute: photos (empty matrix) representing the album with its pages where you should put the photos. Each page can contain only 4 photos. The class should also have 3 more methods:
# •	from_photos_count(photos_count: int) - creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos.
# •	add_photo(label:str) - adds the photo in the first possible page and slot and return "{label} photo added successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}". If there are no free slots left, return "No more free slots"
# •	display() - returns a string representation of each page and the photos in it. Each photo is marked with "[]", and the page separation is made using 11 dashes (-). For example, if we have 1 page and 2 photos:
# -----------
# [] []
# -----------
# and if we have 2 empty pages:
# -----------

# -----------

# -----------


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)] # create an empty matrix of pages and slots

    @classmethod
    def from_photos_count(cls, photos_count: int):
        # calculate the number of pages needed to fit all photos
        pages = photos_count // 4 + (1 if photos_count % 4 else 0)
        return cls(pages) # create a new instance of PhotoAlbum with the calculated pages

    def add_photo(self, label: str):
        # loop through the pages and slots to find an empty one
        for page_index in range(len(self.photos)):
            page = self.photos[page_index]
            if len(page) < 4: # check if there is a free slot on this page
                page.append(label) # add the photo label to the slot
                return f"{label} photo added successfully on page {page_index + 1} slot {len(page)}" # return a success message with the page and slot numbers
        return "No more free slots" # return a failure message if no free slots are found

    def display(self):
        result = "" # initialize an empty string to store the result
        for page in self.photos: # loop through each page
            result += "-" * 11 + "\n" # add a separator line of dashes
            result += " ".join(["[]" for _ in range(len(page))]) + "\n" # add a row of brackets representing the photos on this page
        result += "-" * 11 + "\n" # add a final separator line of dashes
        return result # return the result string