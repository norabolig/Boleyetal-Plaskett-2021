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
