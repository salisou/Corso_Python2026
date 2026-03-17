-- INT = INTERO
-- VARCHAR = TEXT => STRING  
-- NVARCHAR = TEXT => STRING => STR HA UNA LUNGHEZZA
-- DATE 
-- CHART

-- DML => Data Manipulation Language.

CREATE DATABASE ScuolaDb;


USE ScuolaDb;

/*
    create la tabella del corso
    con (
            CorsoId,
            NomeCorso,
            Crediti => intero 
    ) tutti i campi non sono nullabile
*/


-- CREAZIONE DELLA TABELLA STUDENTE
/*
CREATE TABLE IF NOT EXISTS Studente
(
    StudenteId INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
    Nome NVARCHAR(100) NOT NULL,
    Cognome NVARCHAR(100) NOT NULL,
    DataNascita DATE,
    EMAIL NVARCHAR(150) UNIQUE,
    CodiceFiscale CHAR(16) UNIQUE NOT NULL
);



CREATE TABLE Corso
(
    CorsoId INT PRIMARY KEY IDENTITY(1,1),
    NomeCorso NVARCHAR(100) NOT NULL,
    Crediti INT NOT NULL
);
*/

CREATE TABLE Docente
(
    DocenteId INT PRIMARY KEY IDENTITY(1,1),
    Nome NVARCHAR(100) NOT NULL,
    Cognome NVARCHAR(100) NOT NULL,
    Email NVARCHAR(256) UNIQUE NOT NULL,
    Telefono CHAR(13) UNIQUE NULL,
);

SELECT * FROM Docente

-- VISUALIZZAZIONE DEI DATI 
SELECT * FROM Studente;
--==========================================================================
-- Svuotare la tabella:
TRUNCATE TABLE Studente;

-- Esetta l'incrementazione 
DBCC CHECKIDENT ('Studente', RESEED, 1);
--==============================================================================
-- INSERIMENTO DEI DATI
INSERT INTO Studente 
(Nome, Cognome, DataNascita, EMAIL, CodiceFiscale)
VALUES 
('Mario', 'Rossi', '2000-05-12', 'mario.rossi@email.com', 'RSSMRA00E12H501Z'),
('Luca', 'Bianchi', '1999-11-03', 'luca.bianchi@email.com', 'BNCLCU99S03F205X'),
('Giulia', 'Verdi', '2001-02-20', 'giulia.verdi@email.com', 'VRDGLI01B60H501Y'),
('Anna', 'Ferrari', '2002-07-15', 'anna.ferrari@email.com', 'FRRNNA02L55D612T'),
('Marco', 'Romano', '1998-09-28', 'marco.romano@email.com', 'RMNMRC98P28H501U');

--==============================================================================
INSERT INTO Corso (NomeCorso, Crediti) 
VALUES
    ('Matematica', 6),  
    ('Informatica', 8),
    ('Fisica', 6),
    ('Database', 7),
    ('Programmazione', 9);

select * from Corso
--==============================================================================

INSERT INTO Docente 
    (Nome, Cognome, Email, Telefono)
Values
    ('Paola', 'Sarta', 's.paola@gmail.com', '+39321000000' ),
    ('Michele', 'Puliese', 'm.puliese@gmail.com', '+39356048565' ),


Select * from Studente


--============Concattenazione===========
select 
    Nome + ' ' + cognome as 'Nome completo dello studene',
    CodiceFiscale
from Studente

--===  StudenteId Foreign key refeferencese

CREATE TABLE Iscrizione
(
    IscrizioneId INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    StudenteId INT NOT NULL,
    CorsoId INT NOT NULL,
    DtatIscrizione Date,

    -- Definizione della chiave esterna 
    FOREIGN KEY 
);
