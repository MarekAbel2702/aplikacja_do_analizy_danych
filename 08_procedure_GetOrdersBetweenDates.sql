CREATE PROCEDURE GetOrdersBetweenDates
	@FromDate DATE,
	@ToDate DATE
AS
BEGIN
	SELECT * FROM Orders
	WHERE OrderDate BETWEEN @FromDate AND @ToDate;
END