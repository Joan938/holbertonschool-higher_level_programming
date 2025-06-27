-- Use the tv_shows, tv_genres, and tv_show_genres tables to find the genres of the TV show Dexter. Your query should return the genre names in alphabetical order.
SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;