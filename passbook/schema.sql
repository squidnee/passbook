drop table if exists User;
drop table if exists Category;
drop table if exists Credential;
drop table if exists WalletCredential;
create table User (
	UserID INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL,
	Email TEXT NOT NULL,
	Password TEXT NOT NULL,
	Manager BOOLEAN,
	Auth BOOLEAN,
	Date_Created DATETIME,
	Date_Updated DATETIME,
	Date_Accessed DATETIME,
	Trusted_By TEXT,
	Trusts TEXT,
	UNIQUE(UserID, Date_Created)
);
create table Category (
	EntryID INTEGER PRIMARY KEY AUTOINCREMENT,
	Category_Name TEXT,
	FOREIGN KEY(EntryID) REFERENCES Credential(EntryID)
);
create table Credential (
	EntryID INTEGER AUTOINCREMENT,
	Name TEXT,
	Owner TEXT,
	Username TEXT,
	Password TEXT,
	Password_Hash TEXT,
	Category TEXT,
	Website TEXT,
	Description TEXT,
	Notes TEXT,
	Tags TEXT,
	Email TEXT,
	Expiration_Date DATE,
	Version INTEGER,
	Starred BOOLEAN,
	Reprompt BOOLEAN,
	Date_Created DATETIME,
	Date_Updated DATETIME,
	Date_Accessed DATETIME,
	UNIQUE(EntryID, Date_Created),
	FOREIGN KEY(Owner) REFERENCES User(Name),
	FOREIGN KEY(Category) REFERENCES Category(Category_Name)
);
create table WalletCredential (
	EntryID INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT,
	Owner TEXT,
	Category TEXT,
	Card_Number INTEGER,
	Card_Type TEXT,
	Name_On_Card TEXT,
	Secret_Code INTEGER,
	Expiration_Date DATE,
	Zip_Code INTEGER,
	Description TEXT,
	Notes TEXT,
	Starred BOOLEAN,
	Date_Created DATETIME,
	Date_Updated DATETIME,
	Date_Accessed DATETIME,
	UNIQUE(EntryID, Date_Created),
	FOREIGN KEY(Owner) REFERENCES User(Name),
	FOREIGN KEY(Category) REFERENCES Category(Category_Name)
);