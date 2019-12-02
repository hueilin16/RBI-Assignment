# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:46:01 2019

@author: Hueilin
"""
#In command prompt:
#pip install awscli
#aws configure
#key in ACCESS_KEY_ID, ACCES_SECRET_KEY, and region name

import boto3

#Upload a file
s3 = boto3.client('s3')
s3.meta.upload_file('S3_transfer.txt','Bucket1','S3_script.txt')

#Download a file
s3.meta.download_file('Bucket1','S3_script.txt','S3_downloadfile.txt')

#Download all the files in a folder
list=s3.list_objects(Bucket='Bucket1')['Contents']
for key in list:
    s3.download_file('Bucket1', key['Key'], key['Key'])