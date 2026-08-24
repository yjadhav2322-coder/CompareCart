from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from models import (
    db,
    Product,
    Seller,
    Price,
    Feedback,
    User,
    Wishlist,
    CartItem
)

import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "comparecart-development-key"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comparecart.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.context_processor
def inject_cart_count():

    cart_count = 0

    if session.get("user_id"):

        cart_items = CartItem.query.filter_by(
            user_id=session["user_id"]
        ).all()

        cart_count = sum(
            item.quantity
            for item in cart_items
        )

    return dict(
        cart_count=cart_count
    )
# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    products = Product.query.all()

    return render_template(
        "index.html",
        products=products
    )

# ==========================================
# SEARCH PAGE
# ==========================================

@app.route("/search")
def search():

    query = request.args.get("q", "").strip()

    if not query:
        return render_template(
            "results.html",
            query="",
            products=[],
            best_price=None
        )

    matching_products = Product.query.filter(
        db.or_(
            Product.name.ilike(f"%{query}%"),
            Product.category.ilike(f"%{query}%")
        )
    ).all()

    products = []

    for product in matching_products:

        valid_prices = [
            price.price
            for price in product.prices
            if price.price is not None
        ]

        if valid_prices:

            lowest_price = min(valid_prices)

            availability = next(
                (
                    price.availability
                    for price in product.prices
                    if price.price == lowest_price
                ),
                "Out of Stock"
            )

            products.append({
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "description": product.description,
                "image": product.image,
                "price": lowest_price,
                "rating": 4.5,
                "availability": availability
            })

    best_price = None

    if products:
        best_price = min(
            product["price"]
            for product in products
        )

    return render_template(
        "results.html",
        query=query,
        products=products,
        best_price=best_price
    )

    # Demo product data
    # Later we will connect this to the scraper/database

    products = [
        {
            "id": 1,
            "name": query if query else "iPhone 15",
            "store": "Store A",
            "price": 55999,
            "rating": 4.5,
            "availability": "In Stock",
            "url": "https://www.google.com"
        },

        {
            "id": 2,
            "name": query if query else "iPhone 15",
            "store": "Store B",
            "price": 52999,
            "rating": 4.4,
            "availability": "In Stock",
            "url": "https://www.google.com"
        },

        {
            "id": 3,
            "name": query if query else "iPhone 15",
            "store": "Store C",
            "price": 54499,
            "rating": 4.3,
            "availability": "In Stock",
            "url": "https://www.google.com"
        }
    ]

    # Find the lowest price

    best_price = min(
        product["price"]
        for product in products
    )

    return render_template(
        "results.html",
        query=query,
        products=products,
        best_price=best_price
    )


# ==========================================
# PRODUCT DETAILS PAGE
# ==========================================

@app.route("/product/<int:product_id>")
def product(product_id):

    selected_product = Product.query.get_or_404(product_id)

    sellers = selected_product.prices

    best_price = None

    if sellers:
        best_price = min(
            seller.price
            for seller in sellers
        )

    feedbacks = Feedback.query.filter_by(
        product_id=product_id
    ).order_by(
        Feedback.created_at.desc()
    ).all()

    return render_template(
        "product.html",
        product=selected_product,
        sellers=sellers,
        best_price=best_price,
        feedbacks=feedbacks
    )

# ==========================================
# ADD PRODUCT TO WISHLIST
# ==========================================

@app.route("/wishlist/add/<int:product_id>", methods=["POST"])
def add_to_wishlist(product_id):

    if not session.get("user_id"):
        return redirect("/login")

    existing_item = Wishlist.query.filter_by(
        user_id=session["user_id"],
        product_id=product_id
    ).first()

    if not existing_item:
        new_item = Wishlist(
            user_id=session["user_id"],
            product_id=product_id
        )

        db.session.add(new_item)
        db.session.commit()

    return redirect(request.referrer or "/products")


# ==========================================
# ADD PRODUCT FEEDBACK
# ==========================================

@app.route("/product/<int:product_id>/feedback", methods=["POST"])
def add_feedback(product_id):

    name = request.form.get("name")
    rating = request.form.get("rating")
    comment = request.form.get("comment")

    new_feedback = Feedback(
        product_id=product_id,
        name=name,
        rating=int(rating),
        comment=comment
    )

    db.session.add(new_feedback)
    db.session.commit()

    return redirect(f"/product/{product_id}")


# ==========================================
# ALL PRODUCTS PAGE
# ==========================================

@app.route("/products")
def all_products():

    products = Product.query.all()

    return render_template(
        "all_products.html",
        products=products
    )      

# ==========================================
# CATEGORY PRODUCTS PAGE
# ==========================================

@app.route("/products/<category>")
def category_products(category):

    if category.lower() == "all":
        products = Product.query.all()
        page_title = "All Products"
    else:
        products = Product.query.filter_by(
            category=category
        ).all()
        page_title = category

    return render_template(
        "all_products.html",
        products=products,
        page_title=page_title
    )

# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            return render_template(
                "register.html",
                error="Please fill in all fields."
            )

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            return render_template(
                "register.html",
                error="An account with this email already exists."
            )

        hashed_password = generate_password_hash(password)

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        session["user_id"] = new_user.id
        session["user_name"] = new_user.name

        return redirect(url_for("home"))

    return render_template("register.html")

# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(
            email=email
        ).first()

        if not user or not check_password_hash(
            user.password,
            password
        ):
            return render_template(
                "login.html",
                error="Invalid email or password."
            )

        session["user_id"] = user.id
        session["user_name"] = user.name

        return redirect(url_for("home"))

    return render_template("login.html")

# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

# ==========================================
# ACCOUNT
# ==========================================

@app.route("/account")
def account():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get_or_404(
        session["user_id"]
    )

    return render_template(
        "account.html",
        user=user
    ) 


@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    if request.method == "POST":

        name = request.form.get("name")
        rating = request.form.get("rating")
        comment = request.form.get("comment")

        new_feedback = Feedback(
            name=name,
            rating=int(rating),
            comment=comment
        )

        db.session.add(new_feedback)
        db.session.commit()

        return redirect("/feedback")

    feedbacks = Feedback.query.order_by(
        Feedback.created_at.desc()
    ).all()

    return render_template(
        "feedback.html",
        feedbacks=feedbacks
    )

# ==========================================
# WISHLIST
# ==========================================

@app.route("/wishlist")
def wishlist():

    if not session.get("user_id"):
        return redirect("/login")

    wishlist_items = Wishlist.query.filter_by(
        user_id=session["user_id"]
    ).all()

    return render_template(
        "wishlist.html",
        wishlist_items=wishlist_items
    )


@app.route("/wishlist/remove/<int:item_id>", methods=["POST"])
def remove_from_wishlist(item_id):

    if not session.get("user_id"):
        return redirect("/login")

    item = Wishlist.query.filter_by(
        id=item_id,
        user_id=session["user_id"]
    ).first_or_404()

    db.session.delete(item)
    db.session.commit()

    return redirect("/wishlist")


# ==========================================
# ADD PRODUCT TO CART
# ==========================================

@app.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):

    if not session.get("user_id"):
        return redirect("/login")

    existing_item = CartItem.query.filter_by(
        user_id=session["user_id"],
        product_id=product_id
    ).first()

    if existing_item:

        existing_item.quantity += 1

    else:

        new_item = CartItem(
            user_id=session["user_id"],
            product_id=product_id,
            quantity=1
        )

        db.session.add(new_item)

    db.session.commit()

    return redirect(request.referrer or "/cart")

# ==========================================
# CART PAGE
# ==========================================

@app.route("/cart")

def cart():

    if not session.get("user_id"):

        return redirect("/login")

    cart_items = CartItem.query.filter_by(

        user_id=session["user_id"]

    ).all()


    subtotal = 0


    for item in cart_items:

        if item.product.prices:

            lowest_price = min(

                price.price

                for price in item.product.prices

                if price.price is not None

            )

            subtotal += lowest_price * item.quantity


    return render_template(

        "cart.html",

        cart_items=cart_items,

        subtotal=subtotal

    )

# ==========================================
# INCREASE CART QUANTITY
# ==========================================

@app.route("/cart/increase/<int:item_id>", methods=["POST"])
def increase_cart(item_id):

    if not session.get("user_id"):
        return redirect("/login")

    item = CartItem.query.filter_by(
        id=item_id,
        user_id=session["user_id"]
    ).first_or_404()

    item.quantity += 1

    db.session.commit()

    return redirect("/cart")


# ==========================================
# DECREASE CART QUANTITY
# ==========================================

@app.route("/cart/decrease/<int:item_id>", methods=["POST"])
def decrease_cart(item_id):

    if not session.get("user_id"):
        return redirect("/login")

    item = CartItem.query.filter_by(
        id=item_id,
        user_id=session["user_id"]
    ).first_or_404()

    if item.quantity > 1:

        item.quantity -= 1

    else:

        db.session.delete(item)

    db.session.commit()

    return redirect("/cart")


# ==========================================
# REMOVE FROM CART
# ==========================================

@app.route("/cart/remove/<int:item_id>", methods=["POST"])
def remove_from_cart(item_id):

    if not session.get("user_id"):
        return redirect("/login")

    item = CartItem.query.filter_by(
        id=item_id,
        user_id=session["user_id"]
    ).first_or_404()

    db.session.delete(item)

    db.session.commit()

    return redirect("/cart")

# ==========================================
# CHECKOUT PAGE
# ==========================================

@app.route("/checkout")
def checkout():

    if not session.get("user_id"):
        return redirect("/login")

    cart_items = CartItem.query.filter_by(
        user_id=session["user_id"]
    ).all()

    if not cart_items:
        return redirect("/cart")

    subtotal = 0

    for item in cart_items:

        if item.product.prices:

            valid_prices = [
                price
                for price in item.product.prices
                if price.price is not None
            ]

            if valid_prices:

                # Find the lowest price
                best_price = min(
                    valid_prices,
                    key=lambda price: price.price
                )

                # Calculate subtotal
                subtotal += best_price.price * item.quantity

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        subtotal=subtotal
    )
    


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(debug=True)
