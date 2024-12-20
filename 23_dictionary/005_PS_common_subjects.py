def common_subjects(grade1, grade2,grade3):
    if not grade1 or not grade2 or not grade3:
        return set()
    all_grades = [grade1,grade2,grade3]
    
    for grade in all_grades:
        for subject in grade.values():
            if not subject:
                return set()
                
    subjects_in_common = set.intersection(*grade1.values(), *grade2.values(), *grade3.values())
    return subjects_in_common

grade1 = {"Alice": {"Math", "English"}, "Bob": {"Math", "Science"}}
grade2 = {"Charlie": {"Math", "History"}, "David": {"Math", "English"}}
grade3 = {"Eva": {"Math", "Music"}, "Frank": {"Math", "Science"}}
grade4 = {}
grade5 = {"Gina": {}, "Hank": {"History"}}   
print(common_subjects(grade1, grade2, grade3))  # Output: {"Math"}
print(common_subjects(grade1, grade2, grade4))  # Output: set()