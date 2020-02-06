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
