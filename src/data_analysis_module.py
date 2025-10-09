# data_analysis_module.py

import pandas as pd
import numpy as np

def calculate_statistics(data):
    """Calculates aggregate statistics for various data categories."""
    df = pd.DataFrame(data[1:], columns=data[0])

    print("Available columns:", df.columns.tolist())

    # --- CATEGORY 1: INITIAL EXPECTATIONS AND MOTIVATION ---
    if 'expectations_alignment' in df.columns:
        expectations = df['expectations_alignment'].astype(float)
        motivations = df['motivation']

        mean_expectations = expectations.mean()
        median_expectations = expectations.median()
        motivation_distribution = motivations.value_counts()

        print("\nCategory 1: Initial Expectations and Motivation")
        print(f"Mean of expectations alignment: {mean_expectations:.2f}")
        print(f"Median of expectations alignment: {median_expectations:.2f}")
        print("\nDistribution of Motivations:")
        print(motivation_distribution)
    else:
        print("Column 'expectations_alignment' not found in the data.")

    # --- CATEGORY 2: ADAPTATION TO THE UNIVERSITY ENVIRONMENT ---
    if all(col in df.columns for col in ['transition_difficulty', 'academic_load', 'study_life_balance']):
        transition = df['transition_difficulty'].astype(float)
        academic_load = df['academic_load'].astype(float)
        balance = df['study_life_balance'].astype(float)

        mean_transition = transition.mean()
        mean_academic_load = academic_load.mean()
        mean_balance = balance.mean()

        # check correlation between academic load and study-life balance
        correlation = np.corrcoef(academic_load, balance)[0, 1]

        print("\nCategory 2: Adaptation to the University Environment")
        print(f"Mean of transition difficulty: {mean_transition:.2f}")
        print(f"Mean of academic load perception: {mean_academic_load:.2f}")
        print(f"Mean of study-life balance: {mean_balance:.2f}")
        print(f"Correlation between academic load and balance: {correlation:.2f}")
    else:
        print("Missing required columns for the adaptation category.")

    # --- CATEGORY 3: SATISFACTION WITH THE CURRICULUM ---
    if all(col in df.columns for col in ['content_relevance', 'effective_methodologies']):
        content_satisfaction = df['content_relevance'].astype(float)
        mean_satisfaction = content_satisfaction.mean()

        print("\nCategory 3: Satisfaction with the Curriculum")
        print(f"Mean of content satisfaction: {mean_satisfaction:.2f}")

    # --- CATEGORY 4: WELL-BEING AND BALANCE ---
    if all(col in df.columns for col in ['study_life_balance', 'anxiety_stress', 'wellness_resources']):
        wellbeing = df['study_life_balance'].astype(float)
        stress = df['anxiety_stress'].astype(float)

        mean_wellbeing = wellbeing.mean()
        mean_stress = stress.mean()

        print("\nCategory 4: Well-being and Balance")
        print(f"Mean of emotional well-being: {mean_wellbeing:.2f}")
        print(f"Mean of study-related stress: {mean_stress:.2f}")

    # --- CATEGORY 5: RETENTION AND MAJOR CHANGE CONSIDERATION ---
    if all(col in df.columns for col in ['considered_dropping_out', 'considered_changing_major']):
        dropouts = df['considered_dropping_out'].value_counts()
        changes = df['considered_changing_major'].value_counts()

        print("\nCategory 5: Retention and Major Change Consideration")
        print(f"Number of students who considered dropping out: {dropouts}")
        print(f"Number of students who considered changing majors: {changes}")

# generates recommendations based on a student's responses
def generate_recommendations(data):
    recommendations = []
    
    # extract relevant data points by index (note: this is fragile)
    work_study_status = data[3]
    study_hours = data[4]
    motivation = data[5]
    expectations_alignment = int(data[6])
    sufficient_information = int(data[7])
    transition_difficulty = int(data[8])
    academic_load_comfort = int(data[9])
    teaching_style = data[10]
    teaching_method = data[11]
    effective_methodologies = int(data[12])
    desire_for_practical_activities = int(data[13])
    life_balance = int(data[14])
    anxiety_level = int(data[15])
    emotional_wellbeing = int(data[16])
    considered_dropping_out = int(data[17])
    considered_changing_major = int(data[18])

    # --- RECOMMENDATION LOGIC ---
    if study_hours == "30 minutos o menos":
        recommendations.append("Consider dedicating more time to your studies each day to improve your understanding of the topics.")
    elif study_hours == "1 hora":
        recommendations.append("Try to increase your study time to 2 hours for better content assimilation.")
    elif study_hours == "2 horas":
        recommendations.append("This is a good start, but you could benefit from 3 hours of study. Consider planning your time.")
    elif study_hours == "3 horas":
        recommendations.append("Good amount of study time. Ensure you're taking breaks to maximize concentration.")
    elif study_hours in ["4 horas", "5 horas o más"]:
        recommendations.append("Excellent dedication. Remember to balance your studies with recreational activities.")

    if motivation == "Interés personal":
        recommendations.append("Consider exploring topics you're passionate about within your major more deeply.")

    if work_study_status == "Trabajo y estudio":
        recommendations.append("Make sure to manage your time effectively to avoid burnout. Time management techniques like the Pomodoro Technique could be helpful.")

    if expectations_alignment < 3:
        recommendations.append("You might benefit from talking to an academic advisor to align your expectations with the program's reality.")

    if sufficient_information < 3:
        recommendations.append("It's advisable to seek more information about your major through forums or by talking to senior students.")

    if transition_difficulty < 3:
        recommendations.append("Consider joining student support groups or university adaptation workshops.")

    if academic_load_comfort < 3:
        recommendations.append("If you feel uncomfortable with the academic load, speak with your professors to discuss potential support options.")

    if teaching_style == "Nada interesante":
        recommendations.append("It could be beneficial to voice your concerns to the administration regarding teaching methodologies.")

    if teaching_method == "El profesor muestra un PowerPoint para explicar los temas":
        recommendations.append("You could suggest more interactive activities in class to make lessons more dynamic.")

    if effective_methodologies < 3:
        recommendations.append("Seek more information about different teaching methodologies and how they can impact your learning.")

    if desire_for_practical_activities < 3:
        recommendations.append("Request more group projects or practical activities from your professors to enhance your learning experience.")

    if anxiety_level >= 3:
        recommendations.append("If you are feeling anxious, consider using the emotional wellness resources offered by the university.")

    if emotional_wellbeing < 3:
        recommendations.append("It's important to make time for self-care. Look for activities that help you relax and feel good.")

    if considered_dropping_out >= 3:
        recommendations.append("Talk to an academic advisor to explore your concerns and the options available to you.")

    if considered_changing_major >= 3:
        recommendations.append("Reflect on your reasons and seek guidance to make an informed decision about your academic future.")

    if life_balance < 3:
        recommendations.append("It's crucial to work on a better balance between your studies and personal life. Consider creating a schedule that allows you to enjoy both.")
    
    return recommendations