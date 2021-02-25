tasks = [
    { 'description': 'Wash Dishes', 'completed': False, 'time_taken': 10 },
    { 'description': 'Clean Windows', 'completed': False, 'time_taken': 15 },
    { 'description': 'Make Dinner', 'completed': True, 'time_taken': 30 },
    { 'description': 'Feed Cat', 'completed': False, 'time_taken': 5 },
    { 'description': 'Walk Dog', 'completed': True, 'time_taken': 60 },
]

def uncompleted_tasks(tasks_list):
    uncompleted_list = []
    for task in tasks_list:
        if task['completed'] == False:
            uncompleted_list.append(task)
    return uncompleted_list

#print(uncompleted_tasks(tasks))

def completed_tasks(tasks_list):
    completed_list = []
    for task in tasks_list:
        if task['completed'] == True:
            completed_list.append(task)
    return completed_list

#print(completed_tasks(tasks))

def task_descriptions(tasks_list):
    task_descriptions = []
    for task in tasks_list:
        task_descriptions.append(task['description'])
    return task_descriptions

#print(task_descriptions(tasks))

def time_tasks(tasks_list, given_time):
    time_list = []
    for task in tasks_list:
        if task['time_taken'] > given_time:
            time_list.append(task)
    return time_list

#print(time_tasks(tasks, 15))

def description_tasks(tasks_list, description):
    description_list = []
    for task in tasks_list:
        if task['description'] == description:
            description_list.append(task)
    return description_list

#print(description_tasks(tasks, 'Walk Dog'))

def update_task(tasks_list, description):
    for task in tasks_list:
        if task['description'] == description:
            task['completed'] = True

#update_task(tasks, 'Feed Cat')
#print(tasks)

def add_task(tasks_list, new_task_description, new_task_complete, new_task_time):
    tasks_list.append({
        'description': new_task_description,
        'completed': new_task_complete,
        'time_taken': new_task_time
    })

#add_task(tasks, 'Feed Dog', True, 5)
#print(tasks)

def menu():
    print('Menu:')
    print('1: Display All Tasks')
    print('2: Display Uncompleted Tasks')
    print('3: Display Completed Tasks')
    print('4: Mark Task as Complete')
    print('5: Get Tasks Which Take Longer Than a Given Time')
    print('6: Find Task by Description')
    print('7: Add a new Task to list')
    print('M or m: Display this menu')
    print('Q or q: Quit')

def users_choice(tasks_list):
    menu()
    choice_list = ['1', '2', '3', '4', '5', '6', '7', 'M', 'Q']
    choice = input('Please input your choice from the list above:')
    while True:
        if choice == '1':
            print(task_descriptions(tasks_list))
            break
        if choice == '2':
            print(uncompleted_tasks(tasks_list))
            break
        if choice == '3':
            print(completed_tasks(tasks_list))
            break
        if choice == '4':
            description = input('Please input which task has been completed:')
            update_task(tasks_list, description)
            print(f'{description} has been updated')
            break
        if choice == '5':
            given_time = input('Please input the minimum time you which to see:')
            print(time_tasks(tasks_list, int(given_time)))
            break
        if choice == '6':
            description = input('Please input the description of the task:')
            print(description_tasks(tasks_list, description))
            break
        if choice == '7':
            new_task_description = input('Please input the decription of the new task:')
            new_task_complete = input('Has it been completed (y or n):')
            if new_task_complete == 'y':
                new_task_complete = True
            else:
                new_task_complete = False
            new_task_time = input('How long does it take to complete? (minutes):')
            add_task(tasks_list, new_task_description, new_task_complete, int(new_task_time))
            print(f'New task, {new_task_description}, has been added')
            break
        if choice == 'M' or 'm':
            menu()
            choice = input('Please input your choice from the list above:')
        if choice == 'Q' or 'q':
            return None
        if choice not in choice_list:
            choice = input('Please input your choice from the list above:')

users_choice(tasks)