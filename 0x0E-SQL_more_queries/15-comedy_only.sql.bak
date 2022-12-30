-- Uses the hbtn_0d_tvshows database to list all Comedy shows in the database 
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	tv_shows.title
-- Each record should display: tv_shows.title
-- Database name is passed as an argument of the mysql command
SELECT title
FROM tv_shows
JOIN tv_show_genres
ON  id = show_id
WHERE genre_id = (
	SELECT id
	FROM tv_genres
	WHERE name = 'Comedy'
)
ORDER BY title ASC;
