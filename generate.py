import numpy as np;
import time;
import os;
import datetime;

while True:
    #Generate random number and push to dp.txt
    f_dp = open('dp.txt','a')
    a = str(np.random.randint(1, 200)) + '\r\n'
    f_dp.write(a)
    f_dp.close()

    #read current cpu_temp and push to cpu_temp.txt
    #f_cpu_temp = open('cpu_temp.txt','a')
    #a = str(datetime.datetime.now())+ "|" + str(os.popen('cat /sys/class/thermal/thermal_zone0/temp').read())
    #f_cpu_temp.write(a)
    #f_cpu_temp.close()

    #sleep for a while
    sl = np.random.randint(50, 1000)/1000
    time.sleep(sl)

