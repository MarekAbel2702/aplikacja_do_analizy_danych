BEGIN TRY
	BEGIN TRANSACTION 

	INSERT INTO Users (Name, Email, RegistrationDate)
	VALUES
	('Anna Kowalska', 'anna@example.com', '2023-01-10'),
	('Jan Nowak', 'jan@example.com', '2023-02-15'),
	('Katarzyna Wiœniewska', 'kasia@example.com', '2023-03-01'),
	('Marek Zaj¹c', 'marek@example.com', '2023-03-20'),
	('Pawe³ Wójcik', 'pawel@example.com', '2023-04-05'),
	('Magdalena Krawczyk', 'magda@example.com', '2023-04-10');

	INSERT INTO Products (Name, Category, Price)
	VALUES
	('Laptop', 'Elektronika', 3500),
	('Myszka', 'Elektronika', 100),
	('Monitor', 'Elektronika', 900),
	('Krzes³o', 'Meble', 300),
	('Biurko', 'Meble', 800),
	('Zeszyt', 'Papiernicze', 10),
	('D³ugopis', 'Papiernicze', 5),
	('S³uchawki', 'Elektronika', 250),
	('Lampka biurkowa', 'Oœwietlenie', 120);

	INSERT INTO Orders (UserID, ProductID, Quantity, OrderDate)
	VALUES
	(1, 1, 1, '2023-03-01'),
	(2, 2, 2, '2023-03-02'),
	(1, 4, 1, '2023-03-05'),
	(3, 5, 1, '2023-03-06'),
	(4, 3, 2, '2023-03-10'),
	(2, 6, 5, '2023-03-15'),
	(5, 7, 10, '2023-03-18'),
	(6, 8, 1, '2023-03-20'),
	(4, 9, 1, '2023-03-22'),
	(3, 2, 1, '2023-03-25'),
	(5, 1, 1, '2023-03-27'),
	(1, 6, 3, '2023-03-30');

	COMMIT TRANSACTION
END TRY
BEGIN CATCH
	PRINT ERROR_MESSAGE();
	ROLLBACK TRANSACTION
END CATCH