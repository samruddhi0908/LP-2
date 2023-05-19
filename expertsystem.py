knowledge_base = {'employee_data': {}}

def print_options():
    print('1. Evaluate employee')
    print('2. Add employee data')
    print('3. Modify employee data')
    print('4. View employee data')
    print('5. Exit')


def add_employee_data():
    employee_id = input('Enter employee ID: ')
    employee_data = knowledge_base['employee_data'].get(employee_id)

    if employee_data:
        print(f'Employee with ID {employee_id} already exists.')
        return

    quality_of_work = int(input('Enter quality of work rating (1-10): '))
    quantity_of_work = int(input('Enter quantity of work rating (1-10): '))
    initiative = int(input('Enter initiative rating (1-10): '))
    dependability = int(input('Enter dependability rating (1-10): '))
    communication = int(input('Enter communication rating (1-10): '))
    teamwork = int(input('Enter teamwork rating (1-10): '))

    employee_data = {
        'quality_of_work': quality_of_work,
        'quantity_of_work': quantity_of_work,
        'initiative': initiative,
        'dependability': dependability,
        'communication': communication,
        'teamwork': teamwork
    }

    knowledge_base['employee_data'][employee_id] = employee_data

    print(f'Employee data added successfully for ID {employee_id}.')


def modify_employee_data():
    employee_id = input('Enter employee ID: 2')
    employee_data = knowledge_base['employee_data'].get(employee_id)

    if not employee_data:
        print(f'Could not find employee with ID {employee_id}.')
        return

    print(f'Current employee data for ID {employee_id}:')
    for criterion, score in employee_data.items():
        print(f'{criterion}: {score}')

    criterion = input('Enter criterion to modify: ')
    score = int(input('Enter new score (1-10): '))

    if criterion not in employee_data:
        print(f'Could not find criterion {criterion} for employee with ID {employee_id}.')
        return

    employee_data[criterion] = score
    print(f'{criterion} score updated to {score} for employee with ID {employee_id}.')


def view_employee_data():
    employee_id = input('Enter employee ID: ')
    employee_data = knowledge_base['employee_data'].get(employee_id)

    if not employee_data:
        print(f'Could not find employee with ID {employee_id}.')
        return

    print(f'Employee data for ID {employee_id}:')
    for criterion, score in employee_data.items():
        print(f'{criterion}: {score}')


def evaluate_employee(employee_id):
    employee_data = knowledge_base['employee_data'].get(employee_id)

    if not employee_data:
        return f'Could not find employee with ID {employee_id}.'

    quality_of_work = employee_data['quality_of_work']
    quantity_of_work = employee_data['quantity_of_work']
    initiative = employee_data['initiative']
    dependability = employee_data['dependability']
    communication = employee_data['communication']
    teamwork = employee_data['teamwork']

    # Define some evaluation criteria based on the employee's ratings
    evaluation_criteria = []
    if quality_of_work >= 8:
        evaluation_criteria.append('excellent quality of work')
    elif quality_of_work >= 6:
        evaluation_criteria.append('good quality of work')
    elif quality_of_work >= 4:
        evaluation_criteria.append('average quality of work')
    else:
        evaluation_criteria.append('poor quality of work')

    # Evaluate other criteria in a similar way
    # ...

    evaluation = ', '.join(evaluation_criteria)
    return evaluation

def get_feedback_and_recommendation(evaluation):
    if 'excellent quality of work' in evaluation and 'good communication' in evaluation and 'excellent teamwork' in evaluation:
        feedback = 'The employee is performing exceptionally well in all areas.'
        recommendation = 'Consider promoting the employee to a leadership position.'
    elif 'poor quality of work' in evaluation or 'poor dependability' in evaluation or 'poor teamwork' in evaluation:
        feedback = 'The employee needs improvement in some areas.'
        recommendation = 'Provide additional training and support to help the employee improve.'
    else:
        feedback = 'The employee is performing adequately.'
        recommendation = 'Continue to monitor performance and provide feedback as needed.'
    
    return feedback, recommendation

def main():
    while True:
        print_options()
        choice = input('Enter your choice: ')

        if choice == '1':
            employee_id = input('Enter employee ID: ')
            evaluation = evaluate_employee(employee_id)
            feedback, recommendation = get_feedback_and_recommendation(evaluation)
            print(f'Evaluation result: {evaluation}\nFeedback: {feedback}\nRecommendation: {recommendation}')
        elif choice == '2':
            add_employee_data()
        elif choice == '3':
            modify_employee_data()
        elif choice == '4':
            view_employee_data()
        elif choice == '5':
            print('Exiting program.')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()


