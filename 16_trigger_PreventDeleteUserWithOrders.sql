CREATE TRIGGER trg_PreventDeleteUserWithOrders
ON Users
INSTEAD OF DELETE
AS
BEGIN
	IF EXISTS (
		SELECT 1 FROM Orders WHERE UserID IN (SELECT ID FROM deleted)
	)
	BEGIN 
		RAISERROR('Nie mo¿na usun¹æ u¿ytkownika z zamówieniami.', 16, 1)
		ROLLBACK
	END
	ELSE
	BEGIN 
		DELETE FROM Users WHERE ID IN(SELECT ID FROM deleted)
	END
END