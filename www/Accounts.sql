CREATE TABLE account {
	username VARCHAR(30) UNIQUE PRIMARY KEY
	password VARCHAR(100)
	salt varchar(100)
	Fname VARCHAR
	LName VARCHAR
	email VARCHAR 
	DOB DATE
	gender CHAR(1)
	FavGame VARCHAR
}
