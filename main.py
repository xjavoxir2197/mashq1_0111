# 1 - misol
tuple1 = (1, 15, 25, 19)
print(sum(tuple1))

# 2 - misol
tuple2 = (1, 2, 3, 4, 5)
print(max(tuple2))

# 3 - misol
tuple3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple3[::-1])

# 4 - misol
tuple4 = (1, 2, 3, 4, 5)
res = tuple(map(lambda x: x * 2, tuple4))
print(res)

# 5 - misol
tuple5 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
res = tuple(filter(lambda x: x % 2 == 0, tuple5))
print(res)
