from datetime import datetime
from flask  import Flask, jsonify, redirect, render_template, request, url_for
import psycopg2


app=Flask(__name__,template_folder='templates')

app.config['DATABASE'] = {
    'dbname': 'divum',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def get_db_connection():
    return psycopg2.connect(
        dbname=app.config['DATABASE']['dbname'],
        user=app.config['DATABASE']['user'],
        password=app.config['DATABASE']['password'],
        host=app.config['DATABASE']['host'],
        port=app.config['DATABASE']['port']
    )
@app.route('/submit',methods=['POST'])
def submit():
    if request.method=='POST':
        email=request.form.get('email')
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        mob=request.form.get('mobile')
        email=request.form.get('email')
        dob=request.form.get('dob')
        address=request.form.get('address')
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT email FROM form WHERE email = %s', (email,))
    
    
        cursor.execute('INSERT INTO form VALUES (%s, %s, %s, %s, %s, %s)', (email, fname, lname, mob, dob, address))
       
        connection.commit()
        cursor.close()
        connection.close()
        
        return redirect(url_for('index'))

@app.route('/delete/<email>',methods=['GET'])
def delete(email):
    if request.method=='GET':
       connection = get_db_connection()
       cursor = connection.cursor()
       
       cursor.execute('DELETE FROM form WHERE email=%s',(email,))
       connection.commit()
       connection.close()
       
       return redirect(url_for('index')) 
   
@app.route('/edit/<email>')
def edit(email):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM form WHERE email=%s', (email,))
    data = cursor.fetchone()  
    connection.close()

    return render_template('editpage.html', data=data)

@app.route('/check', methods=['POST'])
def check():
    email = request.form.get('email')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT email FROM form WHERE email=%s', (email,))
    data = cursor.fetchone()
    connection.close()

    response = {'exists': data is not None}

    return jsonify(response)

@app.route('/checkedit', methods=['POST'])
def checkedit():
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT email FROM form WHERE email=%s AND mobile<>%s', (email,mobile,))
    data = cursor.fetchone()
    connection.close()

    response = {'exists': data is not None}

    return jsonify(response)

@app.route('/checkmob', methods=['POST'])
def checkmob():
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT mobile FROM form WHERE mobile=%s AND email<>%s', (mobile,email,))
    data = cursor.fetchone()
    connection.close()

    response = {'exists': data is not None}

    return jsonify(response)

@app.route('/update/<email>', methods=['POST'])
def update(email):
    if request.method == 'POST':
        updated_email = request.form.get('email')
        updated_fname = request.form.get('fname')
        updated_lname = request.form.get('lname')
        updated_mob = request.form.get('mobile')
        updated_dob = request.form.get('dob')
        updated_address = request.form.get('address')
        updated_created =  datetime.now()
        

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            'UPDATE form SET email=%s, first_name=%s, last_name=%s, mobile=%s, dob=%s, address=%s, created_at=%s WHERE email=%s',
            (updated_email, updated_fname, updated_lname, updated_mob, updated_dob, updated_address, updated_created, email,)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('index'))

    
   
@app.route('/add_button')
def add_button():
    return render_template('addpage.html')
   
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM form order by created_at desc')
    data = cursor.fetchall()
    connection.close()
    formatted_data = [(row[0], row[1], row[2], row[3], row[4].strftime("%d-%m-%Y")) for row in data]

    return render_template('index.html', data=formatted_data)
    

if __name__=='__main__':
    app.run(debug=True)