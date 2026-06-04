import numpy as np

print('Below are the scores of ten students in five subjects in order: English, Math, Science, Udu, Islamiyat')
print()                         # LEAVE ONE LINE. FOR BETTER READIBILITY

# GENERATING THE SCORES USING random.randint
np.random.seed(42)              # FOR REPRODUCIBILITY OF SAME RANDOM NUMBERS
student_scores = np.random.randint(0, 101, (10,5))
print(student_scores)
print()

# COMPUTING MEAN, MAX, MIN PER STUDENT AND PER SUBJECT

# OPERATIONS FOR STUDENTS
student_mean = np.mean(student_scores, axis=1)
student_max = np.max(student_scores, axis=1)
student_min = np.min(student_scores, axis=1)
print(f'Mean score for all students: {student_mean}')
print(f'Max score for all students: {student_max}')
print(f'Min score for all students: {student_min}')


print()
# OPERATIONS FOR SUBJECTS
subject_mean = np.mean(student_scores, axis=0)
subject_max = np.max(student_scores, axis=0)
subject_min = np.min(student_scores, axis=0)
print(f'Mean score for all subjects: {subject_mean}')
print(f'Max score for all subjects: {subject_max}')
print(f'Min score for all subjects: {subject_min}')
print()

# FLAG STUDENTS WHO SCORED BELOW 50 IN ANY EXAM
flag = np.any(student_scores < 50, axis=1)
flag_indices = np.where(flag)                       # FOR GETTING THE ROW INDICES OF STUDENTS WHO SCORED BELOW
print(flag_indices[0])                              # FOR GETTING FIRST VALUE FROM RETURNED TUPPLE
print()

# NORMALIZING ALL SCORES TO A 0-1 SCALE
normalized = np.round((student_scores - student_scores.min()) / (student_scores.max() - student_scores.min()), 2)
print(normalized)
