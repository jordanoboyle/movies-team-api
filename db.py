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
          genre_id INTEGER,
          review_id INTEGER,
          name TEXT,
          release_year INTEGER,
          run_time INTEGER,
          image_url TEXT
          
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    movies_seed_data = [
        (1, 1, "Alien", 1979, 125, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZQxuhkEwoRCa2QzZBb7lOVhdcMPPpxDAJ2A&s"),
        (2, 2, "Tropic Thunder", 2008, 107, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKRQWm9hzGhsgGzmJx_DLvCy5vos2w4Htb4A&s"),
        (3, 3, "Team America: World Police", 2004, 98, "https://m.media-amazon.com/images/M/MV5BMTM2Nzc4NjYxMV5BMl5BanBnXkFtZTcwNTM1MTcyMQ@@._V1_.jpg"),
        (4, 4, "Borat", 2006, 84,"https://upload.wikimedia.org/wikipedia/en/3/39/Borat_ver2.jpg")
    ]
    conn.executemany(
        """
        INSERT INTO movies (genre_id, review_id, name, release_year, run_time, image_url)
        VALUES (?,?,?,?,?,?)
        """,
        movies_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()