Purpose of this Database:

Sparkify, music startup may wants to analyze the data for the informed decisions which will directly help them to grow their business thourgh their user trends.
Through this database we add more value to the business of sparkify through user location, what type of artist user like whcih directly help sparkify to do personalized marketing and give user a personalized experience.

The purpose is to create dimensional model using star schema to optimize the data reading capabilty and to have a benefits of denormalization. 


Project Description

In this project, 1 fact and 4 dimension tables have modeled and ETL process is created through PostgrSQL and python. 

- Fact Table
* (songplays) table is created from log data directory and some dimensions linked with songplays

- Dimension Tables
* (users) table is created from log directory which contain features of users who are using sparkify app
* (songs) table is created form song directory and artist dimension which contain songs in music database
* (artists) table is created from song directory which contain artists information who sing a songs
* (time) table contain timestamps records which came from transformation of existing column ts

ETL Workflow:

- ETL Design simplified first step to read json files from source and extract specific columns and after little transformation dimensions and facts tables are populated.

Project Workflow:
- first create_tables.py run on terminal which create all the tables
- then etl.py file will be run which contain all etl jobs
- in this data is loaded

