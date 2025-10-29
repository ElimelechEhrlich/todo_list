todo_list = ['aaa', 'bbb']

def added_tesk(task:str, tasks:list):
    return tasks.append(task)
    # return 'The task was added successfully.'

def view_tasks(tasks:list):
    if len(tasks) == 0:
        return 'The task lists are empty.\n' \
        'If you want to add a task - select the Add task option'
    for i in range(len(tasks)):
        print (f'{i+1}. {tasks[i]}')
    return  

def options():
    options_list = {'1': 'Add task',
               '2' : 'View tasks',
               '3' : 'Delete task',
               '4' : 'Edit task',
               '5' : 'Exit'
               }
    for i in options_list:
        print (f'{i}. {options_list[i]}')
    return options_list

def user_selection(options):
    selection = int(input('Select an action from the options.'))
    if selection < 1 or selection > len(options):
        print ('Write the correct operation number according to the list.')
        selection = user_selection(options)
    return selection

print (user_selection(options()))

