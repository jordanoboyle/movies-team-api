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
        DROP TABLE IF EXISTS genres;
        """
    )
    conn.execute(
        """
        DROP TABLE IF EXISTS users;
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

    conn.execute(
        """
        DROP TABLE IF EXISTS genres;
        """
    )
    conn.execute(
        """
        CREATE TABLE genres (
        id INTEGER PRIMARY KEY NOT NULL,
        movie_id INTEGER,
        genre_name TEXT
        );
        """
    )

    conn.commit()
    print("genres table created successfully")

    genres_seed_data = [
        (1, "Comedy",),
        (2, "Sci-Fi",),
        (1, "Romance",),
        (3, "Drama",),
        (1, "Thriller",),
        (4, "Action",)
    ]

    conn.executemany(
        """
        INSERT INTO genres (movie_id, genre_name)
        VALUES (?, ?)
        """,
        genres_seed_data,
    )
    conn.commit()
    print("genres seed data created successfully")

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

    conn.execute(
        """
        CREATE TABLE users (
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT,
        email TEXT,
        password TEXT,
        password_digest TEXT
        );
        """
    )
    conn.commit()
    print("users table created successfully")

    users_seed_data = [
        ("bob", "bob@email.com", "password"),
        ("alex", "alex@email.com", "password"),
        ("tony", "tony@email.com", "password"),
        ("joe", "joe@email.com", "password"),
    ]

    conn.executemany(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        users_seed_data,
    )
    conn.commit()
    print("users seed data created successfully")

    conn.close()

# MOVIES Table Connections
def movies_all():
    conn = connect_to_db()
    rows = conn.executemany(
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
# SELECT genres.name, movies.image_url
#         FROM genres
#         JOIN movies ON genres.movie_id = movies.id
# SELECT * FROM genres
#Genre Table Connections
def genres_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM genres
        """
    ).fetchall()
    return [dict(row) for row in rows]

def genres_create(movie_id, genre_name):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO genres (movie_id, genre_name)
        VALUES (?, ?)
        RETURNING *
        """,
        (movie_id, genre_name,),
    ).fetchone()
    conn.commit()
    return dict(row)

def genres_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM genres
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)

def genres_update_by_id(id, movie_id, genre_name):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE genres SET movie_id = ?, genre_name = ?
        WHERE id = ?
        RETURNING *
        """,
        (movie_id, genre_name, id),
    ).fetchone()
    conn.commit()
    return dict(row)
    
def genres_destroy_by_id(id):
    conn = connect_to_db()
    conn.execute(
        """
        DELETE from genres
        WHERE id = ?
        """,
        (id,)
    )
    conn.commit()
    return {"message": "Genre removed"}

# REVIEWS Table Connections
def reviews_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT reviews.title, reviews.body, reviews.rating, movies.name
        FROM reviews
        JOIN movies ON reviews.movie_id = movies.id
        """
    ).fetchall()
    return [dict(row) for row in rows]

def reviews_create(movie_id, user_id, title, body, rating):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO reviews (movie_id, user_id, title, body, rating)
        VALUES (?, ?, ?, ?, ?)
        RETURNING *
        """,
        (movie_id, user_id, title, body, rating),
    ).fetchone()
    conn.commit()
    return dict(row)

def reviews_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT reviews.title, reviews.body, reviews.rating, movies.name
        FROM reviews
        JOIN movies ON reviews.movie_id = movies.id
        WHERE reviews.id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)

def reviews_update_by_id(id, movie_id, user_id, title, body, rating):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE reviews SET movie_id = ?, user_id = ?, title = ?, body = ?, rating = ?
        WHERE id = ?
        RETURNING *
        """,
        (movie_id, user_id, title, body, rating, id),
    ).fetchone()
    conn.commit()
    return dict(row)

def reviews_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from reviews
        WHERE id = ?
        """,
        (id,),
    )
    conn.commit()
    return {"message": "Review destroyed successfully"}

# USERS Table Connections
def users_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM users
        """
    ).fetchall()
    return [dict(row) for row in rows]

def users_create(name, email, password):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (name, email, password),
    ).fetchone()
    conn.commit()
    return dict(row)

def users_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM users
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)

def users_update_by_id(id, name, email, password):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE users SET name = ?, email = ?, password = ?
        WHERE id = ?
        RETURNING *
        """,
        (name, email, password, id),
    ).fetchone()
    conn.commit()
    return dict(row)

def users_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from users
        WHERE id = ?
        """,
        (id,),
    )
    conn.commit()
    return {"message": "User destroyed successfully"}

if __name__ == "__main__":
    initial_setup()
    