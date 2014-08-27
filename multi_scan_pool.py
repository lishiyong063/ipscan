#coding:utf8
import commands
import multiprocessing
import re
import os


def getip(ip):
    q=commands.getstatusoutput('ping %s -c 1 -w 1'%ip)
    if q[0]!=0:
        return '%s----not online'%ip,os.getpid()
    else:
        return 'online:%s'%ip
ip_seg='192.168.1.2'
ip_list=[]
a=re.findall(r'\d+\.\d+\.\d+\.',ip_seg)

for i in range(1,255):
    ip_list.append('%s%s'%(a[0],i))
print ip_list


result=[]
pool_size = len(ip_list)
process_pool = multiprocessing.Pool(processes=pool_size)

for i in ip_list:
    result.append(process_pool.apply_async(func=getip,args=(i,)))


process_pool.close()
process_pool.join()

#apply用于传递不定参数，同python中的apply函数一致（不过内置的apply函数从2.3以后就不建议使用了），主进程会阻塞于函数。
'''for i in result:
    print i.get()
    '''
    
