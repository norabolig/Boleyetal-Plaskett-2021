import numpy as np

df = np.loadtxt("mags-streaks.dat",skiprows=1,dtype={'names':('Name','magC','magCsig','adu','npix','bkgnd','streak','rate','range','utc','sto','visorsat','oper'),'formats':('U14','f','f','f','f','f','f','f','f','U12','f','U1','U1')})

print(df)

print(df['utc'])

datetime=[]
for i,utc in enumerate(df['utc']):
    print(i,utc,'2021-07-16T'+utc)
    datetime.append('2021-07-16T'+utc)

dates = np.array(datetime,dtype='datetime64')


mags = -2.5*np.log10(df['adu']-df['npix']*df['bkgnd'])+df['magC']-2.5*np.log10(30*df['rate']/df['streak'])
MAGS = (mags-5*np.log10(df['range']/550))
magsRound = np.round(mags,decimals=1)
MAGSRound = np.round(MAGS,decimals=1)

print(magsRound)
print(MAGSRound)

vflag = df['visorsat'] == 'T'
sflag = df['visorsat'] == 'F'


print("ALL Median for mags {} ".format(np.median(magsRound)))
print("ALL Median for MAGS {}".format(np.median(MAGSRound)))

print("ORIG Median for mags {} ".format(np.median(magsRound[sflag])))
print("ORIG Median for MAGS {}".format(np.median(MAGSRound[sflag])))

print("Visor Median for mags {} ".format(np.median(magsRound[vflag])))
print("Visor Median for MAGS {}".format(np.median(MAGSRound[vflag])))

#
#
# histograms
#
#
bins = np.array([3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5])

counts,edges=np.histogram(magsRound,bins)

import matplotlib.pylab as plt

