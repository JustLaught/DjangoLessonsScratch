import redis

r = redis.Redis(
    host='redis-12589.c281.us-east-1-2.ec2.cloud.redislabs.com',
    port=12589,
    username="Test",
    password='Qwer12-='
)

# r.set("ostap", 300)
# print(r.get("ostap"))

# r.mset({"key5": "Hello :3"})
# data = r.mget(["key1", "key2", "key3", "key4", "key5"])
# print(data)

# r.set("counter", 1)
# r.incr("counter")
# r.incrby("counter", 5)
# print(r.get("counter"))

#[1, 2, 3, 4]
# r.lpush("list1", 1)
# push left
# for i in range(2, 10):
#     r.rpush('list1', i)
# while r.llen("list1") > 0:
#     elem = r.lpop("list1")
#     print(elem)
# print(r.llen("list1"))

# for i in  range(5):
#     r.rpush("list2", i)
# for i in range (8, 13):
#     r.rpush("list3", i)

# r.lmove("list2", "list3", "LEFT", "RIGHT")
 
# while r.llen("list2") > 0:
#     elem = r.lpop("list2")
#     print(elem, end=" ")

# print()

# while r.llen("list3") > 0:
#     elem = r.lpop("list3")
#     print(elem, end=" ")