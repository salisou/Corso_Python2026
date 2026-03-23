-- =============================================
-- Author:		MOUSSA
-- Create date: 20/03/2026
-- Description: Serve a	modificare la mail dello studente 
-- =============================================
CREATE PROCEDURE sp_UpdateEmailStudente 
	-- Add the parameters for the stored procedure here
	@StudenteId INT,
	@email NVARCHAR(150)

AS
BEGIN
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE Studente
       SET EMAIL = @email
    WHERE StudenteId = @StudenteId
END
GO
