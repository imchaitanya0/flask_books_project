from flask import Flask,request,jsonify

app=Flask(__name__)

books=[
    {"id":1,"name":"book1","author":"a1"},
    {"id":2,"name":"book2","author":"a2"}
]
def find(id):
    return next((book for book in books if book["id"]==id),None)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book_id(id):
    book=find(id)
    if book:
        return jsonify(book)
    return jsonify({"error":"not found the book"}),404

@app.route('/books',methods=['POST'])
def add_books():
    if not request.json or "name" not in request.json or "author" not in request.json:
        return jsonify({'error adding the book' : 'check the details'}),400
    book={
        'id':books[-1]['id']+1 if books else 1,
        'name':request.json['name'],
        "author":request.json["author"]
    }
    books.append(book)

    return jsonify(book),201
@app.route('/books/<int:id>',methods=["PUT"])
def upd_book(id):
    book=find(id)
    if not book:
        return jsonify({"error" :"book not found"}),404
    if not request.json:
        return jsonify({"error":"provided info not in correct format"}),400
    book['name']=request.json.get('name',book['name'])
    book['author']=request.json.get('author',book['author'])

    return jsonify(book)
@app.route('/books/<int:id>',methods=['DELETE'])
def del_book(id):
    book=find(id)
    if not book:
        return jsonify({"error":"book not found"}),404
    books.remove(book)
    
    return jsonify({"message":"book deleted"}),200


if __name__=='__main__':
    app.run(debug=True)