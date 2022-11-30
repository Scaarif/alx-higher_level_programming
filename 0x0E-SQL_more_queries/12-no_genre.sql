-- Lists all the shows contained in the database hbtn_0d_tvshows without a genre linked
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	tv_shows.title and tv_show_genres.genre_id
-- Note: in this case, the show's a genre is NULL
-- Database name is passed as an argument of the mysql command
SELECT title, genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON  id = show_id
WHERE show_id IS NULL
ORDER BY title, genre_id;
