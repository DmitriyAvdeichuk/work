import sqlite3

with sqlite3.connect('books.db') as table_books:
    cursor = table_books.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS books
                                            (bookID integer ,name text)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS authors
                                            (authorID integer ,author text)""")
    cursor.execute("""INSERT INTO books VALUES(1,'война и мир')""")
    cursor.execute("""INSERT INTO books VALUES(2, 'мёртвые души')""")
    cursor.execute("""INSERT INTO books VALUES(3,'преступление и накзаание')""")
    cursor.execute("""INSERT INTO books VALUES(4,'идиот')""")
    cursor.execute("""INSERT INTO authors VALUES(1,'толстой')""")
    cursor.execute("""INSERT INTO authors VALUES(2,'гоголь')""")
    cursor.execute("""INSERT INTO authors VALUES(3,'достоевский')""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS m2m_books_authors
                                    (book_ID int, author_ID int, 
                                    FOREIGN KEY(book_ID) REFERENCES books(bookID),
                                    FOREIGN KEY(author_ID) REFERENCES  authors(authorID)) """)
    cursor.execute("""INSERT INTO m2m_books_authors VALUES(1,1)""")
    cursor.execute("""INSERT INTO m2m_books_authors VALUES(2,2)""")
    cursor.execute("""INSERT INTO m2m_books_authors VALUES(3,3)""")
    cursor.execute("""INSERT INTO m2m_books_authors VALUES(4,3)""")
    cursor.execute('SELECT*FROM m2m_books_authors')
    print(cursor.fetchall())
    table_books.commit()
