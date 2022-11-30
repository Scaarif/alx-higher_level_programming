-- Lists all the shows contained in the database hbtn_0d_tvshows that have at least one genre linked
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	tv_shows.title and tv_show_genres.genre_id
-- Database name is passed as an argument of the mysql command
SELECT title, genre_id
FROM tv_shows
FULL JOIN tv_show_genres
ON  id = show_id
ORDER BY title, genre_id;
