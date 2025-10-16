run:
	docker compose up -d

stop:
	docker compose down

restart:
	docker compose restart

logs:
	docker logs -f pg_min

down-delete:
	docker compose down -v

setup:
	python3 ./setup.py

