from flask import Flask , jsonify
app=Flask(__name__)

# creacion de rutas y entregar datos de productos
from  products import products
@app.route('/ping')
# declar una funcion
def ping():
  return jsonify({"message":"pong"})

# crer una nueva ruta
@app.route('/products')
def getProducts():
  return jsonify({"products":products, "message":"Product's List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
  productsFound=[product for product in products if product['name']==product_name]
  # tomamos de base la longitud 
  if(len(productsFound)>0):
    return jsonify({"product":productsFound[0]})
    return jsonify({"message":"Product not found"})


if __name__ == '__main__':
  app.run(debug=True, port=3000)
