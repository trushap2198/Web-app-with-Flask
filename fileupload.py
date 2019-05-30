from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def up_file():
	return render_template('upload.html')

@app.route('/uploader', methods= ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f= request.files['file']
		f.save(secure_filename(f.filename))#to obtain secure version of file
		return 'file uploaded'

if __name__ == '__main__':
	app.run(debug= True)
