-- Uses the hbtn_0d_tvshows database to list all tv shows that are NOT in the comedy genre
-- Can ONLY use a max of 2 SELECT statements and the results must be sorted in ascending order by:
-- 	tv_shows.title
-- Each record should display: tv_shows.title
-- Database name is passed as an argument of the mysql command
SELECT title
FROM tv_shows
WHERE title NOT IN (
	SELECT title FROM tv_shows
	JOIN tv_show_genres ON tv_shows.id = show_id
	JOIN tv_genres ON genre_id = tv_genres.id
	WHERE name = 'Comedy'
)
ORDER BY title ASC;
-- In short: get the shows linked to the Comedy gemre and return shows NOT IN the result (noon-comedy shows)
