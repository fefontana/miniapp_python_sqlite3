BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "personas" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "personas" VALUES (1,'Jose','josecode@sistem.com');
INSERT INTO "personas" VALUES (2,'Sol','sjs@ar.com');
INSERT INTO "personas" VALUES (3,'Carlos','carlosadmin@sistem.com');
INSERT INTO "personas" VALUES (5,'Issac','iturletti@hitech.ar');
INSERT INTO "personas" VALUES (6,'Raquel','raquii22@gmail.com');
INSERT INTO "personas" VALUES (7,'Fede','femto@unrc.edu');
INSERT INTO "personas" VALUES (8,'Agustina','agus1980@hotmail.com');
COMMIT;
