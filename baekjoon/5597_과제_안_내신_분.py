import sys

input = sys.stdin.readline

students = {}

num = 30

for i in range(num):
    students[i+1] = 1

for _ in range(num-2):
    submit = int(input())
    del students[submit]

# print(students)

answer = sorted(students)

for i in answer:
    print(i)