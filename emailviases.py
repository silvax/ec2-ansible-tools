#! /usr/bin/env python

# This section loads libraries
import boto
from pprint import pprint
import sys
from datetime import datetime, date, time

htmlemailfile = open(sys.argv[3], 'r')
htmlemailbody = htmlemailfile.read()

emailfrom = sys.argv[1]
emailsubject = sys.argv[2]
emailto = sys.argv[4]
profile = sys.argv[5]

#sesconn = boto.connect_ses(mykey, mysecret)
sesconn = boto.connect_ses(profile_name=profile)

sesconn.send_email(
        emailfrom,
        emailsubject,
        "",
        [emailto],
        html_body = htmlemailbody,)
