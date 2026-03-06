#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

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


@app.route("/products")
def products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    # ❌ source inválido
    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    # 📂 leer archivo
    if source == "json":
        products = read_json()
    else:
        products = read_csv()

    # 🔎 filtrar por id
    if product_id:
        product_id = int(product_id)

        filtered = [p for p in products if p["id"] == product_id]

        if not filtered:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

        products = filtered

    return render_template(
        "product_display.html",
        products=products
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
