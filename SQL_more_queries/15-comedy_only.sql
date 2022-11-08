-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title

FROM tv_shows

INNER JOIN tv_show_genres
	ON title.id = tv_show_id

INNER JOIN tv_genres
	ON tv_genre.id = title.genre_id 

WHERE tv_genre.name = "Comedy"
ORDER BY title ASC;
