CREATE DATABASE IF NOT EXISTS library;
USE library;
CREATE TABLE IF NOT EXISTS author (
  authorID INT PRIMARY KEY,
    author_name VARCHAR(30)
);
CREATE TABLE IF NOT EXISTS book (
  bookID INT PRIMARY KEY,
    book_name VARCHAR(45)
);
INSERT INTO author VALUES  ('1', 'Толстой');
INSERT INTO author VALUES ('2', 'Достоевский');
INSERT INTO author VALUES ('3', 'Гоголь');
INSERT INTO author VALUES ('4', 'Есенин');
INSERT INTO author VALUES ('5', 'Лермонтов');
INSERT INTO book VALUES ('1', 'Война и Мир');
INSERT INTO book VALUES ('2', 'Мертвые души');
INSERT INTO book VALUES ('3', 'Преступление и наказание');
INSERT INTO book VALUES ('4', 'Идиот');
INSERT INTO book VALUES ('5', 'Сборник стихов');
INSERT INTO book VALUES ('6', 'Теремок');
CREATE TABLE IF NOT EXISTS m2m_book_author(
  id_author INT ,
    id_book INT ,
    FOREIGN KEY (id_author) REFERENCES author(authorID),
	FOREIGN KEY (id_book) REFERENCES  book(bookID));
INSERT INTO m2m_book_author VALUES ('1', '1');
INSERT INTO m2m_book_author VALUES ('2', '3');
INSERT INTO m2m_book_author VALUES ('2', '4');
INSERT INTO m2m_book_author VALUES ('3', '2');
INSERT INTO m2m_book_author VALUES ('4', '5');
INSERT INTO m2m_book_author VALUES ('5', '5');
