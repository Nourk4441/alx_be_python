class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year

    def __del__(self):
        print("Deleting",self.title)

    def __str__(self):
            """Return a readable string representation of the book."""
            return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a detailed string representation for debugging."""
        return f"Book('{self.title}', '{self.author}', {self.year})"           