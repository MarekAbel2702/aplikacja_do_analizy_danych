CREATE TRIGGER trg_InfoDeleteProduct
ON Products
AFTER DELETE
AS
BEGIN
	PRINT 'Produkt zosta� usuni�ty.'
END