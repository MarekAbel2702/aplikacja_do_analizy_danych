CREATE TRIGGER trg_AfterInsertUser
ON Users
AFTER INSERT
AS
BEGIN
	PRINT 'Nowy użytkownik dodany!'
END