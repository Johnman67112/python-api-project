from flask import Blueprint
from .controllers import add_book, get_books, get_book_by_id, edit_book_by_id, delete_book_by_id

main = Blueprint('main', __name__)

main.route('/books', methods=['POST'])(add_book)
main.route('/books', methods=['GET'])(get_books)
main.route('/books/<int:id>', methods=['GET'])(get_book_by_id)
main.route('/books/<int:id>', methods=['PUT'])(edit_book_by_id)
main.route('/books/<int:id>', methods=['DELETE'])(delete_book_by_id)