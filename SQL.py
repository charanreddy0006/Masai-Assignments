import sqlite3
import pandas as pd

# SQL approach
sql_query = """
SELECT
    t.name AS track_name,
    ar.name AS artist_name,
    g.name AS genre_name,
    SUM(il.quantity) AS total_quantity
FROM invoice_lines AS il
INNER JOIN tracks  AS t  ON il.track_id  = t.track_id
INNER JOIN albums  AS al ON t.album_id   = al.album_id
INNER JOIN artists AS ar ON al.artist_id = ar.artist_id
INNER JOIN genres  AS g  ON t.genre_id   = g.genre_id
GROUP BY
    t.track_id,
    t.name,
    ar.name,
    g.name
ORDER BY total_quantity DESC;
"""

def build_report(tracks, albums, artists, genres, invoice_lines):
    """
    Build the sales report using Pandas INNER JOINs.
    """

    # Rename columns to avoid collisions
    tracks_df = tracks.rename(columns={"name": "track_name"})
    artists_df = artists.rename(columns={"name": "artist_name"})
    genres_df = genres.rename(columns={"name": "genre_name"})

    # Merge invoice_lines with tracks
    merged_df = pd.merge(
        invoice_lines,
        tracks_df,
        on="track_id",
        how="inner"
    )

    # Merge with albums
    merged_df = pd.merge(
        merged_df,
        albums,
        on="album_id",
        how="inner"
    )

    # Merge with artists
    merged_df = pd.merge(
        merged_df,
        artists_df,
        on="artist_id",
        how="inner"
    )

    # Merge with genres
    merged_df = pd.merge(
        merged_df,
        genres_df,
        on="genre_id",
        how="inner"
    )

    # Aggregate total quantity sold
    report = (
        merged_df
        .groupby(
            ["track_id", "track_name", "artist_name", "genre_name"],
            as_index=False
        )["quantity"]
        .sum()
        .rename(columns={"quantity": "total_quantity"})
        .sort_values(by="total_quantity", ascending=False)
    )

    # Select final columns
    report = report[
        ["track_name", "artist_name", "genre_name", "total_quantity"]
    ]

    return report


if __name__ == "__main__":

    # Connect to SQLite database
    conn = sqlite3.connect("chinook.db")

    # Execute SQL query
    sql_result = pd.read_sql_query(sql_query, conn)

    print("SQL Result:")
    print(sql_result)

    # Load tables into DataFrames
    tracks = pd.read_sql_query("SELECT * FROM tracks", conn)
    albums = pd.read_sql_query("SELECT * FROM albums", conn)
    artists = pd.read_sql_query("SELECT * FROM artists", conn)
    genres = pd.read_sql_query("SELECT * FROM genres", conn)
    invoice_lines = pd.read_sql_query("SELECT * FROM invoice_lines", conn)

    # Execute Pandas solution
    pandas_result = build_report(
        tracks,
        albums,
        artists,
        genres,
        invoice_lines
    )

    print("\nPandas Result:")
    print(pandas_result)

    # Close connection
    conn.close()