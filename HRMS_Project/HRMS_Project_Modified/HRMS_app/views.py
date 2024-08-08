from flask import render_template, request, redirect, url_for, flash, session
from HRMS_app.models import Employee, db, User
from HRMS_app import app
from functools import wraps


# Decorator Function
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get('logged_in'):
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrap

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        usrname = request.form['username']
        passwrd = request.form['password']
        data = User.query.filter_by(username=usrname, password=passwrd).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('Index'))
        return render_template('login.html', message="Incorrect Details")

#query on all our employee data
@app.route('/')
def Index():
    all_employee_data = Employee.query.all()
    return render_template("index.html", employees=all_employee_data)


# insert data to the database via html forms
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        education = request.form['education']
        experience = request.form['experience']

        employee_data = Employee(name, email, phone, address, education, experience)
        db.session.add(employee_data)
        db.session.commit()

        flash("Employee Inserted Successfully")
        return redirect(url_for('Index'))


# update employee table
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        employee_data = Employee.query.get(request.form.get('id'))

        employee_data.name = request.form['name']
        employee_data.email = request.form['email']
        employee_data.phone = request.form['phone']
        employee_data.address = request.form['address']
        employee_data.education = request.form['education']
        employee_data.experience = request.form['experience']

        db.session.commit()
        flash("Employee Updated Successfully")
        return redirect(url_for('Index'))


# delete data from employee table by id
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    employee_data = Employee.query.get(id)
    db.session.delete(employee_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('Index'))

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

