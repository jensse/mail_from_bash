#!/usr/bin/python2.7


import ConfigParser

config = ConfigParser.RawConfigParser()
print "Generate a configfile, no testing input validation is applied"

config.add_section('Section1')
config.set('Section1', 'email', raw_input("Please enter sender email: "))
config.set('Section1', 'password', raw_input("Please enter password: "))
config.set('Section1', 'smtp.server', 'smtp.gmail.com')
config.set('Section1', 'smtp.port', '587')

# Writing our configuration file to 'example.cfg'
with open('send.cfg', 'wb') as configfile:
    config.write(configfile)
