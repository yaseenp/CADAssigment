from flask import Flask, render_template, request, session 
import ibm_db 
import ibm_boto3 from ibm_botocore.client 
import Config, ClientError 
import os 
import re 
import random 
import string 
import datetime 
import requests


from flask import Flask, render_template, request,session

app = Flask(__name__)


if __name__ =='__main__':
    app.run( debug = True,host="0.0.0.0")


#Rendering Index.Html Page

@app.route("/")
def index():
	return render_template("index.html")


#Rendering Contact.Html Page

@app. route("/contact")
def contact():
	return render_template("contact.html")

#3.6

#Rendering Login.Html Page 

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mwv02817;PWD=BGu2G7vYyF7JGCrq",'','')
#conn = ibm_db.conect("DATABASE=bludb;HOSTNAME=« Enter Your Host Name› ; PORT<Port Number>; UID=<Enter Your Username›;

#PASSWORD=<Enter Your Password>; SECURITY=SSL;


#SLServercertificate = DigicertlobalRootCA. crt", '', '')


@app.route("/login", methods=['POST', 'GET'])
def loginentered():
    global Userid
    global username
	msg = ''
    if request.method == "PoST":
            email = str(request. form['email'])
            print(email)
            password = request. form['password']
            sql="SELECT * FROM REGISTER WHERE EMAIL=? AND PASSWORD=?" # from dbz sql table
	        stmt=ibm_db.prepare(conn,sql)

            ibm_db.bind_param(stmt, 1, email) 
	        ibm_db.bind_param(stmt, 2, password)
            ibm_db.execute(stmt) 
            account=ibm_db. fetch_assoc (stmt)
	        print(account)
	        if account:
		        session['Loggedin'] = True
                session['id'] = account ['EMAIL']
                Userid = account['EMAIL']
                session['email'] = account['EMAIL']
                Username = account ["USERNAME"]
                Name= account['NAME']
                msg="logged in sucessfully !"
                sql="SELECT ROLE FROM register where email =?"

                 stmt= ibm_db.prepare(conn, sql)
                 ibm_db.bind_param(stmt, 1, email)
                 ibm_db.execute(stmt)
                 r=  ibm_db. fetch_assoc(stmt)
                 print(r)
                if r['ROLE'] == 1:
	                 print("STUDENT")
                     return render_template("studentprofile.html", msg=msg, user=email, name=Name, role="STUDENT",username=Username, email = email)
                 elif r['ROLE'] == 2:
                       print("FACULTY")
                     return render_template("facultyprofile.html", msg=msg, user=email, name =Name, role="FACULTY", username=Username, email = email)
                 else:
                    return render_template('adminprofile.html', msg=msg, user=email, name = Name, role= "ADMIN", username=Username, email = email)
                 else:
                    msg="in correct email/password"
                    return render_template ("login.html", msg=msg)
                 else:
                    return render_template("login.html")

#based on those details we will validate the login. If the details are correct. According to the role, it will redirect them to their respective pages.
#The login email and username of the user we will track by using the session object of flask to track user activities.

#3.7

#Rendering Adminprofile.Html

@app.route("/adminprofile")
def aprofile():
	return render_template("adminprofile.html")


#3.8
#Rendering The Adminregister.Html

@app. route("/register", methods=['POST', 'GET'])
def signup():
msg =''
if request.method == "POST':
name = request. form["sname"]
email = request. form[ "semail"]
username = request. form[" susername"]
role =int (request. form 'role '])
password = ' join(random.choice (string.ascii_letters) for i in range (0,8))
link = https://university.ac.in/portal'
sql = "SELECT* FROM register WHERE email= ?"
stmt = ibm_db.prepare(conn, sql)
ibm_db.bind_param(stmt, 1, email)
ibm_db. execute (stmt)
account = ibm_db.fetch_assoc (stmt)
msg = "Already Registered"
return render_template('adminregister.html', error=True, msg=msg)
elif not re.match(r'[^@]+@[^@]+/.[^@]+',email):
msg = "Invalid Email Address!"
insert_sal = "INSERT INTO register VALUES (?,?,?,?,?)"
prep_stmt = ibm_db.prepare(conn, insert_sql)
# this username & password is should be same as db-2 details & order also
ibm_db.bind_param(prep_stmt, 1, name)
ibm_db.bind_param(prep_stmt, 2, email)
ibm_db.bind_param(prep_stmt, 3, username)
ibm_db.bind_param(prep_stmt, 5, role)
ibm_db. bind_param(prep_stmt, 4, password) 
ibm_db. execute(prep_stmt)

payload ={ " personalizations": ["to": [l"email": email}],"subject": "Student Account Details""from": {"email": "yaseenpasham@svit.ac.in"),
"content": ["type": "text/plain",In welcome to University,Here the he details l locome to youressuent portal link : in
YOUR Username: {) \n PASSWORD : ()
In Thank you In Sincerely\n
Office of Admissions\n Swami Vivekananda Institute of Technology In E-Mail: admission@university.ac.in ; Website: www.university.ac.in"**
•format( name, link, username, password)

headers = {
"content-type": "application/json",
"X-RapidAPI-Key": "‹Enter your Rapid api - api key>",
"X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com


response = requests. request ("POST", url, json=payload, headers=headers)
print (response. text)
msg = "Registration Successful"
return render_template(adminregister.html', msg-msg)

SendGrid Email service - Rapid API link: https://rapidapi.com/sendgrid/api/sendgrid
Q Rapid ApI
senderic wl
3.010
250ms
TOU %0
＜ POS13000
• Nail soninese to ts they points section lick on the Mail dropdown to se the list of : Combul cal he atopin wine to Node A sins. Click on it and from the
dropdown select the python. In that select requests
Now copy the code and paste it in the flask code. (which you see in the above screenshots).
Note: You need to customise the content section in the copy code after pasting, according to how you want your mail to be.
3.9

//Rendering Studentprofile.Html

@app route("/studentprofile")

def sprofile():

	return render_template("studentprofile.html")