fig,ax=plt.subplots()
plt.hist(magsRound,bins=edges,color='steelblue',edgecolor='black')
plt.hist(magsRound[vflag],bins=edges,color='red',edgecolor='black')
plt.title("Apparent Magnitudes",fontsize=16)
plt.xlabel(r"$m_g$",fontsize=16)
plt.ylabel(r"Number",fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylim(0,8.5)
plt.subplots_adjust(bottom=0.15)
plt.legend(['S','V'])
ax.tick_params(length=6)
plt.savefig("hist-apparent.pdf")

fig,ax=plt.subplots()
plt.hist(MAGSRound,bins=edges,color='steelblue',edgecolor='black')
plt.hist(MAGSRound[vflag],bins=edges,color='red',edgecolor='black')
plt.title("Absolute Magnitudes (550 km)",fontsize=16)
plt.xlabel(r"$H_g^{550}$",fontsize=16)
plt.ylabel(r"Number",fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylim(0,8.5)
plt.subplots_adjust(bottom=0.15)
ax.tick_params(length=6)
plt.legend(['S','V'])
plt.savefig("hist-absolute.pdf")

#
# Scatter Plots
#
#

pointnum = np.array(range(1,len(magsRound)+1))
satrange=df['range']

fig,ax=plt.subplots()
ax.scatter(satrange[sflag],magsRound[sflag],s=200,facecolors='none',edgecolors='black',marker='s')
ax.scatter(satrange[vflag],magsRound[vflag],s=200,facecolors='none',edgecolors='black',marker='o')
for i in range(len(magsRound)):
   ax.annotate(repr(pointnum[i]),(satrange[i],magsRound[i]),ha='center',va= 'center')
ax.legend(['S','V'],loc='lower left',fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Range [km]',fontsize=14)
plt.ylabel(r"$m_g$",fontsize=16)
plt.ylim(10.5,4)
plt.savefig("sats-range.pdf")

sto=df['sto']
fig,ax=plt.subplots()
ax.scatter(sto[sflag],magsRound[sflag],s=200,facecolors='none',edgecolors='black',marker='s')
ax.scatter(sto[vflag],magsRound[vflag],s=200,facecolors='none',edgecolors='black',marker='o')
for i in range(len(magsRound)):
   ax.annotate(repr(pointnum[i]),(sto[i],magsRound[i]),ha='center',va= 'center')
ax.legend(['S','V'],loc='lower right',fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('STO [deg]',fontsize=14)
plt.ylabel(r"$m_g$",fontsize=16)
plt.ylim(10.5,4)
plt.savefig("sats-sto.pdf")

fig,ax=plt.subplots()
ax.scatter(sto[sflag],satrange[sflag],s=200,facecolors='none',edgecolors='black',marker='s')
ax.scatter(sto[vflag],satrange[vflag],s=200,facecolors='none',edgecolors='black',marker='o')
for i in range(len(magsRound)):
   ax.annotate(repr(pointnum[i]),(sto[i],satrange[i]),ha='center',va= 'center')
ax.legend(['S','V'],loc='lower left',fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('STO [deg]',fontsize=14)
plt.ylabel("Range [km]",fontsize=16)
plt.savefig("sats-sto-range.pdf")


import matplotlib.dates as mdates

fig,ax=plt.subplots()
ax.scatter(dates[sflag],magsRound[sflag],s=200,facecolors='none',edgecolors='black',marker='s')
ax.scatter(dates[vflag],magsRound[vflag],s=200,facecolors='none',edgecolors='black',marker='o')
for i in range(len(magsRound)):
   ax.annotate(repr(pointnum[i]),(dates[i],magsRound[i]),ha='center',va= 'center')
ax.legend(['S','V'],loc='lower right',fontsize=12)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
fig.autofmt_xdate()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('UTC [16 Jul 2021]',fontsize=14)
plt.ylabel(r"$m_g$",fontsize=16)
plt.ylim(10.5,4)
plt.xlim(min(dates)-np.timedelta64(30,'m'),max(dates)+np.timedelta64(30,'m'))
plt.savefig("sats-time.pdf")

#
# Now we need models
#
#

def diffuseSphere(zeta,sto,R,beta=1):
   fac1 = 2/(3*np.pi**2)
   sto = sto*np.pi/180
   model = -26.47 -2.5*np.log10( fac1 * zeta * ( beta * ((np.pi-sto)*np.cos(sto) + np.sin(sto) )) + (1-beta)/(4*np.pi) ) + 5 * np.log10(R*1e3)
   return model

def diffusePower(zeta,sto,R,p):
   fac1 = 2/(3*np.pi**(p+1))
   sto = sto*np.pi/180
   model = -26.47 -2.5*np.log10( fac1 * zeta * ( ((np.pi-sto)*np.cos(sto) + np.sin(sto) ))**p  ) + 5 * np.log10(R*1e3)
   return model

dsphere = diffuseSphere(0.7,sto,satrange)
dpower  = diffusePower(1.1,sto,satrange,3.1)
diff = magsRound-dpower

fig,ax=plt.subplots()
ax.scatter(sto[sflag],magsRound[sflag],s=200,facecolors='none',edgecolors='black',marker='s')
ax.scatter(sto[vflag],magsRound[vflag],s=200,facecolors='none',edgecolors='black',marker='o')
ax.scatter(sto,dsphere,s=120,color='red',marker='v')
ax.scatter(sto,dpower,s=120,color='blue',marker='^')
for i in range(len(magsRound)):
   ax.annotate(repr(pointnum[i]),(sto[i],magsRound[i]),ha='center',va= 'center')
ax.legend(['S','V','D','P'],loc='lower right',fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('STO [deg]',fontsize=14)
plt.ylabel(r"$m_g$",fontsize=16)
plt.ylim(10.5,4)
plt.savefig("sats-sto-diffuse.pdf")

fig,ax=plt.subplots()
ax.scatter(sto[sflag],diff[sflag],s=200,facecolors='none',edgecolors='black',marker='s')
ax.scatter(sto[vflag],diff[vflag],s=200,facecolors='none',edgecolors='black',marker='o')
for i in range(len(magsRound)):
   ax.annotate(repr(pointnum[i]),(sto[i],diff[i]),ha='center',va= 'center')
ax.legend(['S','V'],loc='lower right',fontsize=12)
plt.axhline(y=0,color='black',linestyle=':')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('STO [deg]',fontsize=14)
plt.ylabel(r"$m_g$-Model",fontsize=16)
plt.ylim(5,-1)
plt.savefig("sats-obs-model.pdf")




plt.show()


#Name magC magCsig adu npix bkgnd streak rate range utc sto visorsat oper

