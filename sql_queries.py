# DROP TABLES

songplay_table_drop = "drop  table if exists songplays"
user_table_drop = "drop  table if exists users"
song_table_drop = "drop  table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists  time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays( 
                            songplay_id serial primary key ,
                            start_time TIMESTAMP not null,
                            user_id  int  not null, 
                            level VARCHAR NOT NULL,
                            song_id varchar not null, 
                            artist_id varchar  not null,
                            session_id int not null,
                            location varchar,
                            user_agent varchar);""")

user_table_create = ("""create table if not exists users (
                            user_id  INT PRIMARY KEY,
                            first_name  VARCHAR,
                            last_name  VARCHAR,
                            gender  CHAR(1),
                            level VARCHAR NOT NULL)""")


song_table_create = ("""create table if not exists songs (
                            song_id varchar  PRIMARY KEY,
                            title  VARCHAR,
                            artist_id  varchar not null,
                            year INT CHECK (year >= 0),
                            duration FLOAT)""")

artist_table_create = ("""create table if not exists artists (
                            artist_id varchar PRIMARY KEY,
                            name VARCHAR,
                            location VARCHAR,
                            latitude DECIMAL(9,6),
                            longitude DECIMAL(9,6))""")

time_table_create = ("""create table if not exists time (
                            start_time  TIMESTAMP PRIMARY KEY,
                            hour INT ,
                            day INT ,
                            week INT,
                            month INT ,
                            year INT ,
                            weekday VARCHAR NOT NULL)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (
                            songplay_id,
                            start_time,
                            user_id,
                            level,
                            song_id,
                            artist_id, 
                            session_id,
                            location,
                            user_agent)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT(songplay_id) DO NOTHING;
                            """)

user_table_insert = ("""INSERT INTO users (
                            user_id,
                            first_name,
                            last_name,
                            gender,
                            level) VALUES (%s, %s, %s, %s, %s) 
                            ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level 
                            """)

song_table_insert = ("""INSERT INTO songs (
                            song_id,
                            title,
                            artist_id,
                            year,
                            duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists (
                            artist_id,
                            name,
                            location,
                            latitude,
                            longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (
                            start_time,
                            hour,
                            day,
                            week,
                            month,
                            year,
                            weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""          SELECT 
                            b.song_id,
                            b.artist_id 
                            FROM
                            songs b
                            JOIN artists a
                            on b.artist_id = a.artist_id
                            WHERE b.title = %s
                            AND a.name = %s
                            AND b.duration = %s""")

# QUERY LISTS

create_table_queries = [ user_table_create,  artist_table_create, song_table_create,time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
