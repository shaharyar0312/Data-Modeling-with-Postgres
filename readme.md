<h1>Introduction</h1>
Sparkify, music startup needs to analyze the data for the informed decisions which will directly help them to grow their business thourgh their user's trends.
Through this database we can add more value to the business of sparkify through user location, what type of artist user like whcih directly help sparkify to do personalized marketing and give user a personalized experience.

<h1>Database schema design</h1>
The purpose is to create dimensional model using star schema to optimize the data reading capabilty and to have a benefits of denormalization. 

- Following is the Star Schema of my data model

[![N|Solid](ERD.png)]


<h1>Files description </h1>

- test.ipynb displays the first few rows of each table to let you check your database.
- create_tables.py drops and creates tables. Run this file to reset tables before each time we run ETL scripts.
- etl.ipynb reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
- etl.py reads and processes files from song_data and log_data and loads them into your tables.
- sql_queries.py contains all the sql queries containing creation and insertion of tables.
- README.md provides description of Project

<h1>Dimension Model and ETL Process </h1>

In this project, 1 fact and 4 dimension tables have modeled and ETL process is created through PostgrSQL and python. 

- Fact Table
* (songplays) table is created from log data directory and some dimensions linked with songplays

- Dimension Tables
* (users) table is created from log directory which contain features of users who are using sparkify app
* (songs) table is created form song directory and artist dimension which contain songs in music database
* (artists) table is created from song directory which contain artists information who sing a songs
* (time) table contain timestamps records which came from transformation of existing column ts

<h2>ETL Workflow:</h2>

- ETL Design is simplified, first step to read json files from source (song_data and log_data) and extract specific columns and after little transformation dimensions and facts tables are populated.

<h2>Project Workflow</h2>

- first run create_tables.py file which create all the tables on terminal through
```sh
python create_tables.py
```
- second step is to run etl.py file which contain all etl jobs thorugh
```sh
python etl.py
```
- in this way data is loaded

