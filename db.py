import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS movies;
        """
    )
    conn.execute(
        """
        CREATE TABLE movies (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          release_year INTEGER,
          run_time INTEGER,
          image_url TEXT
          
        );
        """
    )
    conn.commit()
    print("movies table created successfully")

    conn.execute(
        """
        DROP TABLE IF EXISTS reviews;
        """
    )
    conn.execute(
        """
        CREATE TABLE reviews (
          id INTEGER PRIMARY KEY NOT NULL,
          movie_id INTEGER,
          user_id INTEGER,
          title TEXT,
          body TEXT,
          rating INTEGER         
        );
        """
    )
    conn.commit()
    print("reviews table created successfully")

    movies_seed_data = [
        ("Alien", 1979, 125, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZQxuhkEwoRCa2QzZBb7lOVhdcMPPpxDAJ2A&s"),
        ("Tropic Thunder", 2008, 107, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKRQWm9hzGhsgGzmJx_DLvCy5vos2w4Htb4A&s"),
        ("Team America: World Police", 2004, 98, "https://m.media-amazon.com/images/M/MV5BMTM2Nzc4NjYxMV5BMl5BanBnXkFtZTcwNTM1MTcyMQ@@._V1_.jpg"),
        ("Borat", 2006, 84,"https://upload.wikimedia.org/wikipedia/en/3/39/Borat_ver2.jpg")
    ]

    conn.executemany(
        """
        INSERT INTO movies (name, release_year, run_time, image_url)
        VALUES (?,?,?,?)
        """,
        movies_seed_data,
    )
    conn.commit()
    print("movies seed data created successfully")

    reviews_seed_data = [
        (1, 1, "Blew Chunks", "I lost my lunch it was so gross and scary.", 7),
        (1, 2, "Rofl copter down", "I fell out of my chair laughing it was so funny", 9),
        (2, 1, "I was not amused", "Why all the offensive jokes. What's wrong with knock knock?", 2),
        (3, 2, "Could I borrow a feeling", "Could you lend me your glove of love. Hearting hearts need some healing", 4),
    ]
    conn.executemany(
        """
        INSERT INTO reviews (movie_id, user_id, title, body, rating)
        VALUES (?,?,?,?,?)
        """,
        reviews_seed_data,
    )
    conn.commit()
    print("reviews seed data created successfully")

    conn.close()

def movies_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM movies
        """
    ).fetchall()
    return [dict(row) for row in rows]

def movies_create(name, release_year, run_time, image_url):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO movies (name, release_year, run_time, image_url)
        VALUES (?, ?, ?, ?)
        RETURNING *
        """,
        (name, release_year, run_time, image_url),
    ).fetchone()
    conn.commit()
    return dict(row)

def movies_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM movies
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)

def movies_update_by_id(id, name, release_year, run_time, image_url):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE movies SET name = ?, release_year = ?, run_time = ?, image_url = ?
        WHERE id = ?
        RETURNING *
        """,
        (name, release_year, run_time, image_url, id),
    ).fetchone()
    conn.commit()
    return dict(row)

def movies_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from movies
        WHERE id = ?
        """,
        (id,),
    )
    conn.commit()
    return {"message": "Movie destroyed successfully"}

if __name__ == "__main__":
    initial_setup()
    