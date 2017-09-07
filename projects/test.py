#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print()
def test():
 print ("This is written in python and if it works we have won the war.")
 return 1
test()
