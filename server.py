import os
from flask import Flask, render_template

UPLOAD_FOLDER = '~/Python-3.6.0/test/files/'
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template('landing.html')

if __name__ == '__main__':
	app.run(debug=True, host='192.168.1.139', port='5397')


