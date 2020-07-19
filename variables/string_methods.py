course = "Python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course)

print(course.lower().find("Pro".lower()))

print(course.lower().replace("p","j").title())

print("pro" in course) # boolean
print("mming" not in course) # boolean
