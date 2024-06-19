"""Example queries for movies sample database."""

import sqlite3


def get_conn():
    # Connect to the SQLite database
    return sqlite3.connect("movies.db")


class Movie:
    """A movie."""

    def __init__(self, movie_id):
        """Queries the database for the movie_id."""
        with get_conn() as conn:
            cur = conn.cursor()
            # Get the Movie attributes
            cur.execute("SELECT * FROM movie WHERE id = ?", (movie_id,))
            row = cur.fetchone()
            self.id = row[0]
            self.created_time = row[1]
            self.rank = row[2]
            self.url = row[3]
            self.name = row[4]
            self.rating = row[5]
            self.date = row[6]
            self.duration = row[7]
            self.category = row[8]
            self.description = row[9]
            self.director = row[10]
            self.writers = row[11]
            self.stars = row[12]
            self.is_completed = row[13]

    @classmethod
    def find_by_name(cls, movie_name):
        """Queries the database for the movie_name."""
        with get_conn() as conn:
            cur = conn.cursor()
            # Get the Movie attributes
            cur.execute("SELECT * FROM movie WHERE name LIKE ?", ('%' + movie_name + '%',))
            rows = cur.fetchall()
            if not rows:
                return None
            movies = [cls(row[0]) for row in rows]
            return movies

    def __str__(self):
        return f"{self.id}: {self.name} directed by {self.director}"

if __name__ == "__main__":
    print(Movie(1))