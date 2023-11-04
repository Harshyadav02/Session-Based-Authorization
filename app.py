from flask import Flask , render_template , request, session
from utils import requires_role
app = Flask(__name__)
app.secret_key="qqoiuytr96852^&()*()_*()_"

#  Database for the Admin holding username and password
Admin = [
   {'Admin':'Harsh' , 'Password' :  'harsh'},
   {'Admin':'Anil'  , 'Password' :  'Anil'},
   {'Admin':'Lokesh', 'Password' :  'Lokesh'}
]
#  Database for the Pateint holding username and password

Patient = [

   {'Patient':'Tony' , 'Password' :  'Stark'},
   {'Patient':'Loki'  , 'Password' :  'Odin-putra'},
   {'Patient':'Tichalla', 'Password' :  'Wakanda'}
]

#  Database for the Doctor holding username and password

Doctor = [

   {'Doctor':'Captain' , 'Password' :  'America'},
   {'Doctor':'Black'  , 'Password' :  'widow'},
   {'Doctor':'spyder', 'Password' :  'man'}
]

@app.route('/')
def index():
   return render_template('index.html')
 

#  Admin route for login
@app.route('/Admin-login/' , methods=('POST','GET'))
def Admin_login():

   if request.method == 'POST':

      username = request.form.get('username')
      password = request.form.get('password')

      for admin in Admin:
         if admin['Admin'] == username:
            if admin['Password'] == password:
               session['role'] = 'Admin'
               print(session)   
               return render_template('pages.html')
            else:
               return "Not a valid password" 
         else:
            "Not a valid username"
   return render_template('admin-login.html')

#  Patient route for login
@app.route('/Patient-login/', methods=('POST','GET'))
def Patient_login():

   if request.method == 'POST':

      username = request.form.get('username')
      password = request.form.get('password')

      for patient in Patient:
         if patient['Patient'] == username:
            if patient['Password'] == password:
               session['role'] = 'Patient'
               print(session)   
               return render_template('pages.html')
            else:
               return "Not a valid password" 
         else:
            "Not a valid username"
   return render_template('patient-login.html')
@app.route('/Doctor-login/', methods=('POST','GET'))

# Doctor route for login
def Doctor_login():

   if request.method == 'POST':

      username = request.form.get('username')
      password = request.form.get('password')

      for doctor in Doctor:
         if doctor['Doctor'] == username:
            if doctor['Password'] == password:
               session['role'] = 'Doctor'  
               print(session) 
               return render_template('pages.html')
            else:
               return "Not a valid password" 
         else:
            "Not a valid username"
   return render_template('doctor-login.html')

#  For logout
@app.route('/logout/')
def logout():
   session.pop('role')
   
   print(session)
   return render_template('index.html')



@app.route('/page1')
@requires_role(['Admin', 'Doctor'])
def page1():
   return '<h1>Welcome authorized user</h1>'

@app.route('/page2')
@requires_role(['Admin', 'Patient'])
def page2():
   return '<h1>Welcome authorized user</h1>'
@app.route('/page3')
@requires_role(['Patient', 'Doctor'])
def page3():
   return '<h1>Welcome authorized user</h1>'



app.run(host='0.0.0.0', port=5000, debug=True)
