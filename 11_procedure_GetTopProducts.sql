CREATE PROCEDURE GetTopProducts
	@TopN INT
AS
BEGIN
	SELECT TOP(@TopN) p.Name, SUM(o.Quantity) AS TotalSold
	FROM Orders o
	JOIN Products p ON o.ProductID = p.ID
	GROUP BY p.Name
	ORDER BY TotalSold DESC;
END