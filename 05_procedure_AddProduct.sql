CREATE PROCEDURE AddProduct
	@Name NVARCHAR(100),
	@Category NVARCHAR(100),
	@Price DECIMAL(10, 2)
AS
BEGIN
	INSERT INTO Products (Name, Category, Price)
	VALUES (@Name, @Category, @Price);
END