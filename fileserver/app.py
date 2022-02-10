import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_autoindex import AutoIndex

app = Flask(__name__)


ppath = "uploadedFiles"
AutoIndex(app, browse_root=ppath)


app.config['UPLOAD_FOLDER'] = './uploadedFiles'
@app.route('/upload_file')
def upload_file():
	return render_template("upload_file.html")

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return render_template("uploader.html")


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0' port=5000)

