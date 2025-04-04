CREATE TRIGGER trg_NewOrderInfo
ON Orders
AFTER INSERT
AS
BEGIN
	PRINT 'Dodano nowe zamówienie.'
END