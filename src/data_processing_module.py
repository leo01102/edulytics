# data_processing_module.py

from src.sheet_config import get_column_indices

# processes the raw data fetched from Google Sheets
def process_responses(values):
    # the first row in the sheet contains the headers
    header = values[0]

    # map column names to their index for reliable access
    columns = get_column_indices(header)

    processed_data = []

    # iterate over each row, skipping the header
    for row in values[1:]:
        if len(row) <= columns['email']:
            print("Skipping incomplete row...")
            continue

        # extract data using the column index map
        email = row[columns['email']]
        study_hours = row[columns['study_hours']] if len(row) > columns['study_hours'] else None
        
        # assemble a dictionary for each student's response
        processed_data.append({
            "email": email,
            "study_hours": study_hours,
            "timestamp": row[columns['timestamp']],
            "department": row[columns['department']],
            "high_school_specialty": row[columns['high_school_specialty']],
            "work_or_study": row[columns['work_or_study']],
            "motivation": row[columns['motivation']],
            "expectations_alignment": row[columns['expectations_alignment']],
            "sufficient_information": row[columns['sufficient_information']],
            "transition_difficulty": row[columns['transition_difficulty']],
            "academic_load": row[columns['academic_load']],
            "content_relevance": row[columns['content_relevance']],
            "teaching_methodology": row[columns['teaching_methodology']],
            "effective_methodologies": row[columns['effective_methodologies']],
            "more_practical_activities": row[columns['more_practical_activities']],
            "study_life_balance": row[columns['study_life_balance']],
            "anxiety_stress": row[columns['anxiety_stress']],
            "wellness_resources": row[columns['wellness_resources']],
            "considered_dropping_out": row[columns['considered_dropping_out']],
            "considered_changing_major": row[columns['considered_changing_major']],
            "student_input_responses": row[1:20]  # assumes open-ended questions are in columns 1-20
        })

    return processed_data