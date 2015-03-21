import mysql.connector
import random
import sqlite3

from flask import Flask, render_template, request, session, flash, escape, redirect, url_for

app = Flask(__name__)
#DEF##################################################################################################################################################################
def getpoints(username):
	cnx = mysql.connector.connect(user='root', database='4sreviews')
	cursor = cnx.cursor()
	query = ("""SELECT username,password,points FROM gameuser WHERE username = '%s'"""%username)
	cursor.execute(query)
	for each in cursor:
	   	points = each[2]
	return points

def givepoints(username, points, value):
	cnx = mysql.connector.connect(user='root', database='4sreviews')
	cursor = cnx.cursor()
	newpoints = points + value
	password = getpassword(username)
	
	query = (""" REPLACE INTO gameuser(username, `password`, `points`) VALUES ('%s','%s','%d') """ %(username, password, newpoints))
	cursor.execute(query)
	cnx.commit()
	cursor.close()
	return newpoints

def getusername():
	if 'username' in session:
		username = str(escape(session['username']))
	return username

def getpassword(username):
	cnx = mysql.connector.connect(user='root', database='4sreviews')
	cursor = cnx.cursor()
	query = ("""SELECT username,password,points FROM gameuser WHERE username = '%s'"""%username)
	cursor.execute(query)
	l = []
	for each in cursor:
	   	l.append(each[0])
	if username in l:
		password = each[1]
	return password

def indatabase():
	a,user_id = hello_world()
	user_id = int(user_id)

	cnx = mysql.connector.connect(user='root', database='4sreviews')
	cursor = cnx.cursor()

	query1 = (" SELECT * FROM origin " " WHERE user_id = %d "%user_id)
	cursor.execute(query1)
	for each in cursor:
		s1 = each[1]
		s2 = each[2]
		s3 = each[3]
		s4 = each[4]
		s5 = each[5]
		s6 = each[6]
		s7 = each[7]
		s8 = each[8]
		s9 = each[9]
		s10 = each[10]
		s11 = each[11]
		s12 = each[12]
		s13 = each[13]
		s14 = each[14]
		s15 = each[15]
		s16 = each[16]
		s17 = each[17]
		s18 = each[18]
		print 'in here!'
		cursor.close()
		return s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18
	
	print 'lets add'
	s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 =s15 =s16 = s17 = s18 = 0
	return s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18

def todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18):
	a,user_id = hello_world()
	user_id = int(user_id)
	cnx = mysql.connector.connect(user='root', database='4sreviews')
	cursor = cnx.cursor()

	query1 = (""" REPLACE INTO origin(user_id, `North America`, `Mexico`, `South America`, `North Africa`, `South Africa`, `North Europe`, `South Europe`, `East Europe`, `England`, `Indonesia`, `Australia + New Zealand`, `West Asia`, `Middle East`, `India/Pakistan`, `Southeast Asia`, `China`, `Japan`, `No Idea!`) VALUES ('%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d') """ %(user_id,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18))
	cursor.execute(query1)
	cnx.commit()
	cursor.close() 

	print 'ADDED'
	givepoints(getusername(), getpoints(getusername()), 1)
	print 'add points'
	return redirect('/index')

############################################################################################################################################################################
@app.route('/')                              #Welcome page, link to game. Options: login? --> hold scores
def show_front():
	return render_template('front.html')


@app.route('/index')                         #Retrieve photo + name (first + last)
def hello_world():
    if not session.get('username'):
        abort(401)
    username = getusername()
    points = getpoints(username)
    cnx = mysql.connector.connect(user='root', database='4sreviews')
    cursor = cnx.cursor()

    query = ("SELECT * FROM users " "ORDER BY RAND() LIMIT 1")  
    cursor.execute(query)

    for each in cursor:
        user_id =   each[0]
        name =      each[1]
        gender =    each[2]
        photo1 =    each[3].replace('{"prefix":"','')
        photo2 =    photo1.replace('","suffix":"', '256x256')
        photo =     photo2.replace('"}', '')
        lastname = 	each[4]
        homecity = 	each[5]

    if lastname == None:
    	lastname = ""

    #need exception when photo not there
    
    cursor.close()    
    return render_template('index.html', name=name, photo=photo, username= username, points= points, lastname=lastname, homecity=homecity), user_id

