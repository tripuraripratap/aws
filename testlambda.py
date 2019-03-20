'''
You need to have AWS credentials in ~/.aws/credentials
[default]
aws_access_key_id=KEY_ID
aws_secret_access_key=ACCESS_KEY
S3_BUCKET_NAME=BUCKET_NAME
'''

import time,json,os
from flask import Flask, render_template,request
from werkzeug import secure_filename
import boto3, botocore, time, json

S3_BUCKET                 = os.environ.get("S3_BUCKET_NAME")

client = boto3.client('lambda', region_name='ap-south-1')
s3 = boto3.resource("s3", region_name='ap-south-1')
localtime = time.asctime(time.localtime(time.time()))

app = Flask(__name__)

@app.route('/hello/<name>')
def uppercase(name):
    payload = '{"key1":"%s"}' % (name)
    response = client.invoke(FunctionName='myFunction1st', Payload=payload)
    print(response)

    output = json.loads(response['Payload'].read().decode('utf-8'))
    result1 = {'input' :input ,'return_str':output}
    return render_template('upper.html', result=result1)

@app.route('/')
def hello():
   return render_template('index.html')
   
@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/loginsuccess')
def loginsuccess():
   return render_template('loginsuccess.html')

@app.route('/upload', methods = ['POST'])
def upload():
    output = ''
    file = request.files['myfile']
    s3.Bucket(S3_BUCKET).put_object(Key=secure_filename(file.filename), Body=request.files['myfile'])
    payload = '{"key1":"%s", "key2":"%s"}' % ((secure_filename(file.filename)), (S3_BUCKET))
    response = client.invoke(FunctionName='myFunction2nd', Payload=payload)
    output = json.loads(response['Payload'].read().decode('utf-8'))
    print(output)
    return render_template('upper1.html', result=output)

@app.route('/loadimage')
def loadimage():
   return render_template('uploadimg.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8888)
   app.run(debug=True)
