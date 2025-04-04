CREATE TRIGGER trg_AfterInsertUser
ON Users
AFTER INSERT
AS
BEGIN
	PRINT 'Nowy u¿ytkownik dodany!'
END