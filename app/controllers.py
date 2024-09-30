from flask import request, jsonify
from .models import books

def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

def get_books():
    return jsonify(books)

def get_book_by_id(id):
    book = next((book for book in books if book['id'] == id), None)
    return jsonify(book) if book else ('', 404)

def edit_book_by_id(id):
    updated_book = request.get_json()
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(updated_book)
        return jsonify(book)
    return ('', 404)

def delete_book_by_id(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify(books)