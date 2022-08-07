import numbers
import sqlite3
from unittest import result
from flask import Flask, render_template, request 

def getConn():
    conn = sqlite3.connect('./db/work.db')
    return conn
app = Flask(__name__)

@app.route("/")
def home ():
    return render_template('home.html')

@app.route("/Home", methods=['get', 'post'])
def Home ():
    return render_template('home.html')

@app.route("/addRecord", methods=['post'])
def addRecord():
    company = request.form["company"]
    email = request.form["email"]
    number = request.form["number"]
    address = request.form["address"]
    dbConn = getConn()
    sql = "INSERT INTO company (company, email, address, number) VALUES ('" +company+ "','" + email+ "','"+number +"','" + address+ "')"
    csr = dbConn.cursor()
    csr.execute(sql)
    dbConn.commit()
    print(csr.lastrowid)
    return render_template('response.html', msg="Successfully added company")

@app.route("/results", methods=['get', 'post'])
def results():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    companyList = dbConn.execute('SELECT * from company')
    return render_template('results.html', companyList=companyList)

@app.route("/delete", methods=['get', 'post'])
def delete():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    companyList = dbConn.execute('SELECT * from company')
    return render_template('delete.html', companyList=companyList)

@app.route("/deleteRecord", methods=["get", "post"])
def deleteRecord():
    id = request.form["data"]
    dbConn = getConn()
    sql = "DELETE FROM company WHERE Id ='" + id + "'" 
    csr = dbConn.cursor()
    csr.execute(sql)
    dbConn.commit()
    return render_template('response.html', msg="Successfully deleted Company Record")

@app.route("/qualify", methods=["get", "post"])
def qualify():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    companyList = dbConn.execute('SELECT * FROM student WHERE student.grade > 85')
    return render_template('results.html', companyList=companyList)

@app.route("/update", methods=['get', 'post'])
def update():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    companyList = dbConn.execute('SELECT * from company')
    return render_template('update.html', companyList=companyList)

@app.route("/updateRecord", methods=['get', 'post'])
def updateRecord():
    company = request.form["company"]
    email = request.form["email"]
    number = request.form['number']
    address = request.form['address']
    id = request.form["id"]
    dbConn = getConn()
    sql = "UPDATE company SET company = '" + company + "', email='"+ email + "', number='"+ number +"', address='"+ address+"' where Id='"+id +"'" 
    csr = dbConn.cursor()
    csr.execute(sql)
    dbConn.commit()
    return render_template('response.html', msg="Successfully Updated the Record")



if __name__ == '__main__':
    app.run()

