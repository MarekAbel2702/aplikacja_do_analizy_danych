CREATE TRIGGER trg_AutoSetRegDate
ON Users
INSTEAD OF INSERT
AS
BEGIN
	INSERT INTO Users(Name, Email,RegistrationDate)
	SELECT Name, Email,
		ISNULL(RegistrationDate, GETDATE())
	FROM inserted
END