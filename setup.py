from files import *
from utils import create_file
import os

print("Starting pg setup")

os.mkdir("initdb", mode=744)

create_file(".env", dotenv)
create_file("docker-compose.yml", docker_compose_yml)
create_file("initdb/01_init.sql", initdb_01_init_sql)

print("Successfuly created all files, run 'make run' to continue...")