
def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    
    number_students = 0
    for entry, leave in permanence_period:
        if not (isinstance(entry, int) and isinstance(leave, int)):
            return None
        if entry <= target_time <= leave:
            number_students += 1

    return number_students
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 7
print(study_schedule(permanence_period, target_time))