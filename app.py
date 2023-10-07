from flask import Flask , jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/search/<string:query>')
def search_product(query):
    # Your code to search for products based on the 'query' parameter
    # You will implement web scraping or API calls to fetch product data

    # Example response (replace with actual data)
    results = [
        {"name": "Product 1", "price": 100},
        {"name": "Product 2", "price": 150},
        # Add more products here
    ]

    return jsonify(results)
@app.route('/compare/<string:product_id_1>/<string:product_id_2>')
def compare_products(product_id_1, product_id_2):
    # Your code to compare products based on their IDs
    # You will implement logic to compare products and return the comparison

    # Example response (replace with actual data)
    comparison = {
        "product_1": {"name": "Product 1", "price": 100},
        "product_2": {"name": "Product 2", "price": 150},
        "result": "Product 1 is cheaper",
    }

    return jsonify(comparison)
if __name__ =="__main__":
    app.run(debug=True)
