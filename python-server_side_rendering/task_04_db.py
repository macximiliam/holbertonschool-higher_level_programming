#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open("products.json") as f:
        return json.load(f)


def read_csv():
    products = []

    with open("products.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })

    return products


def read_sql():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")

    rows = cursor.fetchall()

    conn.close()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    return products


@app.route("/products")
def products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    if source == "json":
        products = read_json()

    elif source == "csv":
        products = read_csv()

    else:
        try:
            products = read_sql()
        except Exception:
            return render_template("product_display.html", error="Database error")

    if product_id:

        product_id = int(product_id)

        filtered = [p for p in products if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        products = filtered

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
