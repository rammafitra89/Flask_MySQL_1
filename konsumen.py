from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'konsumen'

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		details = request.form 
		Nama = details['name']
		Alamat = details['address']
		cur = mysql.connection.cursor()
		cur.execute ("INSERT INTO profile (nama, alamat) VALUES (%s, %s)", (Nama, Alamat))
		mysql.connection.commit()
		cur.close()
		return 'sukses'
	return render_template('index.html')		
if __name__ == '__main__':
	app.run()	