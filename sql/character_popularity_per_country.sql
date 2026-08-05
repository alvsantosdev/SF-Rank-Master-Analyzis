WITH chars_country AS (

SELECT p1_home, p1_char FROM matches

UNION ALL

SELECT p2_home, p2_char FROM matches

)

SELECT p1_home, p1_char,
COUNT(*) AS picks FROM chars_country

GROUP BY p1_home, p1_char;
