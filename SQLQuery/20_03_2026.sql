--== Implementazione degli strore procedur
EXEC sp_GetAllStudenti;
EXEC sp_GetStudenteById 30;
EXEC sp_GetStudenteByName 'Marco';
EXEC sp_InsertStudente 'Pippo', 'Bobbo', '2000-11-20', 'b.pippo@gmail.com', 'PIBBWNA02L45D612P';
EXEC sp_UpdateEmailStudente 30, 'l.emanuele26@gmail.com'
 

-- linke
SELECT * FROM Studente WHERE Nome LIKE 'A%';
SELECT * FROM Studente WHERE CodiceFiscale LIKE '%P';
SELECT * FROM Studente WHERE Cognome LIKE '%P%';

--=== IN 
SELECT * FROM Studente WHERE StudenteId IN (1,2,20, 30,5) ORDER BY StudenteId DESC;



