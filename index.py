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

@app.route("/studentReg", methods=['post'])
def studentReg():
    studentName = request.form["name"]
    studentGrade = request.form["grade"]
    dbConn = getConn()
    sql = "INSERT INTO student (name, grade) VALUES ('" + studentName + "','" + studentGrade + "')"
    csr = dbConn.cursor()
    csr.execute(sql)
    dbConn.commit()
    print(csr.lastrowid)
    return render_template('response.html', msg="Successfully added Student")

@app.route("/results", methods=['get', 'post'])
def results():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    studentList = dbConn.execute('SELECT * from student')
    return render_template('results.html', studentList=studentList)

@app.route("/delete", methods=['get', 'post'])
def delete():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    studentList = dbConn.execute('SELECT * from student')
    return render_template('delete.html', studentList=studentList)

@app.route("/deleteRecord", methods=["get", "post"])
def deleteRecord():
    id = request.form["data"]
    dbConn = getConn()
    sql = "DELETE FROM student WHERE Id ='" + id + "'" 
    print(sql)  
    csr = dbConn.cursor()
    csr.execute(sql)
    dbConn.commit()
    return render_template('response.html', msg="Successfully deleted Student Record")

@app.route("/qualify", methods=["get", "post"])
def qualify():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    studentList = dbConn.execute('SELECT * FROM student WHERE student.grade > 85')
    return render_template('results.html', studentList=studentList)

@app.route("/update", methods=['get', 'post'])
def update():
    dbConn = getConn()
    dbConn.row_factory = sqlite3.Row
    studentList = dbConn.execute('SELECT * from student')
    return render_template('update.html', studentList=studentList)

@app.route("/updateRecord", methods=['get', 'post'])
def updateRecord():
    studentName = request.form["name"]
    studentGrade = request.form["grade"]
    id = request.form["id"]
    dbConn = getConn()
    sql = "UPDATE student SET name = '" + studentName + "', grade='"+ studentGrade + "' where Id='"+id +"'" 
    print(sql)  
    csr = dbConn.cursor()
    csr.execute(sql)
    dbConn.commit()
    return render_template('response.html', msg="Successfully Updated the Record")



if __name__ == '__main__':
    app.run()

