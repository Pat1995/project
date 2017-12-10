#!/usr/bin/python

import threading
import time
import thread

def jedzenie(nr, widelce, lock):
    
    count = 0
    
    if ((nr+1)%5 > nr):
       widelce[nr%5].acquire()
       time.sleep(5)
       widelce[(nr+1)%5].acquire()
    else:
       widelce[(nr+1)%5].acquire()
       time.sleep(5)
       widelce[nr%5].acquire()

    print "jem"

    if ((nr+1)%5 > nr):
       widelce[(nr+1)%5].release()
       widelce[nr%5].release()
    else:       
       widelce[nr%5].release()
       widelce[(nr+1)%5].release()
       
    print "juz nie jem\n"

print "Jadalnia wita\n"

widelce = []
for i in range(0,5):
    widelce.append(threading.Lock())
lock = threading.Lock()

try:
   thread.start_new_thread( jedzenie, (0, widelce, lock) )
   time.sleep(10)
   thread.start_new_thread( jedzenie, (1, widelce, lock) )
   time.sleep(10)
   thread.start_new_thread( jedzenie, (2, widelce, lock) )
   time.sleep(10)
   thread.start_new_thread( jedzenie, (3, widelce, lock) )
   time.sleep(10)
   thread.start_new_thread( jedzenie, (4, widelce, lock) )
   time.sleep(10)

except:
   print "Error: unable to start thread"

print "Jadalnia zegna\n"
