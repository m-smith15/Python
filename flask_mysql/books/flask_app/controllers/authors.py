from flask import render_template, redirect, request, session, url_for
from flask_app import app
from flask_app.models.authors import Author
from flask_app.models.books import Book

@app.route('/')
def landing():

    return redirect('/author')

@app.route('/author')
def authors_page():

    authors = Author.get_all_authors()
    return render_template("authors.html", all_authors = authors)

@app.route('/author/add', methods=["POST"])
def add_author():

    author_data = {
        "name": request.form["add_author"]
    }
    Author.add_author(author_data)
    return redirect('/author')

@app.route('/author/<int:authorid>')
def author_by_id(authorid):

    author_data = {
        "id": authorid
    }
    author = Author.get_author_by_id(author_data)
    favorites = Author.get_favorites_by_author(author_data)
    print(author)
    books_not_favorited = Book.get_books_not_favorited_by_authorid(author_data)
    return render_template("author_page.html", author = author, favorites = favorites, books_not_favorited = books_not_favorited)

@app.route('/author/<int:authorid>/add_favorite', methods=['POST'])
def author_add_favorite(authorid):

    data = {
        "book_id": request.form["add_favorite"],
        "author_id": authorid
    }
    Book.add_favorite_book(data)
    return redirect(url_for("author_by_id", authorid = authorid))

@app.route('/books')
def books_page():

    books = Book.get_all_books()
    return render_template("books.html", books = books)

@app.route('/books/<int:bookid>')
def book_by_id(bookid):

    book_data = {
        "id": bookid
    }
    book = Book.get_book_by_id(book_data)
    books_favorites = Book.get_favorites(book_data)
    add_favorite = Author.get_all_authors()
    return render_template("book_page.html", books = book, books_favorites = books_favorites, add_favorite = add_favorite)

@app.route('/books/<int:bookid>/add_favorite', methods=['POST'])
def book_add_favorite(bookid):

    data = {
        "book_id": bookid,
        "author_id": request.form["add_favorite"]
    }
    Book.add_favorite_book(data)
    return redirect(url_for("book_by_id", bookid = bookid))

@app.route('/books/create', methods=["POST"])
def add_book():

    book_data = {
        "title": request.form["new_book_name"],
        "num_of_pages": request.form["new_num_of_pages"]
    }
    Book.add_book(book_data)
    return redirect('/books')