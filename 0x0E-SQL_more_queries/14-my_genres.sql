-- Uses the hbtn_0d_tvshows database to list all genres of the show Dexter
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	the genre name
-- Each record should display: tv_genres.name
-- Database name is passed as an argument of the mysql command
SELECT name
FROM tv_genres
JOIN tv_show_genres
ON  id = genre_id
WHERE show_id = (
	SELECT id
	FROM tv_shows
	WHERE title = 'Dexter'
)
ORDER BY name ASC;
