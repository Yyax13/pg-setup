from utils import gen_tag

POSTGRES_PASSWORD = gen_tag()
APP_USER_PASS = gen_tag()

dotenv = f"""
PG_PASS='{POSTGRES_PASSWORD}'
"""

docker_compose_yml = """
services:
    postgres:
        image: postgres:16-alpine
        container_name: pg_min
        environment:
            POSTGRES_PASSWORD: ${PG_PASS}

        ports:
            - "0.0.0.0:55432:5432"

        volumes:
            - pgdata:/var/lib/postgresql/data
            - ./initdb:/docker-entrypoint-initdb.d:ro

        restart: always


volumes:
    pgdata:

"""

initdb_01_init_sql = f"""
create database app_db;

create role app_user with
    login
    password '{APP_USER_PASS}'
    nosuperuser
    nocreatedb
    nocreaterole
    nologin inherit
    noreplication
    nobypassrls
;

\\connect app_db

create schema if not exists app;

revoke all on schema public from public;

grant usage on schema app to app_user;

alter default privileges in schema app
    grant select, insert, update, delete on tables to app_user;

alter default privileges in schema app
    grant usage, select on sequences to app_user;

alter default privileges in schema app
    grant execute on functions to app_user;

"""