-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title

FROM tv_shows

INNER JOIN tv_show_genres
	ON title.id = tv_show_id

INNER JOIN tv_genres
	ON tv_genres.id = title.genre_id 

WHERE name = "Comedy"
ORDER BY tv_shows.title ASC;
