run:
	docker compose up -d

stop:
	docker compose down

restart:
	docker compose restart

logs:
	docker logs -f pg_min

down-delete:
	docker compose down --volumes --rmi all

clean:
	rm -rf __pycache__ .env initdb docker-compose.yml .passwords

setup:
	python3 ./setup.py

