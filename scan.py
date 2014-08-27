#coding:utf8
import commands
import multiprocessing
import re
import os


qu=multiprocessing.Queue()
def getip(ip):
    q=commands.getstatusoutput('ping %s -c 1 -w 1'%ip)
    if q[0]!=0:
        print '%s----not online'%ip,os.getpid()
    else:
        print 'online:',ip
ip_seg='192.168.1.2'
ip_list=[]
a=re.findall(r'\d+\.\d+\.\d+\.',ip_seg)

for i in range(89,110):
    ip_list.append('%s%s'%(a[0],i))
print ip_list

for i in ip_list:
    getip(i)

