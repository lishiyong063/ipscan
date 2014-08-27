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
        qu.put('online:%s'%ip)
#ip_seg=raw_input('Please enter your query IP network segment:')
ip_seg='192.168.1.2'
ip_list=[]
a=re.findall(r'\d+\.\d+\.\d+\.',ip_seg)

for i in range(1,255):
    ip_list.append('%s%s'%(a[0],i))
print ip_list
multi=[]

for i in ip_list:
    multi.append(multiprocessing.Process(target=getip,args=(i,)))

for i in multi:
    i.start()
    #i.join()不能再start后再执行join 否则每次子进程执行一次会等到执行完后再执行
for i in multi:
    i.join()
for i in ip_list:
  try: 
    print qu.get_nowait()#不等待没有数据则直接引发异常
  except:
    pass
