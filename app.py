from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_DB"] = "py_db"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "SELECT * FROM users"
    con.execute(sql)
    res = con.fetchall()
    return render_template("index.html", datas=res)

# New User Creation
@app.route('/addusers', methods=['GET', 'POST'])
def addusers():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        sys_username = request.form['sys_username']
        sys_ip = request.form['sys_ip']
        sys_password = request.form['sys_password']

        
        con = mysql.connection.cursor()
        sql = "INSERT INTO users (name, email, sys_username, sys_ip, sys_password) VALUES (%s, %s, %s, %s, %s)"
        val = (name, email, sys_username, sys_ip, sys_password)
        con.execute(sql, val)
        mysql.connection.commit()
        
        return redirect(url_for('home'))  # Redirect to home page after adding user
    
    return render_template("addusers.html")

if __name__ == "__main__":
    app.run(debug=True)
