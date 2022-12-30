-- Uses the hbtn_0d_tvshows_rate database to list all tv shows by their rating (sum)
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by:
-- 	the rating(sum)
-- Each record should display: tv_shows.title - rating sum
-- Database name is passed as an argument of the mysql command
SELECT title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON id = show_id
GROUP BY show_id
ORDER BY rating DESC;
-- In short: get the shows and sum of their ratings and order results
