SELECT lokacija1, COUNT(*) FROM ml_real_estate.real_estates GROUP BY lokacija1 ORDER BY COUNT(*) DESC;