# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:31:02 2019

@author: hueil
"""
import boto3

#Create an instance
ec2 = boto3.client('ec2')
ec2.create_instances(ImageId='ami-12345678',
    InstanceType='t2.micro',
    MaxCount=123,
    MinCount=123,)

#Terminate an instance
ec2.instances.filter(InstanceIds='instance-id').terminate()