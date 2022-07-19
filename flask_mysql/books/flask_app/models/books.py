from flask_app.config.mysqlconnection import connectToMySQL 

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_books_not_favorited_by_authorid(cls, data):
        #this returns all books...need to tweak query so it only returns books not currently favorited
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id WHERE favorites.user_id != %(id)s"

        results = connectToMySQL('books_schema').query_db(query, data)

        books = []

        books.append(Book(results[0]))

        for row in results:
            if row['id'] != books[-1].id:
                books.append(Book(row))

        return books

    @classmethod
    def add_favorite_book(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(author_id)s, %(book_id)s)"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * from books"
        return connectToMySQL('books_schema').query_db(query)

    @classmethod
    def get_book_by_id(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_favorites(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id JOIN users ON favorites.user_id = users.id WHERE  books.id = %(id)s"

        return connectToMySQL('books_schema').query_db(query, data)

        # authors = []
        # if len(results) < 1:
        #     return authors
        # authors.append(Book(results[0]))

        # for row in results:
        #     if row['id'] != authors[-1].id:
        #         authors.append(Book(row))

        # return authors

    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s)"

        return connectToMySQL('books_schema').query_db(query, data)