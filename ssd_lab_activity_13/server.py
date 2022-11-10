

from flask import Flask, redirect, url_for, request, render_template,flash
import sqlite3
app = Flask(_name_)

@app.route('/')
def Home():
    return "aayiye aapka intazaar tha!!"

@app.route('/user/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        try:
            inp=request.get_json()
            mailId=inp["email"]
            pwd=inp["password"]
            print(mailId,pwd)
            if ((mailId is None or (not mailId)) or (pwd is None or (not pwd))):
                return {"errorMessage": "invalid credentials"}
            else:
                conn=sqlite3.connect('database.db')
                conn.execute("insert into user values(?,?)",(mailId, pwd))
                conn.commit()
                flash("Record Added  Successfully","success")
                conn.close()
                return {"ResponseMessage":"Signed in successfully"}
        except Exception as e:
            print(e)
            return {"errorMessage":"invalid request" }


@app.route('/user/login', methods=['POST'])
def login():
    try:
        inp = request.get_json()
        mailId=inp["email"]
        pwd=inp["password"]
        if (mailId is None or not mailId or pwd is None or not pwd):
            return {"errorMessage":"invalid credentials"}
        else:
            conn = sqlite3.connect('database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM user WHERE email=? and password=?",(mailId,pwd))
            data=c.fetchone()
            print(data)
            if len(data)==0:
                return {"ResponseMessage":"User not found"}
            else:
                conn.close()
                return {"ResponseMessage":"login successfull"}
    except Exception as e:
        print(e)
        return {"errorMessage":"invalid request"}


@app.route('/user/signout', methods=['Get'])
def logout():
    try:
        return {"ResponseMessage":"Logout successfull"}

    except Exception as e:
        return {"errorMessage": "invalid request"}


@app.route('/seats/available', methods=['Get'])
def available():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("select * from seats where bookingType=''")
        rows = c.fetchall()
        print(rows)
        if len(rows)==0:
            return {"ResponseMessage":"No seats available"}
        else:
            return {"ResponseMessage":"Logout successfull"}

    except Exception as e:
        return {"errorMessage": "check request"}
    finally:
        conn.close()

@app.route('/seats/book', methods=['Post'])
def Book():
    try:
        inp=request.get_json()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("select * from seats where bookingType=''")
        rows = c.fetchall()
        print(rows)
        if len(rows)==0:
            return {"ResponseMessage": "No seats available"}
        else:
            return {"ResponseMessage": "Logout successfull"}

    except Exception as e:
        return {"errorMessage": "check request"}
    finally:
        conn.close()



# main driver function
if _name_ == '_main_':
    # run() method of Flask class runs the application
    # on the local development server.
    # app = Flask(_name_, template_folder='tem
    app.run()