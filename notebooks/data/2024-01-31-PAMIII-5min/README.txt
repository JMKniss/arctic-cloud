TITLE: Ice Camp Surface Mesonet NCAR PAM-III (netCDF)

AUTHORS: Edgar L. Andreas
        CRREL
        72 Lyme Rd
        Hanover NH  03755-1290
        Tel: (603) 646-4436
        eandreas@nwra.com

	Christopher W. Fairall
	NOAA/ESRL
	DSRC, Bldg 33
	325 Broadway
	Boulder CO  80305-3337
	Tel: (303) 497-3253
	chris.fairall@noaa.gov

	Peter S. Guest
	NPS
	Monterey, CA 93943
	Tel: (831) 656-2451
	pguest@nps.navy.mil
        www.weather.nps.navy.mil/~psguest/sheba/

	P. Ola G. Persson
	NOAA/ESRL
	DSRC, Bldg 33
	325 Broadway
	Boulder CO 80305-3337
	Tel: (303) 497-5078
	ola.persson@noaa.gov
	

1.0 DATA SET OVERVIEW

SHEBA (Surface Heat Budget of the Arctic) is an interdisciplinary
program to study the interactions of clouds, atmospheric radiation,
and the surface energy balance over the Arctic Ocean. The field phase
involved the deployment of numerous measurement systems on board and
in the vicinity of the Canadian ice breaker N.G.C.C. Des Groseilliers,
which was frozen into the Arctic ice pack north of Alaska from October
1997 to October 1998. During this period, Ice Station SHEBA drifted
from approximately 75 N, 144 W to 80 N, 166 W.  

The research teams at the ice camp included the SHEBA Atmospheric
Surface Flux Group (ASFG), which was responsible for direct
measurement of the fluxes contributing to the surface energy
balance. The principal investigators in this group are Ed Andreas
(U.S. Army Cold Regions Research and Engineering Laboratory), Chris
Fairall (NOAA Environmental Technology Laboratory), Peter Guest (Naval
Postgraduate School), and Ola Persson (NOAA Environmental Technology
Laboratory and the Cooperative Institute for Research in Environmental
Sciences). The Atmospheric Surface Flux Group instrumented a 20 m
micrometeorological tower located about 1 km from the Des Groseilliers
and also requested the use of four NCAR Flux-PAM stations to measure
fluxes over a variety of different surface types.  

2.0 INSTRUMENT DESCRIPTION

Flux-PAM remote meteorological stations are one of the principal
components of the NCAR Integrated Surface Flux Facility (ISFF). These
stations measure the standard meteorological variables of wind,
temperature, humidity, pressure and precipitation plus net radiation,
soil heat flux and the eddy fluxes of momentum, water vapor and
sensible heat. To provide maximum siting flexibility, Flux-PAM
stations are powered by solar-charged batteries and the sensor are
mounted on an internally-guyed mast with a tripod base. The Flux-PAM
data-processing computer, known as EVE, ingests data from the sensors
at rates commensurate with their individual response characteristics
and calculates 5-min means, variances and covariances. These data
statistics are stored locally on EVE and also transmitted to a base
computer system for archival, analysis and display. Data transmission
is accomplished in real time either through the GOES satellite and/or,
for networks of limited spatial extent, by means of line-of-sight RF
modems. For SHEBA, RF modems were used to transmit the data from each
station to a base computer located on the Des Groseilliers.  
In order to meet the research requirements of the SHEBA Atmospheric
Surface Flux Group, the Flux-PAM stations required several
modifications.  

Propane-fueled thermoelectric generators were used to power the
stations, supplemented during the spring and summer with solar panels
and (at two stations) wind generators. For operation in the extreme
cold, the thermoelectric generator and propane bottles were packaged
with the 12V batteries and data computer in an insulated
container. For station portability, each of these containers was
mounted on a freighter sled that could be towed by snowmobile. In
order to accurately determine true wind direction on the drifting ice
pack, an electronic compass was mounted on the meteorological mast to
measure station orientation. A strobe beacon and GPS receiver were
added to help service personnel locate the sites, to archive station
coordinates, and for accurate time-keeping. 
 
Several adaptations were also made to the standard complement of
Flux-PAM sensors. Because of sensor maintenance requirements, no
attempt was made to directly measure eddy fluxes of water vapor. The
standard net radiometer was replaced by a 4-component measurement of
incoming and outgoing, short and long-wave radiation utilizing
aspirated Kipp and Zonen pyranometers and Eppley pyrgeometers. Since
the standard platinum-resistance thermometer used by Flux-PAM has a
lower limit of -40 C, it was supplemented with a thermistor
calibrated over the range -55 C to 10 C. 

