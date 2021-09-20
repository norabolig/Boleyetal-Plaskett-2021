# Boleyetal-Plaskett-2021
Associated data for Boley et al. 2021, Plaskett measurements of Starlink satellites

Supplemental Data
=================

This repo contains supplemental data for Boley et al 2021, _Plaskett 1.8 metre Observations of Starlink Satellites_.
It is provided for independent assessment, as well as to share details that typically are not included in a paper. 
If you use information provided here, please cite the Boley et al. 2021 paper.

All observations were conducted in the g' filter.

Main Photometry File
--------------------

`mags-streaks.dat` contains the photometric measurements and additional information needed to reconstruct the magnitudes listed in the paper. 

The header is as follows:  
`Name magC magCsig adu npix bkgnd streak rate range utc sto visorsat oper`
* Name: Satellite name
* magC: Magnitude zero point for image
* magCsig: Dispersion in zero points among calibration stars
* adu: Measured adu in all boxes along the streak
* npix: Number of pixels in all boxes for the measured adu
* bkgnd: Average background pixel value as determined by pixels in the proximity (but away from) the streak and as free of stars as practicable
* streak: Length of all boxes together along the streak, measured in arcsec
* rate: rate of satellite across the FOV in arcsec/s, as determined by the JPL emphemeris service and the corresponding TLEs
* utc: Time of start of observation in utc (16 Jul 2021), chosen such that the satellite is expected to pass through the FOV 15 seconds into the 30 second exposures.
* sto: Sun-Target-Observer angle, essentially the phase angle, in degrees
* visorsat: bool whether a visorsat or not (inferred)
* oper: `+` means the satellite was operational at the time of the observations and `-` if it was defunct

Plotting and Stats File
-----------------------

`satplot.py` produces all figures in the paper and also prints out some basic stats, such as the medians.

TLEs
----

`starlink.15JUL2021` are the TLEs for all Starlink satellites on the noted date. This was used for developing the observing plan and is made available by T. S. Kelso at Celestrak.com.

JPL Query
---------

`get_eph.py` queries JPL Horizons using the TLE file and some in-code information (careful, some of it is project specific). It will produced a `NAME.txt` file, where `NAME` is the name of the satellite. The query contains elevation and azimuth cuts.

Observing Opportunities 
-----------------------

`dat` is a txt file that contains all of the resulting ephemerides at the time of transt, as `grepped` from the output files of `get_eph.py`.

Observing Plan Rough Cut
------------------------

`reorder.py` looks through the `dat` file, sorts by UTC, and then develops a preliminary plan to be sent to the telescope operator. Targets are selected so that they are so many minutes apart. The output is the file `plan`. The telescope operator had the final decision on which targets to select, which resulted in the closely related file `plan.ran`. This latter file is the one that has the time spacing noted in the paper. 

Convenience Scripts
-------------------

When writing the paper, a few convenience scripts were made to pring out relevant information.  This is the purpose of `printrates.py` and `printtable.py`, which both print observational information from `plan.ran`. The file `mcmc.py` runs a fast and simple MCMC to determine the power law formulation of the super(?) diffuse phase function. It reads in `mags-streaks.mcmc`, which is just like `mags-streaks.dat`, but with the outliers commented out.

Calibrated Images
-----------------

Astrometically calibrated, reduced, and flattened images are in the `calibratedImages` folder. The suffixes have ".new", but they are all fits files. 

Aperture Files
--------------

Aperture files for the stars used in the photometric calibration. Values are given in "physical coordinates" as defined in DS9, and are arranged as CENTRE_X CENTRE_Y R_IN R_OUT for the apertures.

Region Files
------------

Region files for DS9, in degrees, giving the details for where the streaks were measured. 



