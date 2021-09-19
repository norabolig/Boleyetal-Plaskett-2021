#
# A. C. Boley, 15 Sept 2021
# Convenience script for Boley et al. 2021 paper
#
import numpy as np

fh = open("plan.ran","r")

#STARLINK-2195.txt: 2021-Jul-16 10:53:10.000 At  22 51 39.83 +35 54 22.5 8585115.  3706662. 149.4319  75.9273 -155151.  -3120.17 22 17 29.4634 0.00000388212255   0.0390493 107.4124 /L  73.5878

for line in fh:
    utc = line[31:43]
    dra = float(line[71:81])
    dde = float(line[81:90])
    ra = line[47:60]
    dec = line[60:71]
    az = float(line[91:100])
    el = float(line[100:108])
    phase = float(line[184:191])
    distance = float(line[142:158])*1.496e8



    #print("Sat = {} rate = {} arcsec/s utc = {} distance = {} km".format(line[0:14],np.sqrt(dra**2+dde**2)/3600,utc,distance))
    print(" {} & {} & {} & {} & {:.2f} & {:.2f} & {:.0f} & {:.1f} & {:.0f}\\\\".format( line[0:13], utc, ra, dec, az, el, np.sqrt(dra**2+dde**2)/3600, distance, phase) ) 
