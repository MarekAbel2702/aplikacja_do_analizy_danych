CREATE PROCEDURE UpdateProductPrice
	@ProductID INT,
	@NewPrice DECIMAL(10, 2)
AS
BEGIN
	UPDATE Products
	SET Price = @NewPrice
	WHERE ID = @ProductID;
END