import os
from flask import Flask, render_template, send_file, request, redirect, url_for, send_from_directory
from database import userPassExists, userExists, insertUser4, insertUser6, getMainPage
#from werkzeug.utils import secure_filename
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

@app.route('/login', methods=['POST'])
def loginU():
	print('login post')
	print(userPassExists(request.form.get('username'), request.form.get('password')))
	print('login pass')
	return ''
	
@app.route('/create-account', methods=['POST'])
def accountMaker():
	print('create post')
	print(userExists(request.form.get('username')))
	if not userExists(request.form.get('username')):
		insertUser4(request.form.get('username'), request.form.get('password'), request.form.get('firstname'), request.form.get('lastname'))
		print('user Inserted')
	print('create pass')
	return ''

@app.route('/files/<path:path>')
def serveFile(path):
	path = path.replace('\\', '', path.count('\\'))
	path = path.replace('%20', ' ', path.count('%20'))
	#path = path.replace('/', '\\/', path.count('/'))
	print(path)
	return send_file('files/'+path, attachment_filename=path)

@app.route('/')
def index1():
	return render_template('landing.html')

@app.route('/create-account/')
def index2():
	return render_template('account.html')

if __name__ == '__main__':
	app.run(debug=True, host='192.168.1.139', port='5397')
	

