CREATE TRIGGER trg_MaxOrderQuantity
ON Orders
INSTEAD OF INSERT 
AS
BEGIN
	IF EXISTS (
		SELECT 1 FROM inserted WHERE Quantity > 100
	)
	BEGIN
		RAISERROR('Nie mo�na zam�wi� wi�cej ni� 100 sztuk.', 16, 1)
		ROLLBACK
	END
	ELSE
	BEGIN
		INSERT INTO Orders(UserID, ProductID, Quantity, OrderDate)
		SELECT UserID, ProductID, Quantity, OrderDate FROM inserted
	END
END