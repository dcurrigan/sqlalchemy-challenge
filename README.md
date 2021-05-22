# sqlalchemy-challenge
Week 10 SQLAlchemy Homework

> Created by Dale Currigan  
> May 2021  
  
![SQL](EmployeeSQL/static/surfs-up.png)    

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
  
*Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do...  
*Step 1 - Climate Analysis and Exploration*  
   *- Precipitation Analysis*  
   *- Station Analysis*  
*Step 2 - Climate App*  
*Bonus: Other Recommended Analyses*  
   *- Temperature 1*  
   *- Temperature 2*  
   *- Daily Rainfall Average*  
  
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
The Entity Relationship Diagram (ERD) below describes the structure and relationship present in the database:  

![SQL](EmployeeSQL/static/surfs-up.png)  
  
To perform the queries below the database can be establised as follows:  
1. Create a new Database in PostgreSQL  
2. Create tables using table schemata in the 'schema.sql' file 
3. Import the csv files into  the tables from the data folder  
    **Note:** Due to the foreign keys described in the schema, the csv's should be imported in the folllowing order:  
              (1) departments.csv --> (2) titles.csv --> (3) employees.csv --> (4) dept_emp.csv -->  (5) dept_manager.csv --> (6)) salaries.csv
5. Run queries from the 'Data Analysis.sql' file  
  
The 'Bonus' section of the homework can be loaded from the SQL-Analysis.ipynb notebook   
  
**NOTE:** This notebook requires the users **PostgreSQL username and password** to be loaded into the **config.py** file in order to load the engine  
  
  
# Analysis  
  
**Question 1:** List the following details of each employee: employee number, last name, first name, sex, and salary   

![SQL](EmployeeSQL/Output/question_1.png)  

**Question 2:** List first name, last name, and hire date for employees who were hired in 1986.

![SQL](EmployeeSQL/Output/question_2.png)  

**Question 3:** List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name. 
  
![SQL](EmployeeSQL/Output/question_3.png)   
   
**Question 4:** List the department of each employee with the following information: employee number, last name, first name, and department name. 
  
![SQL](EmployeeSQL/Output/question_4.png)  

**Question 5:** List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B." 

![SQL](EmployeeSQL/Output/question_5.png)  

**Question 6:** List all employees in the Sales department, including their employee number, last name, first name, and department name. 

![SQL](EmployeeSQL/Output/question_6.png)  

**Question 7:** List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name. 

![SQL](EmployeeSQL/Output/question_7.png)  

**Question 8:** In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

![SQL](EmployeeSQL/Output/question_8.png)  

**Question 9:** Create a histogram to visualize the most common salary ranges for employees.

![SQL](EmployeeSQL/Output/salary_histogram.png)  
There is a skewed distribution of salaries with most employees earning on salaries on the lower end of the scale  
  
  
**Question 10:** Create a bar chart of average salary by title.
  
![SQL](EmployeeSQL/Output/salary_query.png)  
  
![SQL](EmployeeSQL/Output/avg_salary_title.png)  
'Staff' and 'Senior Staff' make on average considerably more than employees with other titles

  
**Question 11 - Epilogue:** Evidence in hand, you march into your boss's office and present the visualization. With a sly grin, your boss thanks you for your work. On your way out of the office, you hear the words, "Search your ID number." You look down at your badge to see that your employee ID number is 499942.

I see...  
  
![SQL](EmployeeSQL/Output/my_id.png)  

    
# Contributors  
- [@dcurrigan](https://github.com/dcurrigan) - <dcurrigan@gmail.com>


## Status
Project is: 
````diff 
+ Completed
````
