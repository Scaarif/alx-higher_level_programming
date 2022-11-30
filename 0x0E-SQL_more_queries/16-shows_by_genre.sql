-- Uses the hbtn_0d_tvshows database to list all shows, and all genres linked to that show in the database 
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	tv_shows.title
-- Each record should display: tv_shows.title - tv_genres.name
-- If a show doesn't have a genre, display NULL in the genre column
-- Database name is passed as an argument of the mysql command
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON  tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;
