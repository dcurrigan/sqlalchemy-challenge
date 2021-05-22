# sqlalchemy-challenge
Week 10 SQLAlchemy Homework

> Created by Dale Currigan  
> May 2021  
  
![SQL](/static/surfs-up.png)    

## Table of contents  
* [Project Intro](#Project-Intro)  
* [Project Structure](#Project-Structure)  
* [Setup](#Setup)  
* [Analysis](#Analysis)  
* [Contributors](#Contributors)  
* [Status](#Status)  

# Project Intro
This project covers the week 10 SQLAlchemy homework project - Surfs Up!
  
The project briefing was as follows:  
  
*Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area.* 

The project includes the following elements:  
   - Precipitation Analysis  
   - Station Analysis  
   - Flask Climate App  
   - Additional Bonus Analyses:  
        - Temperature 1  
        - Temperature 2  
        - Daily Rainfall Average  
  
# Project Structure  
```
sqlalchemy-challenge   
|  
|    
|__ Climate Analysis.ipynb                # Jupyter Notebook for the project
|__ app.py                                # Flask server 
|__ README.md                             # This file 
|
|__ Resources/                            # Hawaii climate database files  
|   |__ hawaii.sqlite                    
|   |__ hawaii_measurement.csv 
|   |__ hawaii_stations.csv
|
|__ templates/     
|      |__ welcome.html                   # HTML template for the climate app homepage  
|
|__ static/     
|      |__ surfs-up.png                   # Image folder for rendering to homepage   
|     
|__ Output/                               # Plots generated by jupyter notebook   
|      |__ climate_app.png
|      |__ daily_normals.png
|      |__ daily_trip_temps.png
|      |__ precipitaion.png
|      |__ temp_histogram.png
|      |__ trip_temps.png
``` 
  
# Setup 
  
* Open Climate Analysis.ipynb as a Jupyter Notebook  
* Once opened, Select *Restart & Run All* from Kernel menu  
* The Notebook can now be navigated using the links to observe the data analysis  
  
* Run app.py with the commond 'python app.py' from the terminal
* Instructions for navigating the routes are found on the home page   
  
  
# Analysis  
  
### Precipitation Analysis    
Analysis of daily precipitation readings from all stations for the last 12 months showed that rainfail was fairly unpredicatable and occured throughout the year without any clear patterns regarding time of year where it was of lesser or greater amount. 
  
![SQL](/Output/precipitation.png)  

### Station Analysis 
The Waihee 837.5 Station had the greatest number of temperature observations with 2772. In the data for this station the Min temp (F) was 54, Max temp (F) was 85, and Average temp (F) was 71.66. A histogram of this stations temperature data for 12 months from 23/8/2016-2017 showed an approximate normal distribution:

![SQL](/Output/temp_histogram.png)  

### Climate App  
Results of Analyses are available in JSON format via Climate App  
  
  ![SQL](/Output/climate_app.png) 
   
### Temperature Analysis 1: Is there a statistically significant difference in temperatures between June and Decemeber?   
  
Analysis revealed an avaerage temperature in June across all years of74.94 degrees F, and 71.04 degrees F for December. An independent sample T-test revealed a P-value of 3.9025129038616655e-191, suggesting temeperatures between June and Decemebr have a statistitically significant differrence.   
  
An unpaired test was used, as whilst the groups contain measurements of the same thing (Hawaii temperatures), there are different numbers of measurements present in each
group, so the measurements are not truly 'paired' and are rather independent sets.  
   
### Temperature Analysis 2    

An analysis was carried out with respect to my hypothetical holiday over the dates **11/04/18 - 25/04/18**  
  
Based on the previous years data the average Min temp (F) was 67, Max temp (F) was 83, and Average temp (F) was 73.8 during this time period.

![SQL](/Output/trip_temps.png) 
  
![SQL](/Output/daily_trip_temps.png) 

### Daily Rainfall Average  
A plot of the the daily normals for each day of the trip, based on the previous years data can be seen beloew:  
  
![SQL](/Output/daily_normals.png)  


    
# Contributors  
- [@dcurrigan](https://github.com/dcurrigan) - <dcurrigan@gmail.com>


## Status
Project is: 
````diff 
+ Completed
````
