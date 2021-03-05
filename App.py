from flask import Flask, render_template,  request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost" 

app.config['MYSQL_USER'] = "root"

app.config['MYSQL_PASSWORD'] = ""

app.config['MYSQL_DB'] = "examen"

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addcontact', methods = ['POST'])
def addContact():
    if request.method == "POST":
        connectionMysql = mysql.connection.cursor()
        
        form = request.form
        connectionMysql.execute('INSERT INTO contacts (id,name,last_name,phone_code,phone,email,status,address,marital) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)',
        (form["name"],form["last_name"],form["phone_code"],form["phone"],form["email"],form["status"],form["address"],form["marital"]))
        mysql.connection.commit()

        return "ok"


@app.route('/deletecontact')
def deletecontact():
    return("delete contact")


if __name__ == '__main__':
    app.run(port = 3000,debug = True)
