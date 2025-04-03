CREATE PROCEDURE AddOrder
	@UserID INT,
	@ProductID INT,
	@Quantity INT,
	@OrderDate DATE
AS
BEGIN
	INSERT INTO Orders (UserID, ProductID, Quantity, OrderDate)
	VALUES (@UserID, @ProductID, @Quantity, @OrderDate);
END