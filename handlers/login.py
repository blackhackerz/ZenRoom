from zenroom.forms import Login
from zenroom import app, bcrypt
from flask import render_template, redirect, url_for, flash, request, session
import pymongo

client = pymongo.MongoClient('mongodb+srv://ypratik817:zzWzxZAcDT1efuMx@cluster0.7tltv8e.mongodb.net/')
db = client['zenroom']
col = db["users"]       



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        print(form.email.data)
        try:
            res = col.find({"email": form.email.data})
            print(res[0])
            # session['user_id'] = res[0]["user_id"]
        except:
            flash('Incorrect Email/Password', "error")
            print(res)
            # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            # print(hashed_password, bcrypt.check_password_hash("$2b$12$gbVs1yn4KeOxk2vkwXiYFuLCsrE/pHdlOK3Z3EDRGXMLnb.cT1P1W", form.password.data))
            
            password = form.password.data
            
            # print(res)
            # return redirect(url_for('login'))
        if bcrypt.check_password_hash(password.decode('utf-8'), res[0]["password"]):
               return res[0]['password']
     

       
    return render_template('login.html', form= form)


