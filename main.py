faculty_file = open("requiredCS.txt",'r')
all_class_lines = faculty_file.readlines()
for class_line in all_class_lines:
    loud_line = class_line.upper()
    class_and_name = loud_line.split(" : ")
    loud_line = loud_line.strip()
    print(class_and_name[0])
print("those are the courses you have to take")
