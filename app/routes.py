from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Product, Category

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    products = Product.query.order_by(Product.created_at.desc()).all()
    return render_template('index.html', products=products)


@bp.route('/products')
def products():
    products = Product.query.order_by(Product.name).all()
    return render_template('products.html', products=products)


@bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)


@bp.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price') or 0
        description = request.form.get('description')
        category_name = request.form.get('category')

        if not name:
            flash('Product name is required.', 'danger')
            return redirect(url_for('main.add_product'))

        try:
            price = float(price)
        except ValueError:
            flash('Invalid price value.', 'danger')
            return redirect(url_for('main.add_product'))

        category = None
        if category_name:
            category = Category.query.filter_by(name=category_name.strip()).first()
            if not category:
                category = Category(name=category_name.strip())
                db.session.add(category)

        product = Product(name=name.strip(), price=price, description=description, category=category)
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully.', 'success')
        return redirect(url_for('main.index'))

    # GET
    categories = Category.query.order_by(Category.name).all()
    return render_template('add_product.html', categories=categories)
