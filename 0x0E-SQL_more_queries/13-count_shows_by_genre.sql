-- Lists all genres from the hbtn_0d_tvshows and displays the number of shows linked to each
-- Can ONLY use one SELECT statement and the results must be sorted in descending order by:
-- 	number of shows linked
-- First column must be called genre
-- Second column must be called number_of_shows
-- Dont display a genre that doesn't have any shows linked
-- Database name is passed as an argument of the mysql command
SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON  tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
