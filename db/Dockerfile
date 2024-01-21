FROM postgres:latest

COPY init.sql /docker-entrypoint-initdb.d/
COPY pg_hba.conf /var/lib/postgresql/pg_hba.conf
COPY postgresql.conf /var/lib/postgresql/postgresql.conf

