#coding:utf8
import commands
import threading
import re
import os
import eventlet
import time

'''
    eventlet:1.非阻塞I/O模型
             2.协程(Coroutines)使得开发者可以采用阻塞式的开发风格,却能够实现非阻塞I/O的效果
             3.隐式事件调度,使得可以在Python解释器或者应用程序的某一部分去使用Eventlet
             4.多个协同程序间表现为协作运行，如A的运行过程中需要B的结果才能继续运行
             5.并不是真正意义上的并发只是不存在阻塞的问题
'''

def getip(ip):
    q=commands.getstatusoutput('ping %s -c 1 -w 1'%ip)
    if q[0]!=0:
        print '%s----not online'%ip,os.getpid()
        return 'false'
    else:
        print '----------'
        return ip
#ip_seg=raw_input('Please enter your query IP network segment:')
ip_seg='192.168.1.2'
ip_list=[]
a=re.findall(r'\d+\.\d+\.\d+\.',ip_seg)

for i in range(89,110):
    ip_list.append('%s%s'%(a[0],i))

pool = eventlet.GreenPool(20)

try:
    for ip in pool.imap(getip,ip_list):
        if ip != 'false':
            print 'online:',ip
except:
    print 'error'
