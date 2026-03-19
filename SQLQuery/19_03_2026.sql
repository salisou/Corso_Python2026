--========= MAX, MIN, AVG, COUNT, SUM, HANVING
--========= Condizione if => Case When Then Else END Alias

--=====================AVG============================
-- 1 Restuire: la media dei voti per corso
--====================================================
Select 
	c.NomeCorso,
	AVG(e.Voto) AS 'la media dei voti' -- => Calcola la media dei voti usando la funzione AVG()
From Esame e 
Join Corso c ON c.CorsoId = e.CorsoId
GROUP BY c.NomeCorso
ORDER BY AVG(e.Voto) ASC

--===============Con il nome completo dello studente
Select 
	s.Nome + ' ' + s.Cognome AS 'Nome completo dello studente',
	c.NomeCorso,
	AVG(e.Voto) AS 'la media dei voti'
From Esame e 
Join Corso c ON c.CorsoId = e.CorsoId
JOIN Studente s On s.StudenteId = e.StudenteId
GROUP BY c.NomeCorso, s.Nome, s.Cognome
ORDER BY AVG(e.Voto) DESC

--==============Studenti senza esami
SELECT 
    s.Nome,
    s.Cognome
FROM Studente s
LEFT JOIN Esame e ON s.StudenteId = e.StudenteId
WHERE e.EsameId IS NULL;

--=====================COUNT==========================
SELECT COUNT(*) AS NRigheStudente FROM Studente
SELECT Count(*) AS NRigheEsame From Esame
SELECT Count(*) AS NRigheIscrizione From Iscrizione
SELECT Count(*) AS NRigheCorso From Corso
SELECT Count(*) AS NRigheDocente From Docente
--====================================================

--=====================MIN============================
--====================================================

--=====================MAX============================
--====================================================

--=====================SUM============================

--====================================================
--====================================================



--====================================================
--====================================================


--====================================================
--====================================================



--====================================================
--====================================================




--====================================================
--====================================================




--====================================================
--====================================================


--=============================================================
-- Restituire la lista degli Studenti sopra la media generale
--=============================================================

SELECT 
    Nome,
    Cognome,
FROM Studente
WHERE StudenteId IN (
    SELECT StudenteId
    FROM Esame
    GROUP BY StudenteId
    HAVING AVG(Voto) > (
        SELECT AVG(Voto) FROM Esame
    )
);

--====================================================
--====================================================


