from fileinput import filename
import subprocess
from flask import Flask, render_template, request, send_file, url_for, jsonify
# from nfstream_script import pcapTocsv
from nfstream import NFStreamer
import os

app = Flask(__name__)
fileName = ''
@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
        uploaded_file = request.files['file']
        uploaded_file.save(uploaded_file.filename)
        fileName = uploaded_file.filename
        # path = fileName
        pcap = fileName
        file = open('nfstream_script.py')
        # fileName = fileName[:-4]
        # path = fileName

        subprocess.call(['python', 'nfstream_script.py', fileName])
        fileName += '.csv'

        os.remove(pcap)
        
        return send_file(fileName, as_attachment=True)
		
if __name__ == '__main__':
   app.run(debug = True)


# @app.route('/')
# def index():
#     return render_template('index.html')
