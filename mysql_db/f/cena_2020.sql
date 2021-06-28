SET @cnt=0;
SELECT (@cnt := @cnt + 1)  AS Rang, cena AS Cena FROM ml_real_estate.real_estates WHERE godina_izgradnje=2020 order by cena desc