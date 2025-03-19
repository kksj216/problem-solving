n, k = map(int, input().split())

student_x = list(map(int, input().split()))
sort_stu = sorted(student_x, reverse=True)

print(sort_stu[k-1])