-- Lists all the shows contained in the database hbtn_0d_tvshows that have at least one genre linked
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	tv_shows.title and tv_show_genres.genre_id
-- If a sho doesn't have a genre, display NULL
-- Database name is passed as an argument of the mysql command
SELECT title, genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON  id = show_id
ORDER BY title, genre_id;
-- This query is the same as a LEFT JOIN of the two tables (with the first table being tv_shows)
-- In both cases all the values (records) in tv_shows are returned and if there are no matching values
-- in the other table (tv_show_genres), NULL values are appended in their place
