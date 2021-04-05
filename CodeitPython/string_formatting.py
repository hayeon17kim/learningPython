year = 2021
month = 4
day = 5

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day ) + "일입니다.")


print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))

print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌게이츠"))
num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))

# 가장 오래된 방식
name = "최지웅"
age = 32
print("제 이름은 %s이고 %d살입니다." % (name, age))

# 가장 보편적인 방식
print("제 이름은 {}이고 {}살입니다.".format(name, age))

# 새로운 방식: 파이썬 3.6부터 새로 나온 방식
print(f"제 이름은 {name}이고 {age}살입니다.")