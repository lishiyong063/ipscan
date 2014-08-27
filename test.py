#coding:utf8
import commands
import multiprocessing
import re
import os
import time

def getip(ip):
    q=1
    if q!=0:
        print '%s----not online'%ip,os.getpid()
        time.sleep(10)
ip_seg='192.168.1.2'
ip_list=[]
a=re.findall(r'\d+\.\d+\.\d+\.',ip_seg)

for i in range(89,110):
    ip_list.append('%s%s'%(a[0],i))
print ip_list
multi=[]
for i in ip_list:
    multi.append(multiprocessing.Process(target=getip,args=(i,)))

for i in multi:
    i.start()

