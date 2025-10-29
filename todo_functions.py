todo_list = []

def added_tesk(tasks:list):
    task = str(input('new task:'))
    tasks.append(task)
    print ('The task was added successfully.')
    return

def view_tasks(tasks:list):
    if len(tasks) == 0:
        return 'The task lists are empty.\n' \
        'If you want to add a task - select the Add task option\n'
    print ('\ntasks:')
    for i in range(len(tasks)):
        print (f'\n{i+1}. {tasks[i]}')
    return 

def get_task_index_from_user() -> int:
    task_number = int(input('Task number to remove?'))
    index = task_number-1
    return index

def delete_task(tasks: list):
    view_tasks(tasks)
    index = get_task_index_from_user()
    if index not in range(len(tasks)):
        print ('There is no task at the number you specified.')
        return delete_task(tasks)
    tasks.pop(index)
    return 'The task with the number you specified was successfully removed.'

def edit_task(tasks: list) -> bool:
    view_tasks(tasks)
    index = get_task_index_from_user()
    new_task = str(input('new task in place of the existing one:'))
    if index not in range(len(tasks)):
        print ('There is no task at the number you specified.')
    tasks[index] = new_task
    return 'The task was successfully modified.'

def brake(tasks:list):
    return 'End of task organization'

def options():
    options = {1: ('Add task', added_tesk),
               2 : ('View tasks', view_tasks),
               3 : ('Delete task', delete_task),
               4 : ('Edit task', edit_task),
               5 : ('Exit', brake)
               }
    return options

def view_options(options:dict[tuple]):
    print ('\nThe options are:')
    for i in options:
        print (f'\n{i}. {options[i][0]}')
    return

def user_selection(options:dict):
    selection = int(input('Select an action from the options.'))
    while selection < 1 or selection > len(options):
        print ('Write the correct operation number according to the list.')
        selection = user_selection(options)
    return selection

def main() -> None:
    global todo_list
    tasks = todo_list
    while True:
        print (view_options(options()))
        selection = user_selection(options())
        if selection == 5:
            return
        selected_action = options()[selection][1]
        selected_action(tasks)
    return
main()
    


