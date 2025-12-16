def analyze_results(marks):
    pass_count = 0
    fail_count = 0
    for i in (marks):
        if i >= 50:
            print (i,"pass")
            pass_count += 1
        else:
            print(i,"fail")
            fail_count += 1

    print("Pass :",pass_count)
    print("Fail :",fail_count)

N = int(input("Enter number of students :"))
marks =[]
for i in range(N):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

analyze_results(marks)



