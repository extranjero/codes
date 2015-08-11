package main

import (
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
	"github.com/rubenv/sql-migrate"

	"log"
)

func main() {

	db, err := sqlx.Connect("postgres", "host=localhost user=root password=root dbname=acl sslmode=disable")

	if err != nil {
		log.Fatal("db connect error: ", err)
	}

	migrations := &migrate.FileMigrationSource{
		Dir: "migrations",
	}

	n, err := migrate.Exec(db.DB, "postgres", migrations, migrate.Up)

	if err != nil {
		log.Fatal("Migration error:", err)
	}

	log.Printf("Applied %d migration \n", n)

}
