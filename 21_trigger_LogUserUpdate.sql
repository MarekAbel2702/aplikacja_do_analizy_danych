CREATE TRIGGER trg_LogUserUpdate
ON Users
AFTER UPDATE
AS
BEGIN
	PRINT 'Dane u�ytkownika zosta�y zmienione.'
END