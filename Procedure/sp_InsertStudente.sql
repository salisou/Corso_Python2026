
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Moussa
-- Create date: 20/03/2026
-- Description:	Gestisce l'inserimento di uno studente
-- =============================================
CREATE PROCEDURE sp_InsertStudente
	-- Add the parameters for the stored procedure here
	@Nome nvarchar(100),
    @Cognome nvarchar(100),
    @DataNascita date,
    @EMAIL nvarchar(150),
    @CodiceFiscale char(16)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO [dbo].[Studente]
           (Nome
           ,Cognome
           ,DataNascita
           ,EMAIL
           ,CodiceFiscale)
     VALUES
           (@Nome,
            @Cognome,
            @DataNascita,
            @EMAIL,
            @CodiceFiscale);
END
GO 