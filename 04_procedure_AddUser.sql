CREATE PROCEDURE AddUser
	@Name NVARCHAR(100),
	@Email NVARCHAR(100),
	@RegistrationDate DATE
AS
BEGIN
	INSERT INTO Users (Name, Email, RegistrationDate)
	VALUES (@Name, @Email, @RegistrationDate);
END