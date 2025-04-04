CREATE TRIGGER trg_CheckProductPrice
ON Products
INSTEAD OF INSERT
AS
BEGIN
	INSERT INTO Products (Name, Category, Price)
	SELECT Name, Category,
		CASE WHEN Price < 1 THEN 1 ELSE Price END
	FROM inserted;
END