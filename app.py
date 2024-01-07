from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from USER"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ",  dictionary["CONTACT"])
        print("The Adress is : ",  dictionary["ADDRESS"])
        print("The Role is : ",  dictionary["ROLE"])
        print("The Branch is : ",  dictionary["BRANCH"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from USER where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ", dictionary["CONTACT"])
        print("The Address is : ", dictionary["ADDRESS"])
        print("The Role is : ", dictionary["ROLE"])
        print("The Branch is : ", dictionary["BRANCH"])
        print("The Password is : ", dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,email,contact,address,role,branch,password):
    sql= "INSERT into USER VALUES('{}','{}','{}','{}','{}','{}','{}')".format(name,email,contact,address,role,branch,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mwv02817;PWD=OgCJRNGF3YrIpX8k",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('adminRegister.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['mobile']
        address = request.form['address']
        role = request.form['role']
        if role =="0":
            role = "Faculty"
        else:
            role = "Student"
        branch = request.form['branch']
        password = request.form['pwd']
        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,name,email,contact,address,role,branch,password)
        return render_template('login.html')
        

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pwd']
        sql= "select * from USER where email='{}' and password='{}'".format(email,password)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["EMAIL"]
            return render_template('userprofile.html',name=userdetails["NAME"],email= userdetails["EMAIL"],contact= userdetails["CONTACT"],address=userdetails["ADDRESS"],role=userdetails["ROLE"],branch=userdetails["BRANCH"])
        else:
            msg = "Incorrect Email id or Password"
            return render_template("login.html", msg=msg)
    return render_template('login.html')


if __name__ =='__main__':
    app.run( debug = True)
                  
