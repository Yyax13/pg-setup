from files import *
from utils import create_file
import os

print("Starting pg setup")

os.mkdir("initdb", mode=0o777)

create_file(".env", dotenv)
create_file("docker-compose.yml", docker_compose_yml)
create_file("initdb/01_init.sql", initdb_01_init_sql)

print(f"Created with PG_PASS \"{POSTGRES_PASSWORD}\" and app_user password: \"{APP_USER_PASS}\"")
print("Successfuly created all files, run 'make run' to continue...")