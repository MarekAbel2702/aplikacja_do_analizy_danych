CREATE PROCEDURE GetDailySales
AS
BEGIN
	SELECT OrderDate, SUM(p.Price * o.Quantity) AS Total
	FROM Orders o
	JOIN Products p ON o.ProductID = p.ID
	GROUP BY OrderDate
	ORDER BY OrderDate;
END