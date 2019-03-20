#!/bin/bash
sudo su
yum update -y
yum install python3 -y
/usr/bin/pip3.7 install flask
/usr/bin/pip3.7 install boto3
mkdir /usr/src/templates
cd /usr/src

aws s3 cp s3://myassignment12032019/index.html /usr/src/templates
aws s3 cp s3://myassignment12032019/myscript /etc/init.d
aws s3 cp s3://myassignment12032019/upper.html /usr/src/templates
aws s3 cp s3://myassignment12032019/upper1.html /usr/src/templates
aws s3 cp s3://myassignment12032019/login.html /usr/src/templates
aws s3 cp s3://myassignment12032019/loginsuccess.html /usr/src/templates
aws s3 cp s3://myassignment12032019/uploadimg.html /usr/src/templates
aws s3 cp s3://myassignment12032019/testlambda.py /usr/src/

nohup /usr/bin/python3.7 /usr/src/testlambda.py 8888 &
cd /etc/init.d
chmod 755 /etc/init.d/myscript
chkconfig --add myscript
chkconfig --level 2345 myscript on


