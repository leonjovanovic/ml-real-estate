SET @cnt=0;
SET @cnt2=0;
SELECT A.id AS 'Rang',A.cena AS 'Kuca(€)',B.cena AS 'Stan(€)' FROM
(SELECT (@cnt := @cnt + 1)  AS id, cena FROM ml_real_estate.real_estates WHERE tip_nekretnine=1 AND tip_ponude=0 order by cena desc LIMIT 30) AS A
RIGHT JOIN
(SELECT (@cnt2 := @cnt2 + 1)  AS id, cena FROM ml_real_estate.real_estates WHERE tip_nekretnine=0 AND tip_ponude=0 order by cena desc LIMIT 30) AS B
ON A.id=B.id