3.0 DATA COLLECTION AND PROCESSING

The SHEBA Flux-PAM data are available at two time resolutions, five-minute 
averages and one-hour averages.  The basic data archived during field 
operations are five-minute averages calculated at each Flux-PAM site by the 
EVE data systems. The five-minute data were stored on removable media on the 
local station data systems and also transmitted by RF modem to the base 
computer on the Des Grosseiliers. These two overlapping data sets have been 
merged during post-project processing to fill in non-coincident data gaps 
present in both sets.  

Various corrections have been applied to the five-minute data during post-project 
processing. Most of these have been discussed in the sections of the report that 
correspond to individual sensors. They include

    * interpolating between pre- and post-project radiometer calibrations,
    * correction to the compass reading for offsets generated when the beacon was on,
    * use of a 1-hour median filter to remove known spikes in the compass and 
         hygrothermometer data in October 1997,
    * subtracting offsets from the radiometer level data,
    * calibration correction to the Tsoil/ice sensor at Station 2 after April 11,
    * correction to Solent virtual temperature data prior to June 21,
    * where possible, the wind measurements from the sonic anemometer have been 
         rotated into a coordinate system with its vertical axis normal to a plane 
         defined by the local mean wind field. 

Missing or obviously erroneous compass data have not been replaced in the 5-minute 
data record (with the exception noted above), but obviously erroneous data have 
been flagged as missing, including compass data collected during operation of the 
sonic heaters. For most of the project, the orientation of the stations, and thus 
the compass data, varied rather slowly. Thus it was thought to be generally 
acceptable to fill in the missing data by interpolation (and extraplotion) during 
the calculation of derived variables such as Vazimuth, dir, or boom. 

Hourly averages of most data parameters, centered on the half-hour,
have been calculated during post-project processing. The hour-average
parameters generally, but not always, correspond to the five-minute
parameters. For example, the pyrgeometer thermopile and temperature
measurements have been combined to calculate the long-wave radiation
flux, the PRT and thermistor data have been combined into a single
value for the air temperature, and the PRT and RH (with respect to
water) data have been combined to calculate the relative humidity with
respect to ice. 

Prior to calculating hour averages, two editing steps were applied to
the data to minimize the contribution of occasional erroneous
spikes. First absolute range limits, listed in Table 10.1, were
imposed on the data. Observations exceeding these limits were flagged
as missing. Second, a running 3-point (15 minute) median filter was
applied to the five-minute time series, which replaced the central
data point with the median of the data within the 15-minute window. If
the data within the 15-minute window are monotonically increasing or
decreasing (or constant), they are unaffected by the median
filter. However, valid maxima or minima within the window are
suppressed in the same manner as erroneous spikes, reducing the
variance of the five-minute time series. Reduction of the five-minute
variance is not expected to have a significant effect on the hour
average. 

4.0 DATA FORMAT

These data include data from all six stations in each data file.  These data have
been post-processed and are quality checked.

5.0 DATA REMARKS

Some information on the NCAR Flux-PAM stations that was taken from the
Roughness Lengths Over Snow paper: 

"At the other four SHEBA sites, we deployed portable automated mesonet
(PAM) stations-these are the flux-PAM stations from NCAR's instrument
pool (Militzer et al. 1995). These PAM stations featured either ATI or
Gill sonic anemometer/thermometers mounted at heights between 2 and 4
m above the surface. We named our first four PAM sites Atlanta,
Baltimore, Cleveland, and Florida after the teams playing in the Major
League Baseball Championship Series in the fall of 1997 while we were
building the SHEBA ice camp. The Atlanta, Baltimore, and Florida sites
lasted for the entire experiment. A pressure ridge engulfed the
Cleveland PAM station in late January 1998, and the station was
offline for several months for refurbishing. We redeployed it at a
site called Seattle in spring 1998 and, later in the summer, moved it
to Maui." 

6.0 REFERENCES
 
SHEBA FLUX-PAM Project Report - http://www.eol.ucar.edu/rtf/projects/sheba/
Sheba Atmospheric Surface Flux Group Home Page -
http://www.weather.nps.navy.mil/~psguest/sheba/index.html 
Parameterizing the Turbulent Surface Fluxes Over Summer Sea Ice paper
- http://www.esrl.noaa.gov/psd/people/ola.persson/polar_studies/conference/Andreas_8th_Polar.pdf 
Roughness Lengths Over Snow paper -
http://ams.confex.com/ams/pdfpapers/68601.pdf  

