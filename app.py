from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

all_products = {}

@app.route('/', methods=['GET', 'POST'])
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        category = request.form['category']

        price = float(price)

        if title in all_products:
            flash(f'Product {title} already exists!')
        else:
            all_products.update({title: {'price': price, 'category': category}})
            flash(f'Product {title} added!')

        return redirect(url_for('products'))

    return render_template('product.html', products=all_products)

@app.route('/delete/<name_product>')
def delete_product(name_product):
    all_products.pop(name_product)
    flash(f'Product {name_product} deleted!')

    return redirect(url_for('products'))



app.run(debug=True)