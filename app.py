from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import json
import os

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["flask_assignment"]
students = db["students"]
todo_items = db["todo_items"]


@app.route("/api")
def api():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        return jsonify(data)

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/", methods=["GET", "POST"])
def form():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        if not name or not email or not course:
            return render_template(
                "form.html",
                error="Please fill in all the fields."
            )

        if "@" not in email:
            return render_template(
                "form.html",
                error="Please enter a valid email."
            )

        try:
            student = {
                "name": name,
                "email": email,
                "course": course
            }

            students.insert_one(student)

            return redirect(url_for("success"))

        except Exception as error:
            return render_template(
                "form.html",
                error="Error submitting data: " + str(error)
            )

    return render_template("form.html")


@app.route("/todo")
def todo():
    return render_template("todo.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({
            "error": "Both itemName and itemDescription are required."
        }), 400

    try:
        todo_item = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        result = todo_items.insert_one(todo_item)

        return jsonify({
            "status": "success",
            "message": "To-Do item stored in MongoDB.",
            "_id": str(result.inserted_id),
            "item": todo_item
        }), 201

    except Exception as error:
        return jsonify({
            "status": "failed",
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)