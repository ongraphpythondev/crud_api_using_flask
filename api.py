from settings import *

#Init db 
db = SQLAlchemy(app)

#Init ma
ma = Marshmallow(app)
api = Api(app)


# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Get All Products
@app.route('/product', methods=['GET'])
def all_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    #print(type(jsonify(result)))
    return jsonify(result)


# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get Single Product
@app.route('/product/<int:id>', methods=['GET'])
def product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    db.session.commit()

    return product_schema.jsonify(product)

@app.route('/product/<int:id>',methods=['PATCH'])
def partial_update(id):
    product = Product.query.get_or_404(id)
    data = request.json

    if data.get('name'):
        product.name = data.get('name')
    if data.get('description'):
        product.description = data.get('description')
    if data.get('price'):
        product.price = data.get('price')
    if data.get('qty'):
        product.qty = data.get('qty')

    db.session.commit()
    return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({"message":"product is deleted"})


#Run server
if __name__ == '__main__':
    app.run(debug=True,port=8000)
