#
# A. C. Boley, 15 Sept 2021
# Convenience script for Boley et al. 2021 paper
#
import numpy as np

fh = open("plan.ran","r")

for line in fh:
    utc = line[31:43]
    dra = float(line[71:81])
    dde = float(line[81:90])
    distance = float(line[142:158])*1.496e8
    print("Sat = {} rate = {} arcsec/s utc = {} distance = {} km".format(line[0:14],np.sqrt(dra**2+dde**2)/3600,utc,distance))
