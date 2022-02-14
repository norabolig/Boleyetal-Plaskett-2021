# 
# A. C. Boley. 15 Jul 2021
# Query JPL using available TLEs to get ephemerides 
#
import os
PMAX=15.1 # used for cutoffs by orbit rate
DIR='./'

COMMAND= 'TLE'
CENTER= '658@399'
MAKE_EPHEM= 'YES'
TABLE_TYPE= 'OBSERVER'
START_TIME= '2021-07-16 04:00'
STOP_TIME= '2021-07-16 16:00'
STEP_SIZE= '86400'
CAL_FORMAT= 'CAL'
TIME_DIGITS= 'MINUTES'
ANG_FORMAT= 'HMS'
OUT_UNITS= 'KM-S'
RANGE_UNITS= 'AU'
APPARENT= 'AIRLESS'
ELEV_CUT= '45'
SUPPRESS_RANGE_RATE= 'NO'
SKIP_DAYLT= 'YES'
EXTRA_PREC= 'NO'
R_T_S_ONLY= 'NO'
REF_SYSTEM= 'J2000'
CSV_FORMAT= 'NO'
OBJ_DATA= 'YES'
QUANTITIES= '1,3,4,5,7,20,23,24'

fname = DIR+"starlink.15JUL2021"

import sys

if len(sys.argv)>1:
   fname = sys.argv[1]

print("opening file {}".format(fname))

fh = open(fname,"r")

step=0
for line in fh:
   if step==0:
      SAT=line.rstrip()
      step+=1
   elif step==1: 
      TLE1 = line.rstrip()
      step+=1
   else: 
      TLE2 = line.rstrip()
      val = TLE2.split()
      P = float(val[7])
      step=0

      if P < PMAX:

        TLE = TLE1+'%0A '+TLE2
        url="https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&TLE='{}'&COMMAND='{}'&CENTER='{}'&MAKE_EPHEM='{}'&TABLE_TYPE='{}'&START_TIME='{}'&STOP_TIME='{}'&STEP_SIZE='{}',CAL_FORMAT='{}'&TIME_DIGITS='{}'&ANG_FORMAT='{}'&OUT_UNITS='{}'&RANGE_UNITS='{}'&APPARENT='{}'&ELEV_CUT='{}'&SUPPRESS_RANGE_RATE='{}'&SKIP_DAYLT='{}'&EXTRA_PREC='{}'&R_T_S_ONLY='{}'&REF_SYSTEM='{}'&CVS_FORMAT='{}'&OBJ_DATA='{}'&QUANTITIES='{}'".format(TLE,COMMAND,CENTER,MAKE_EPHEM,TABLE_TYPE,START_TIME,STOP_TIME,STEP_SIZE,CAL_FORMAT,TIME_DIGITS,ANG_FORMAT,OUT_UNITS,RANGE_UNITS,APPARENT,ELEV_CUT,SUPPRESS_RANGE_RATE,SKIP_DAYLT,EXTRA_PREC,R_T_S_ONLY,REF_SYSTEM,CSV_FORMAT,OBJ_DATA,QUANTITIES)

        command="curl -o '"+DIR+SAT+".txt' "+'"'+url+'"'

        print(command)

        os.system(command)

        

