<<<<<<< HEAD
import random

print("난수의 최댓값을 구합니다.")

count = int(input("난수의 개수를 입력하세요: "))
mini = int(input("난수의 최솟값을 입력하세요: "))
maxx = int(input("난수의 최댓값을 입력하세요: "))

l = [] * count
print(l)
for _ in range(count): l.append(random.randint(mini, maxx))
print(l)
print("최댓값은", max(l))
=======
import random

print("난수의 최댓값을 구합니다.")

count = int(input("난수의 개수를 입력하세요: "))
mini = int(input("난수의 최솟값을 입력하세요: "))
maxx = int(input("난수의 최댓값을 입력하세요: "))

l = [] * count
print(l)
for _ in range(count): l.append(random.randint(mini, maxx))
print(l)
print("최댓값은", max(l))
>>>>>>> 2d8319d170ef6f026fca7327b39a71e5297cfca9
