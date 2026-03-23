--== Implementazione degli strore procedur
EXEC sp_GetAllStudenti;
EXEC sp_GetStudenteById 30;
EXEC sp_GetStudenteByName 'Marco';
EXEC sp_InsertStudente 'Pippo', 'Bobbo', '2000-11-20', 'b.pippo@gmail.com', 'PIBBWNA02L45D612P';
EXEC sp_UpdateEmailStudente 30, 'l.emanuele26@gmail.com'
EXEC sp_VotoStudentiSopraMedia;
EXEC sp_VotiSopraMedia;
-- linke
SELECT * FROM Studente WHERE Nome LIKE 'A%';
SELECT * FROM Studente WHERE CodiceFiscale LIKE '%P';
SELECT * FROM Studente WHERE Cognome LIKE '%P%';

--=== IN 
SELECT * FROM Studente WHERE StudenteId IN (1,2,20, 30,5) ORDER BY StudenteId DESC;


--== Contare esame sopra la media
CREATE PROCEDURE sp_VotiSopraMedia
AS
BEGIN
	SELECT 
		e.StudenteId,
		COUNT(*) AS 'Numero esame sopra la media',
		AVG(e.Voto) AS Media
	FROM Esame e
	GROUP BY e.StudenteId
	HAVING AVG(e.Voto) > 
	(
		SELECT AVG(Voto) FROM Esame
	)
END;
SELECT @@SERVERNAME -- MOUSSA\LOCALDB#AAC8E731
SELECT @@VERSION -- Microsoft SQL Server 2025 (RTM) - 17.0.1000.7 (X64)   Oct 21 2025 12:05:57   Copyright (C) 2025 Microsoft Corporation  Express Edition (64-bit) on Windows 10 Home 10.0 <X64> (Build 26200: ) (Hypervisor) 