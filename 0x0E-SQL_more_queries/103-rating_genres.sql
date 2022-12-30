-- Uses the hbtn_0d_tvshows_rate database to list all genres by their rating (sum)
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	the rating(sum)
-- Each record should display: tv_genres.name - rating sum
-- Database name is passed as an argument of the mysql command
SELECT name, SUM(rate) AS rating
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = genre_id
JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
-- In short: get the shows and sum of their ratings and order results
