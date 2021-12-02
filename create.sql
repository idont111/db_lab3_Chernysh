----------------------
-- Create table book
----------------------
CREATE TABLE book(
book_id char(10) NOT NULL,
title VARCHAR(50) NOT NULL ,
author_id char(10) NOT NULL,
genre_id char(10) NOT NULL,
period_id char(3) NOT NULL
);

----------------------
-- Create table author
----------------------
CREATE TABLE author(
	author_id char(10) NOT NULL,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL
);

----------------------
-- Create table genre
----------------------
CREATE TABLE genre(
    genre_id char(10),
    genre_name VARCHAR(20)
);

----------------------
-- Create table period
----------------------
CREATE TABLE rank_period(
    period_id char(3),
    rank_period_name date NOT NULL
);

----------------------
-- Define primary keys
----------------------
ALTER TABLE book ADD CONSTRAINT PK_book PRIMARY KEY (book_id);
ALTER TABLE author ADD CONSTRAINT PK_author PRIMARY KEY (author_id);
ALTER TABLE genre ADD CONSTRAINT PK_genre PRIMARY KEY (genre_id);
ALTER TABLE rank_period ADD CONSTRAINT PK_rank_period PRIMARY KEY (period_id);
----------------------
-- Define foreign keys
----------------------
ALTER TABLE book
ADD CONSTRAINT FK_author FOREIGN KEY (author_id) REFERENCES author (author_id);
ALTER TABLE book
ADD CONSTRAINT FK_genre FOREIGN KEY (genre_id) REFERENCES genre (genre_id);
ALTER TABLE book
ADD CONSTRAINT FK_rank_period FOREIGN KEY (period_id) REFERENCES rank_period (period_id);
