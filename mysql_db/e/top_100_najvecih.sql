SET @cnt=0;
SET @cnt2=0;
SELECT A.id AS 'Rang',A.kvadratura AS 'Kuca(m2)',B.kvadratura AS 'Stan(m2)' FROM
(SELECT (@cnt := @cnt + 1)  AS id, kvadratura FROM ml_real_estate.real_estates WHERE tip_nekretnine=1 order by kvadratura desc LIMIT 100) AS A
RIGHT JOIN
(SELECT (@cnt2 := @cnt2 + 1)  AS id, kvadratura FROM ml_real_estate.real_estates WHERE tip_nekretnine=0 order by kvadratura desc LIMIT 100) AS B
ON A.id=B.id
