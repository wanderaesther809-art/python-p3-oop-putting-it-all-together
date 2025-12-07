class Book:
    def __init__(self, title="Unknown", page_count=0):
        self.title = title
        self.page_count = page_count

    # Title property
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value.title()
        else:
            raise ValueError("Title must be a string")

    # Page count property
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Method to turn page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
