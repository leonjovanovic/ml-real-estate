SELECT
(SELECT COUNT(*) FROM ml_real_estate.real_estates WHERE uknjizenost=1 AND tip_nekretnine=1) AS 'Uknjizene kuce', 
(SELECT COUNT(*) FROM ml_real_estate.real_estates WHERE uknjizenost=0 AND tip_nekretnine=1) AS 'Neuknjizene kuce', 
(SELECT COUNT(*) FROM ml_real_estate.real_estates WHERE uknjizenost=1 AND tip_nekretnine=0) AS 'Uknjizeni stanovi', 
(SELECT COUNT(*) FROM ml_real_estate.real_estates WHERE uknjizenost=0 AND tip_nekretnine=0) AS 'Neuknjizene stanovi'