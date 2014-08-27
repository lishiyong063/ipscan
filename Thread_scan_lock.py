#coding:utf8
import commands
import threading
import re
import os

lock=threading.Lock()
line=[]
def getip(ip):
    global line
    q=commands.getstatusoutput('ping %s -c 1 -w 1'%ip)
    if q[0]!=0:
        print '%s----not online'%ip,os.getpid()
    else:
        lock.acquire()
        line.append('online:%s'%ip)
        lock.release()
        '''不知道为什么加不加锁好像都是一样的结果'''
#ip_seg=raw_input('Please enter your query IP network segment:')
ip_seg='192.168.1.2'
ip_list=[]
a=re.findall(r'\d+\.\d+\.\d+\.',ip_seg)

for i in range(1,255):
    ip_list.append('%s%s'%(a[0],i))
print ip_list
mu_th=[]

for i in ip_list:
    mu_th.append(threading.Thread(target=getip,args=(i,)))

for i in mu_th:
    i.start()
for i in mu_th:
    i.join()

print '\n'.join(line)
