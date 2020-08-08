from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_mysqldb import MySQL

import  requests
import pyodbc
import json

#SQL Server Connection
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=ADMIN-PC;"
    "Database=knowledge;"
    "Trusted_Connection=yes;"
)


app = Flask(__name__)
'''app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'knowledge'
mysql = MySQL(app)'''

# settings
app.secret_key = 'mysecretkey'


@app.route('/')
def home():

    url = 'http://httpbin.org/get'
    args = { 'nombre':'eduardo', 'curso':'python', 'nivel':'intermedio'}
    response = requests.get(url, params=args)
    response_json = json.loads(response.text)
    origin = response_json['origin']
    return render_template('home.html', origen = origin)

@app.route('/dashboard')
def dashboard():
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('dashboard.html', contacts = data)
    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = conn.cursor() #cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (?, ?, ?)', (fullname, phone, email)) #cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        conn.commit() #mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('home'))

@app.route('/edit/<id>')
def get_contact(id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = ?', (id))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']   
        cur = conn.cursor()
        cur.execute("""
        UPDATE contacts
        SET fullname = ?,
            phone = ?,
            email = ?
        WHERE id = ?
        """, (fullname,phone,email,id))
        flash('Contact Updated Successfully')
        return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = conn.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    conn.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(debug=True)
    '''ctx_auth = AuthenticationContext(url=settings['url'])
    if ctx_auth.acquire_token_for_app(client_id=settings['client_credentials']['client_id'],
                                      client_secret=settings['client_credentials']['client_secret']):
        ctx = ClientContext(settings['url'], ctx_auth)
        read_folder_and_files(ctx, "Documents")
        # read_folder_and_files_alt(ctx, "Documents")
        # upload_file_into_library(target_library, name, content)
        # download_file(ctx)
    else:
        print(ctx_auth.get_last_error())
'''
