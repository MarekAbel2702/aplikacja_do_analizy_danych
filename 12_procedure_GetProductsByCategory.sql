CREATE PROCEDURE GetProductsByCategory
	@Category NVARCHAR(100)
AS
BEGIN
	SELECT * FROM Products
	WHERE Category = @Category;
END