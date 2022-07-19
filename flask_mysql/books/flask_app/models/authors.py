from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app.models.books import Book

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(Author(author))
        return authors

    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO users (name) VALUES (%(name)s)"

        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_author_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"

        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_favorites_by_author(cls, data):
        query = "SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.user_id LEFT JOIN books ON favorites.book_id = books.id WHERE  users.id = %(id)s"

        return connectToMySQL('books_schema').query_db(query, data)
    