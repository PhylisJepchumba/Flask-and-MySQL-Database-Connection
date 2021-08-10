from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'phyliskorir'
app.config['MYSQL_DB'] = 'Contact'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        Name = details['fname']
        Email = details['email']
        Message = details['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO data(Name, Email,Message) VALUES (%s, %s, %s)", (Name, Email,Message))
        mysql.connection.commit()
        cur.close()
        return render_template('sucess.html')

      
    else :return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)