from flask import Flask, request, redirect, url_for, render_template
import boto3
import os

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        s3.upload_fileobj(
            file,
            'cloud-photo-lib',  
            file.filename,
            ExtraArgs={'ACL': 'public-read'}  
        )
        
        return redirect(url_for('index'))
    return "Failed to upload"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
