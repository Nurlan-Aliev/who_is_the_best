start:
	uvicorn main:app --reload

redis_run:
	docker run --name some-redis -p 6379:6379 -d redis

