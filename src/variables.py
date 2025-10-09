# variables.py

# this class serves as a data structure for storing each student's information
# an instance of this class represents one student's complete survey response
class StudentData:
    def __init__(self, email, study_hours, timestamp, department,
                 high_school_specialty, work_or_study, motivation,
                 expectations_alignment, sufficient_information,
                 transition_difficulty, academic_load, content_relevance,
                 teaching_methodology, effective_methodologies,
                 more_practical_activities, study_life_balance,
                 anxiety_stress, wellness_resources, considered_dropping_out,
                 considered_changing_major, student_input_responses):
        
        self.email = email
        self.study_hours = study_hours
        self.timestamp = timestamp
        self.department = department
        self.high_school_specialty = high_school_specialty
        self.work_or_study = work_or_study
        self.motivation = motivation
        self.expectations_alignment = expectations_alignment
        self.sufficient_information = sufficient_information
        self.transition_difficulty = transition_difficulty
        self.academic_load = academic_load
        self.content_relevance = content_relevance
        self.teaching_methodology = teaching_methodology
        self.effective_methodologies = effective_methodologies
        self.more_practical_activities = more_practical_activities
        self.study_life_balance = study_life_balance
        self.anxiety_stress = anxiety_stress
        self.wellness_resources = wellness_resources
        self.considered_dropping_out = considered_dropping_out
        self.considered_changing_major = considered_changing_major
        self.student_input_responses = student_input_responses