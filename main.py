from datetime import datetime
from flask import Flask, render_template, request, session, url_for, redirect
from flask_mail import Mail, Message
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'hello'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'portfolio'

db = MySQL(app)

app.config.update(
            MAIL_SERVER = 'smtp.gmail.com',
            MAIL_PORT = 465,
            MAIL_USE_TLS = False,
            MAIL_USE_SSL = True,
            MAIL_USERNAME = 'dsouzareuben79@student.sfit.ac.in',
            MAIL_PASSWORD = '#Reuben123'
        )
mail = Mail(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        cur = db.connection.cursor()
        cur.execute("INSERT INTO contacts (name, phone, msg, date, email) VALUES (%s, %s, %s, %s, %s)",
                    (name, phone, message, datetime.now(), email))
        db.connection.commit()
        cur.close()

        msg = Message(
            subject='Welcome Message',
            sender='dsouzareuben79@student.sfit.ac.in',
            recipients=[email],
            body='hi hello'
        )
        mail.send(msg)
        print('Email Sent!')

    return render_template("contact.html")


@app.route("/admin", methods=['GET', 'POST'])
def admin_page():
    cur = db.connection.cursor()

    if 'user' in session and session['user'] == 'Reuben':
        # Fetch projects using raw MySQL query
        cur.execute("SELECT * FROM projects")
        projects = cur.fetchall()
        cur.close()
        return render_template('admin.html', projects=projects)

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')

        session['user'] = username
        cur.execute("SELECT * FROM projects")
        projects = cur.fetchall()
        cur.close()
        return render_template('admin.html', projects=projects)

    cur.close()
    return render_template('login.html')


@app.route("/projects")
def projects_page():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    for project in projects:
        print(project[3])
    return render_template("projects.html", projects=projects)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit_page(sno):
    print(sno)
    if "user" in session and session['user'] == 'Reuben':
        cur = db.connection.cursor()

        if request.method == "POST":
            req_title = request.form.get('title')
            description = request.form.get('description')
            link = request.form.get('link')
            image = request.form.get('image')
            date = datetime.now()

            if sno == '0':
                cur.execute("INSERT INTO projects (title, description, link, img_file, date) "
                            "VALUES (%s, %s, %s, %s, %s)", (req_title, description, link, image, date))
                db.connection.commit()
                return redirect("admin.html")
            else:
                cur.execute("""
                    UPDATE projects
                    SET title=%s, description=%s, link=%s, img_file=%s, date=%s
                    WHERE sno=%s
                """, (req_title, description, link, image, date, sno))
                db.connection.commit()
                return redirect('/edit/' + sno)

        cur.execute("SELECT * FROM projects WHERE sno = %s", (sno,))
        project = cur.fetchone()
        cur.close()

        return render_template('edit.html', project=project, sno=sno)

    return render_template('login.html')


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete_page(sno):
        if "user" in session and session['user'] == 'Reuben':
            cur = db.connection.cursor()

            cur.execute("DELETE FROM projects WHERE sno = %s", (sno,))
            db.connection.commit()
            cur.close()

        return redirect(url_for("admin_page"))


@app.route("/logout")
def logout():
    session.pop('user')
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
