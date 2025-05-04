from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Route for the landing page (home page)
@app.route('/')
def home():
    return render_template('home_page.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Basic login check
        if username == 'admin' and password == 'admin':
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid Credentials')
    return render_template('login.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ID Card Management home
@app.route('/id-card-management')
def id_card_management():
    return render_template('id_card_management.html')

# Add Student page
@app.route('/add-student')
def add_student():
    return render_template('add_student.html')

# Modify Student page
@app.route('/modify-student')
def modify_student():
    return "Modify Student Page (Coming Soon)"

# Show Students page
@app.route('/show-students')
def show_students():
    return "Show Students Page (Coming Soon)"

# School Management
@app.route('/school-management')
def school_management():
    return "School Management Page (Coming Soon)"

# Other Services
@app.route('/other-services')
def other_services():
    return "Other Services Page (Coming Soon)"

if __name__ == '__main__':
    app.run(debug=True)
