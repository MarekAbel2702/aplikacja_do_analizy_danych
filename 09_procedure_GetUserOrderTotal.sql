CREATE PROCEDURE GetUserOrderTotal
	@UserID INT
AS
BEGIN
	SELECT SUM(p.Price * o.Quantity) AS TotalSpent
	FROM Orders o 
	JOIN Products p ON o.ProductID = p.ID
	WHERE o.UserID = @UserID;
END