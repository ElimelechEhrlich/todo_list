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

def delete_task(tasks:list):
    return 'This action is not yet available.'

def edited_task(tasks:list):
    return 'This action is not yet available.'

def brake(tasks:list):
    return 'End of task organization'

def options():
    options = {1: ('Add task', added_tesk),
               2 : ('View tasks', view_tasks),
               3 : ('Delete task', delete_task),
               4 : ('Edit task', edited_task),
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
    


