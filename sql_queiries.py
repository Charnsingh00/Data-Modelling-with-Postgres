# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES
songplay_table_create = ("""CREATE TABLE songplays(
songplay_id SERIAL,
start_time TIMESTAMP REFERENCES time(start_time),
user_id VARCHAR(50) REFERENCES users(user_id),
level VARCHAR(50),
song_id VARCHAR(100) REFERENCES songs(song_id),
artist_id VARCHAR(100) REFERENCES artists(artist_id),
session_id BIGINT,
location VARCHAR(255),
user_agent TEXT,
PRIMARY KEY (songplay_id)) """)

user_table_create = ("""CREATE TABLE users(
user_id VARCHAR,
firstName VARCHAR(255),
lastName VARCHAR(255),
gender VARCHAR(1),
level VARCHAR(50),
PRIMARY KEY (user_id)) """)

song_table_create = ("""CREATE TABLE songs(
song_id VARCHAR(100),
title VARCHAR(255),
artist_id VARCHAR(100),
year INTEGER,
duration DOUBLE PRECISION,
PRIMARY KEY (song_id)) """)

artist_table_create = ("""CREATE TABLE artists(
artist_id VARCHAR(100),
name VARCHAR(255),
location VARCHAR(255),
latitude DOUBLE PRECISION,
longitude DOUBLE PRECISION,
PRIMARY KEY (artist_id)) """)

