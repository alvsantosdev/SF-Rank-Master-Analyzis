WITH every_country_and_picks AS (

SELECT p1_home, p1_char FROM matches

UNION ALL

SELECT p2_home, p2_char FROM matches

)

SELECT p1_home, p1_char, COUNT(*) AS picks FROM every_country_and_picks

GROUP BY p1_char, p1_home;

