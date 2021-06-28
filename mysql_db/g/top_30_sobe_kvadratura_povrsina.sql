SET @cnt=0;
SET @cnt1=0;
SET @cnt2=0;
SELECT A.id AS 'Rang',A.broj_soba AS 'Broj soba',A.kvadratura AS 'Kvadratura(m2)',B.povrsina_zemljista AS 'Povrsina zemljista(m2)' FROM
(SELECT A.id ,A.broj_soba ,B.kvadratura FROM
(SELECT (@cnt := @cnt + 1)  AS id, broj_soba FROM ml_real_estate.real_estates order by broj_soba desc LIMIT 30) AS A
RIGHT JOIN
(SELECT (@cnt1 := @cnt1 + 1)  AS id, kvadratura FROM ml_real_estate.real_estates WHERE tip_nekretnine=0 order by kvadratura desc LIMIT 30) AS B
ON A.id=B.id) AS A
RIGHT JOIN
(SELECT (@cnt2 := @cnt2 + 1)  AS id, povrsina_zemljista FROM ml_real_estate.real_estates WHERE tip_nekretnine=1 order by povrsina_zemljista desc LIMIT 30) AS B
ON A.id=B.id