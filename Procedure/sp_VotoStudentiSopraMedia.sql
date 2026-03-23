-- =============================================
-- Author:		MOUSSA
-- Create date: 20/03/2026
-- Description:	Restituisce la lista degli Studenti sopra la media generale
-- =============================================
CREATE PROCEDURE sp_VotoStudentiSopraMedia
	AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT 
        Nome,
        Cognome
    FROM Studente
    WHERE StudenteId IN (
        SELECT StudenteId
        FROM Esame
        GROUP BY StudenteId
        HAVING AVG(Voto) > (
            SELECT AVG(Voto) FROM Esame
        )
    );
END
GO
