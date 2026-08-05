SELECT p1_char, p2_char, p1_result, p2_result, p1_mr, p2_mr FROM matches
WHERE p1_char != p2_char AND p1_mr >= 1800 AND p2_mr >= 1800
ORDER BY p1_mr DESC;