-- Christopher Springer
-- 10/29/26

USE sakila;

SELECT AVG(rental_rate) FROM film;

SELECT title, rental_rate, ROUND(rental_rate) AS rounded_rate
FROM film;

SELECT rental_id,
       rental_date,
       CAST(rental_date AS DATE) AS rental_day,
       CAST(rental_date AS TIME) AS rental_time
FROM rental
LIMIT 10;

SELECT title,
       CONVERT(rental_rate, CHAR) AS rate_as_text,
       CAST(rental_duration AS DECIMAL(5,2)) AS duration_decimal,
       CAST(rental_rate AS SIGNED) AS rate_as_integer
FROM film
LIMIT 10;

SELECT film_id,
       CONV(film_id, 10, 2)  AS binary_id,
       CONV(film_id, 10, 16) AS hex_id
FROM film
WHERE film_id IN (10, 255);
SELECT CAST(4.39 AS SIGNED);

SELECT customer_id,
       CONCAT_WS(' ', first_name, last_name)  AS full_name,
       CONCAT_WS(', ', last_name, first_name) AS directory_name,
       LOWER(email) AS clean_email
FROM customer
LIMIT 10;

SELECT title,
       SUBSTRING(title, 1, 3)  AS first_three,
       LOWER(title)            AS lower_title,
       REPLACE(title, ' ', '_') AS file_name,
       REVERSE(title)          AS backwards
FROM film
LIMIT 10;

SELECT TRIM('   Sakila   ')                      AS trimmed,
       INSERT('ACADEMY DINOSAUR', 1, 7, 'MUSEUM') AS inserted,
       STRCMP('ALIEN', 'ZORRO')                   AS compare_1,
       STRCMP('ACE', 'ACE')                       AS compare_2,
       FORMAT(1234567.891, 2)                     AS formatted;
       
SELECT first_name,
       CONCAT(UPPER(SUBSTRING(first_name, 1, 1)),
              LOWER(SUBSTRING(first_name, 2))) AS proper_first
FROM customer
LIMIT 10;

SELECT rental_id,
       rental_date,
       DATE(rental_date)      AS rental_day,
       DAYNAME(rental_date)   AS weekday,
       DAYOFWEEK(rental_date) AS weekday_number,
       DAYOFYEAR(rental_date) AS day_of_year,
       QUARTER(rental_date)   AS quarter
FROM rental
LIMIT 10;

SELECT r.rental_id,
       r.rental_date,
       r.return_date,
       DATEDIFF(r.return_date, r.rental_date) AS days_kept,
       f.rental_duration,
       DATE_ADD(r.rental_date, INTERVAL f.rental_duration DAY) AS due_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
LIMIT 10;

SELECT r.rental_id,
       r.rental_date,
       r.return_date,
       DATEDIFF(r.return_date, r.rental_date) AS days_kept,
       f.rental_duration,
       DATE_ADD(r.rental_date, INTERVAL f.rental_duration DAY) AS due_date
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
LIMIT 10;

SELECT payment_id,
       payment_date,
       DATE_FORMAT(payment_date, '%M %d, %Y')         AS report_date,
       DATE_FORMAT(payment_date, '%m/%d/%Y %h:%i %p') AS us_format,
       DATE_SUB(payment_date, INTERVAL 1 MONTH)       AS one_month_earlier
FROM payment
LIMIT 10;

SELECT CURDATE(), CURTIME(), CURRENT_TIMESTAMP;
SELECT DATEDIFF(curdate(),rental_date) From rental;

-- Part D
SELECT rental_id,
       rental_date,
       IFNULL(return_date, 'Not returned') AS return_status
FROM rental
WHERE return_date IS NULL;

SELECT COUNT(*) AS total_rentals,
       SUM(ISNULL(return_date)) AS not_returned
FROM rental;

SELECT title,
       original_language_id,
       language_id,
       COALESCE(original_language_id, language_id) AS display_language
FROM film
LIMIT 10;

SELECT COUNT(*) AS all_films,
       COUNT(NULLIF(rental_rate, 0.99)) AS films_not_099
FROM film;

SELECT IFNULL(rental_id, 'No rental linked') AS no_linked_rentals
FROM payment
WHERE rental_id IS NULL;

SELECT COUNT(*) FROM payment
WHERE rental_id IS NULL;

SELECT * FROM payment
WHERE payment_id IN (1, 424, 7011, 10840, 14675, 15458);

-- Part E: Numeric Functions
SELECT title,
       replacement_cost,
       rental_rate,
       replacement_cost / rental_rate               AS raw_ratio,
       ROUND(replacement_cost / rental_rate, 2)     AS rounded,
       CEILING(replacement_cost / rental_rate)      AS rentals_to_break_even,
       FLOOR(replacement_cost / rental_rate)        AS floored,
       TRUNCATE(replacement_cost / rental_rate, 1)  AS truncated
FROM film
LIMIT 10;

SELECT title,
       rental_rate,
       ROUND(rental_rate - (SELECT AVG(rental_rate) FROM film), 2)
           AS diff_from_avg,
       ABS(ROUND(rental_rate - (SELECT AVG(rental_rate) FROM film), 2))
           AS distance_from_avg
FROM film
LIMIT 10;

SELECT MOD(film_id, 2) AS even_or_odd, COUNT(*) AS films
FROM film
GROUP BY MOD(film_id, 2);

SELECT title, rental_rate,
       GREATEST(rental_rate, 2.99) AS price_with_2_99_minimum
FROM film
LIMIT 10;

SELECT LEAST(4.99, 2.99, 0.99), POW(2, 10), SQRT(144), ROUND(PI(), 4);

-- Five random films (run it twice)
SELECT title FROM film ORDER BY RAND() LIMIT 5;


-- Guided practice
-- G1
SELECT customer_id, concat_ws(', ', last_name, first_name) as full_name, LOWER(email) as email
FROM customer
ORDER BY last_name;

-- G2: July had the most rentals with 6709.
SELECT COUNT(*) AS 'rentals', DATE_FORMAT(rental_date, '%M') AS 'month'
FROM rental
GROUP BY DATE_FORMAT(rental_date, '%M');

-- G3: The film was returned on time
SELECT r.rental_date, date_add(r.rental_date, INTERVAL f.rental_duration DAY) AS 'due date' , r.return_date
FROM rental r
JOIN inventory i
ON r.inventory_id = i.inventory_id
JOIN film f
ON i.film_id = f.film_id
WHERE rental_id = 1; 

-- G4
SELECT rental_id, IFNULL(return_date, 'Not returned') AS 'return status'
FROM rental;
SELECT COUNT(return_date) AS 'Not Returned'
FROM rental
WHERE return_date IS NULL;
