#
# A. C. Boley, 15 Sept 2021
# Script for Boley et al. 2021 paper
# Used to sort candidate observations by UTC and with a separation of deltaT in minutes.
#
# 2021-Jul-15 08:23:48.000  t  21 24 25.83 +10 37 45.4 6851521.  2878021. 142.0829  46.6461 -122997.  -3280.97 19 43 46.3759 0.00000490077799   0.1676220 138.6407 /L  41.3601
import numpy as np

fh=open('dat','r')
MINAZ=90
MAXAZ=270
deltaT = 4 # min

doc=[]
lst=[]
utc=[]
az=[]
time=[]
for line in fh:
  doc.append(line.rstrip())
  na,st=line.split(":",1)
  hr = float(st[13:15])
  min = float(st[16:18])
  sec = float(st[19:25])

  utc.append(hr+min/60+sec/3600)
  az.append(float(st[72:81]))
  d=st[1:12]
  t=st[13:25]
  s=d+"T"+t
  s=s.replace("Jul","07")
  time.append(np.datetime64(s))

utc = np.array(utc)
az = np.array(az)

id = np.argsort(utc)

#print(utc[id])

tnow=time[id[0]]-np.timedelta64(20,"m")
for i in id:
#  print(time[i])
  if az[i] > MINAZ and az[i] < MAXAZ:
     if time[i]>tnow+np.timedelta64(deltaT,"m"):
       print(doc[i])
       tnow=time[i]


  

  
