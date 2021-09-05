## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


#### Database Schema
This is the schema of the database

How to read the schema: 
* If the field is bold this means that is a primary key 
* Blue lines denote the relationships between each entity 


<img src="erd-diagram.png" alt="ERD Diagram" width="800"/>


The core of this schema is defined by the songplays table which contains foreign keys to four tables;
* start_time
* user_id
* song_id
* artist_id

--------------------------------------------



#### Project structure

Create a custom user called `student` with password `student` and create a database called `sparkifydb` after installing the database

Run these commands in order to start the project: <br><br>
<I> This script will create the tables and must be runned first </I> <br>
`` create_tables.py`` <br>

<I> This script will run the ETL process </I> <br>
`` etl.py`` <br>


* <b> data/log_data </b> - This folder contains JSON files and are used to populate the core table Song Plays and to populate the Dimension tables for Users and Time.
* <b> data/song_data </b> -  This folder contains JSON files and contains metadata about a song and the artist of that song adn are thus used to populate dimension tables for Songs and Artists.
* <b> erd-diagram </b> - Picture of Schema
* <b> etl.ipynb </b> - Jupyter Python 3 notebook that helps to explore and test the ETL process
* <b> test.ipynb </b> - Jupyter Python 3 notebook to test if data loaded 
* <b> create_tables.py </b> - This script will drop old tables (if exist) ad re-create new tables
* <b> etl.py </b> - This Jupyter Python 3 script reads in and inserts the Log and Song data files into the database.
* <b> sql_queries.py </b> - This Jupyter Python 3 script with all the SQL statements required to build the ETL process
* <b> Create_tables_sql_queiries_etl.ipynb </b> - This Jupyter Python 3 script runs the create_tables.py, sql_queiries.py & etl.py scripts defined above


