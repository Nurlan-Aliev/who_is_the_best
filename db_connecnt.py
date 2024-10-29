from redis import Redis

database = Redis(host="localhost", port=6379, decode_responses=True)


def grow_count(name):
    count = int(database.get(name) if database.get(name) else 0)
    count += 1
    database.set(name, count)
