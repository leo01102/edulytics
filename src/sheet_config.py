# sheet_config.py

# maps the column headers from the Google Form to their corresponding index
# note: the values must exactly match the question text in the sheet's header
def get_column_indices(header):
    return {
        'timestamp': header.index('Marca temporal'),
        'email': header.index('Dirección de correo electrónico'),
        'department': header.index('¿De qué departamento es la carrera que elegiste?'),
        'high_school_specialty': header.index('¿En qué se especializaba tu secundaria?'),
        'work_or_study': header.index('¿Actualmente trabajas o solo estudias?'),
        'study_hours': header.index('¿Más o menos cuántas horas estudias normalmente por día fuera de clases? (opcional)'),
        'motivation': header.index('¿Qué te motivó a elegir esta carrera?'),
        'expectations_alignment': header.index('¿Hasta ahora qué tan alineadas están tus expectativas iniciales con lo que has experimentado hasta ahora en la carrera?'),
        'sufficient_information': header.index('¿Consideras que la información que recibiste antes de comenzar la carrera fue suficiente para tomar una decisión informada?'),
        'transition_difficulty': header.index('¿Qué tan difícil se te hizo la transición del colegio a la universidad?'),
        'academic_load': header.index('¿Te sientes cómodo con la carga académica actual?'),
        'content_relevance': header.index('Hasta ahora ¿Consideras que la forma en que se te enseñaron los contenidos de las materias es interesante/relevante?'),
        'teaching_methodology': header.index('¿Cómo suele ser la metodología de enseñanza de la mayoría de tus clases?'),
        'effective_methodologies': header.index('De las metodologías que elegiste antes, ¿te resultan efectivas para aprender?'),
        'more_practical_activities': header.index('¿Te gustaría tener más actividades prácticas o proyectos grupales en los primeros años de la carrera?'),
        'study_life_balance': header.index('¿Sientes que puedes equilibrar tus estudios con otras áreas de tu vida, como la vida social, familiar o laboral?'),
        'anxiety_stress': header.index('¿Has sentido ansiedad o estrés relacionado con tus estudios en este primer año?'),
        'wellness_resources': header.index('¿Sientes que la universidad ofrece suficientes recursos para tu bienestar emocional y el de los demás estudiantes?'),
        'considered_dropping_out': header.index('¿Has pensado en abandonar la universidad?'),
        'considered_changing_major': header.index('¿Has pensado en cambiar de carrera desde que comenzaste?')
    }