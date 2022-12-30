-- Uses the hbtn_0d_tvshows database to list all genres NOT linked to that show 'Dexter'
-- Can ONLY use a max of 2 SELECT statements and the results must be sorted in ascending order by:
-- 	tv_genres.name
-- Each record should display: tv_genres.name
-- Database name is passed as an argument of the mysql command
SELECT name
FROM tv_genres
WHERE name NOT IN (
	SELECT name FROM tv_genres
	JOIN tv_show_genres ON tv_genres.id = genre_id
	JOIN tv_shows ON show_id = tv_shows.id
	WHERE title = 'Dexter'
)
ORDER BY name ASC;
-- In short: get the genres linked to Dexter show and return genres NOT IN the result (linked genres)
