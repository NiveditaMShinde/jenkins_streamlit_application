#!/bin/bash


cd /home/ec2-user/
sudo netstat -tnlp | grep 8501
if [ $(echo $?) = 1 ]
then
  	screen -m -d streamlit run app.py
else
      fuser -k 8501/tcp
      screen -m -d streamlit run app.py
fi
