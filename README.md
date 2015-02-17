# Mail From Bash

This is a collection of scripts to send email from the command line. That I use on from my Ubuntu, and 
previously from my OSX computer.  The intention is to make them better, refine them.


## To the one

I grabbed this python script (__./bin/send.py__) from the internet (no credit was taken, but thanks!), and it works brilliant for sending 
emails from the Linux command line.

In order to use this scrip you need to modify the lines, with your own values:

  sender = 'your account@gmail.com'
  password = "the password"


## To the many!

When i need to send "spam", to the team, I use the __./bin/send.sh__ wrapper and modify the __to.csv__ 
accordingly, "email;The message;the attachment".

Hopefylly I get arround to do somthing about it, at least now its in Git.
