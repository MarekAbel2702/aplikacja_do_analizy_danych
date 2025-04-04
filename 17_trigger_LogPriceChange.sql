CREATE TRIGGER trg_LogPriceChange
ON Products
AFTER UPDATE
AS
BEGIN
	IF UPDATE(Price)
	BEGIN
		PRINT 'Cena produktu zosta�a zmieniona.'
	END
END