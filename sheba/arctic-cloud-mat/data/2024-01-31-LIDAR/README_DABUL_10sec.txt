Contact Name:  Janet Intrieri
Lab Affiliation: NOAA/ETL/ET2
Email: janet.intrieri@noaa.gov

Dataset Title: SHEBA Depolarization and Backscatter Unattended Lidar dataset
Version and Release Date:  Version 4, March 2002
Author: Janet Intrieri, Brandi McCarty
Source of Data: Depolariztion and Backscatter Unattended Lidar
Size of Data Set: 7500 MB (entire data set)
Data Format:  NetCDF

Brief Description:
The Depolarization and Backscatter - Unattended Lidar (DABUL) is a pulsed laser-radar
operating at 523 nm wavelength.  Range resolution is 30 m, and time resolution is as short as 1 s.
This lidar system uses a low energy laser with high repetition rates for good
sensitivity while being completely eyesafe.

Data are collected in four channels according to receiver field of view and polarization detected: 
far parallel, far perpendicular, near parallel, and near perpendicular.  The far channel has greater
sensitivity and a narrower field of view than the near channels. Linear polarization is transmitted,
and parallel and perpendicular refer to the polarization detected.  The depolarization ratios are
obtained by taking the ratio of the perpendicular to parallel channels in either the near or far
channels.  The far parallel lidar return is the field represented here, and the far parallel and far
perpendicular channels are used to calculate the depolarization ratios.

The FINAL data set provided here contains two products:
a.) Lidar returned-power netcdf data files  (variable name = far_parallel, [dB])
b.) Linear depolarization ratio netcdf data files   (variable name = depolarization, [dB])

Start and end of data collection, and interruptions:  
Three files per day include both of the final products available, and are named according to the
date it represents. For example, the file named "06120012.BARO.ncdf" represents data starting
at 00:12 UTC on June 12.  The letters after the date and time identify the corrections that have
been applied to the data. All of these final products have been averaged for 10 seconds. Data is
available up to 12.5 km, with a range resolution of 30 meters. All products are available for the
dates of Nov. 1, 1997 through Aug. 7, 1998, with the exception of the following periods:
1.) February 2 -13, offline due to heater repair
2.) July 5 - 10, offline due to shutter disabling
3.) Aug. 8,  laser failure, end of lidar SHEBA data set

The linear depolarization ratio (far perpendicular channel divided by far parallel channel) 
illustrate cloud phase. Generally, low values for the depolarization depolarization indicate
spherical particles (water or aerosols). Depolarization ratios greater than 0.1 indicate
shaped particles (ice phase).

Additional information or questions pertaining to the DABUL system should be directed to Dr.
Raul Alvarez (raul.alvarez@noaa.gov) and for information regarding the data fields or processing
please contact Janet Intrieri (janet.intrieri@noaa.gov) or Wynn Eberhard
(wynn.eberhard@noaa.gov).               

Additional information as well as examples of DABUL measurements
can be found on our web site:

 http://www2.etl.noaa.gov

and also at
 http://www6.etl.noaa.gov/projects/fireace.html

