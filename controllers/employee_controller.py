# controllers/employee_controller.py
from flask import Blueprint, jsonify, request, render_template, redirect
from models.employee_model import employees

print (__name__)

employee_bp = Blueprint("employee_bp", __name__)

# READ ALL  ->  GET /employees
@employee_bp.route("/employees", methods=["GET"])
def list_employees():
    return jsonify(employees), 200

# READ ONE  ->  GET /employees/3
@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    for e in employees:
        if e["id"] == id:
            return jsonify(e), 200
    return jsonify({"error": "Not found"}), 404


@employee_bp.route("/employees/new", methods=["GET"])
def show_form():
    return render_template("form.html", employees=employees)

# PROSES FORM  ->  POST /employees/new
@employee_bp.route("/employees/new", methods=["POST"])
def submit_form():
    name = request.form.get("name")          # <- beda dari request.get_json()
    position = request.form.get("position", "Staff")
    salary = request.form.get("salary", 0)

    if not name:
        return "Nama wajib diisi!", 400

    new_id = max([e["id"] for e in employees], default=0) + 1
    new = {
        "id": new_id,
        "name": name,
        "position": position,
        "salary": int(salary) if salary else 0,
    }
    employees.append(new)

    return redirect("/employees/new")   # <- reload halaman, tampilkan list terbaru