###########MAP LINKS######################################################################################################################################################################3
@app.route('/NA')
def NA():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s1 = s1 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)


@app.route('/mexico')
def mexico():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s2 = s2 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/southamerica')
def southamerica():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s3 = s3 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/northafrica')
def northafrica():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s4 = s4 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/southafrica')
def southafrica():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s5 = s5 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/northeurope')
def northeurope():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s6 = s6 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/southeurope')
def southeurope():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s7 = s7 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/easteurope')
def easteurope():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s8 = s8 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/england')
def england():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s9 = s9 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/indonesia')
def indonesia():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s10 = s10 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/australia')
def australia():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s11 = s11 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/westasia')
def westasia():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s12 = s12 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/middleeast')
def middleeast():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s13 = s13 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/indiapakistan')
def indiapakistan():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s14 = s14 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/southeastasia')
def southeastasia():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s15 = s15 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/china')
def china():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s16 = s16 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/japan')
def japan():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s17 = s17 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)

@app.route('/noidea')
def noidea():
	s = indatabase()
	s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = s
	s18 = s18 + 1
	return todb(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18)



#LOGIN/REGISTER######################################################################################################################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    cnx = mysql.connector.connect(user='root', database='4sreviews')
    cursor = cnx.cursor(buffered=True)
    if request.method == 'POST':
    		username = request.form['username']
    		password = request.form['password']
    		query = ("SELECT username,password,points FROM gameuser")  
    		cursor.execute(query)
    		l = []
    		for each in cursor:
    			l.append((each[0],each[1]))
    		print l
    		if (username,password) in l:
    			session['username'] = username
    			return hello_world()
    return show_front() + "Not registered yet?" + render_template('register.html')

@app.route('/logout')
def logout():
    return render_template('front.html') 

@app.route('/register', methods=['GET', 'POST'])   ## register in the database, checks double usernames, 2 times password must be same
def register():
	cnx = mysql.connector.connect(user='root', database='4sreviews')
	cursor = cnx.cursor(buffered=True)
	if request.method == 'POST':
    		username = request.form['username']
    		password = request.form['password']
    		password1 = request.form['password1']
    		query = ("SELECT username FROM gameuser")  
    		cursor.execute(query)
    		l = []
    		for each in cursor:
    			l.append(each[0])
    		if username in l:
    			return show_front() + render_template('register.html') + "This username is already taken!"
    		elif password == password1 and len(password) > 0:
    			query1 = (""" INSERT INTO gameuser(`username`, `password`, points) VALUES ('%s','%s',0) """%(username,password))
    			cursor.execute(query1)
    			cnx.commit()
    			return show_front() + "You can login now :)"
    		else: 
    			return show_front() + render_template('register.html') + "Passwords do not match!, Try again!"

###################################################################################################################################################################################################
@app.route('/highscores')
def highscores():
	cnx = mysql.connector.connect(user='root', database='4sreviews')
	cursor = cnx.cursor()
	query = ("""SELECT username, points FROM gameuser ORDER BY points DESC LIMIT 10 """)
	cursor.execute(query)
	l = []
	for each in cursor:
	   	l.append((each[0],each[1]))
	username1,points1 = l[0]
	username2,points2 = l[1]
	try:
		username3,points3 = l[2]
	except: 
		username3,points3 = 0,0
	return render_template('highscores.html', username1=username1, username2=username2, username3=username3, points1=points1, points2=points2, points3=points3)

#####################################################################################################################################################################################################
if __name__ == '__main__':
    app.secret_key = 'eysgCIdwfbsif23h5246&^&#$jhr'
    app.run(debug=True)
    