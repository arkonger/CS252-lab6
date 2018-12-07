import os
import sys
from pathlib import Path
from flask import Flask, render_template, send_file, request, redirect, url_for, send_from_directory, Response, abort, flash
from werkzeug.utils import secure_filename
from database import userPassExists, userExists, insertUser4, insertUser6, getMainPage, getLocale, insertLocale
from werkzeug.utils import secure_filename
#from PyPDF2 import PdfFileReader, PdfFileWriter


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = set(['pdf'])


app = Flask(__name__)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


"""@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('index'))
	return 
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form action="" method=post enctype=multipart/form-data>
		<p><input type=file name=file>
			<input type=submit value=Upload>
	</form>
	<p>%s</p>
	% "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))#"""



uploadForm = """<form id="uploadcontent" method="post" style="display: inline-block"
  	width="20%" height="25%" enctype="multipart/form-data">
  	<input type="file" id="pdfbox" style="border: 1px solid black"
    	accept="application/pdf"><br>
  	<input type="submit" name="submit" value="Upload"><br>
	</form>"""
@app.route('/login', methods=['POST'])
def loginU():
	print('login post')
	print(request.args)
	print(request.data)
	print(request.form)
	print(request.files)
	print(request.values)
	if userPassExists(request.form.get('username'), request.form.get('password')):
		print('auth checked out')
		return send_file('templates/data/upload.txt')
	print('login pass')
	return 'False'#send_file('templates/data/upload.txt')
	
@app.route('/create-account', methods=['POST'])
def accountMaker():
	print('create post')
	print(userExists(request.form.get('username')))
	if not userExists(request.form.get('username')):
		insertUser4(request.form.get('username'), request.form.get('password'), request.form.get('firstname'), request.form.get('lastname'))
		print('user Inserted')
	print('create pass')

def pdfAdder():
	print('create post')
	for a1, a2 in request.args:
		print(a1 + "\t" + a2)
	print(userExists(request.form.get('username')))
	if userExists(request.form.get('username')):
		print('User exists, reading pdf')
		print(request.form.get('filename'))
		print(request.form.get('filesize'))
		return'True'
	print('create pass')
	return 'False'

@app.route('/<path:path>')
def serveFile(path):
	path = path.replace('\\', '', path.count('\\'))
	path = path.replace('%20', ' ', path.count('%20'))
	#path = path.replace('/', '\\/', path.count('/'))
	print(path)
	if path is not None:
		if userExists(path):
			locale = getLocale(path)
			if locale is not None:
				fileT = Path('files/'+locale)
				if fileT.is_file():
					return send_file('files/'+locale, attachment_filename=locale)
		else:
			fileT = Path('files/'+path)
			if fileT.is_file():
				return send_file('files/'+path, attachment_filename=path)
	return abort(404)

@app.route('/')
def index1():
	f = open('templates/landing.html','r')
	fileContent = f.read()
	#print(getMainPage())
	fileContent = fileContent.replace('$REPLACE_WITH_USER_LIST', getMainPage())
	return fileContent

@app.route('/create-account/')
def index2():
	return render_template('account.html')

@app.route('/style.css')
def style():
	return send_file('templates/style.css')
@app.route('/create-account/style.css')
def styleCA():
	return send_file('templates/style.css')

@app.route('/', methods = ['POST'])
def upload_file_req2():
	return upload_file(request)
		
@app.route('/upload', methods = ['POST'])
def upload_file_req():
	return upload_file(request)

def upload_file(request):
	if request.method == 'POST':
		#print(request.args)
		#print(request.data)
		print(request.form)
		print(request.files)
		print(request.values)
		print('if1')
		sys.stdout.flush()
		if 'file' not in request.files:
			print('file not found')
			sys.stdout.flush()
			#flash('No file part')
			return 'file not found'#redirect(request.url)
		file = request.files['file']
		username = request.form.get('username')
		sys.stdout.flush()
		print('if2')
		if file.filename == '':
			print('file not given')
			sys.stdout.flush()
			#flash('No selected file')
			return 'file not given'#redirect(request.url)
		print('if3')
		if file and allowed_file(file.filename) and username is not None:
			print('file found and written')
			sys.stdout.flush()
			filename = secure_filename(file.filename)
			file.save(os.path.join('./files/', filename))
			insertLocale(username, filename)
			#return redirect('./templates/landing.html')
			return 'Successful'
		else:
			print(file)
			print(allowed_file(file.filename))
			print(uesrname is not None)
		f = open('Hello World.pdf','w')
		f.write(request.form.get('file'))
		f.close()
		print('POSTING')
		sys.stdout.flush()
		for a1, a2 in request.args:
			print(a1 + "\t" + a2)
			sys.stdout.flush()
		#f = request.files['file']
		#f.save(secure_filename(f.filename))
		sys.stdout.flush()
		return 'Successful'
	

if __name__ == '__main__':
	app.run(debug=True, host='192.168.1.139', port='5397')
