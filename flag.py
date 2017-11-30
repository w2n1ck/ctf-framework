#!/usr/bin/env python

from http import http
from config import *
from function import *

# if u get the flag string, chk it before the post. If u still get some problems,
# this may blame to : 1.the network failure to flag_server
#		      2.the flag is out of data
def post_flag(flag):
    flag = flag.replace(" ","").replace("\n","")
    try:
	#res = http("post",flag_server,9000,flag_url,"flag="+flag+"&token="+flag_token,{}) 
	res = http("post",flag_server,flag_port,flag_url,"flag="+flag+"&token="+flag_token,{})
    except Exception,e:
	dump_error("flag server","flag post error","flag.py post_flag")
	return False
    if "success" in res:
	print '[!info] get flag success'
	return True
    return False


	
