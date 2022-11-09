-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title

FROM tv_shows

INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id

INNER JOIN tv_genres
	ON tv_genres.genre_id = tv_genres_id 

WHERE tv_genre.name = "Comedy"

ORDER BY tv_shows.title ASC;
