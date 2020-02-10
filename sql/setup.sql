CREATE DATABASE data_dashboard;

CREATE TABLE netflix_titles (
  show_id INT PRIMARY KEY NOT NULL,
  type TEXT,
  title TEXT,
  director TEXT,
  "cast" TEXT,
  country TEXT,
  date_added DATE,
  release_year INT,
  rating TEXT,
  duration TEXT,
  listed_in TEXT,
  description TEXT
);

# MYSQL

CREATE TABLE netflix_titles (
  show_id INT PRIMARY KEY NOT NULL,
  type TEXT,
  title TEXT,
  director TEXT,
  cast TEXT,
  country TEXT,
  date_added DATE,
  release_year INT,
  rating TEXT,
  duration TEXT,
  listed_in TEXT,
  description TEXT
);



LOAD DATA LOCAL INFILE  
'/Users/tabdulhakeem/Documents/Development/Coding-Interview/AmericanTireDistribution/data-dashboard-server/data/dump/netflix_titles.csv'
INTO TABLE netflix_titles  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description);

