CREATE TABLE IF NOT EXISTS "tweet_db" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"content"	TEXT NOT NULL,
	"time"	INTEGER,
	"location"	TEXT,
	"likes"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "users" (
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT,
    "cookie" TEXT,
    "salt" TEXT
);
