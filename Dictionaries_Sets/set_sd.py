morning = {"Java", "C", "Ruby", "Lisp", "C#"}
afternoon = {"Python", "C#", "Java", "C", "Ruby"}

possible_courses = morning ^ afternoon
print(possible_courses)
print(morning.symmetric_difference(afternoon))
