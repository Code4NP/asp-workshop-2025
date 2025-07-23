from flask import Flask, jsonify, request
import json

app = Flask(__name__)

BGC0000001 = "data/mibig_data/BGC0000001.5.json"
BGC0000002 = "data/mibig_data/BGC0000002.5.json"

with open(BGC0000001, 'r') as f:
    bgc1 = json.load(f)

with open(BGC0000002, 'r') as f:
    bgc2 = json.load(f)

# Combine the data from both BGCs
combined_data = {
    "BGC0000001": bgc1,
    "BGC0000002": bgc2
}

combined_data["BGC0000001"].keys()

combined_data["BGC0000001"]["biosynthesis"]

for i in combined_data["BGC0000001"]["biosynthesis"]:
    print(i["name"])





# # GET - List all books
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)

# # GET - Get one book by ID
# @app.route('/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((b for b in books if b["id"] == book_id), None)
#     if book:
#         return jsonify(book)
#     return jsonify({"error": "Book not found"}), 404

# # POST - Add a new book
# @app.route('/books', methods=['POST'])
# def add_book():
#     new_book = request.json
#     books.append(new_book)
#     return jsonify(new_book), 201

# # PUT - Update a book
# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     book = next((b for b in books if b["id"] == book_id), None)
#     if book:
#         data = request.json
#         book.update(data)
#         return jsonify(book), 200
#     return jsonify({"error": "Book not found"}), 404

# # DELETE - Delete a book
# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     global books
#     books = [b for b in books if b["id"] != book_id]
#     return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    print(bgc1)
