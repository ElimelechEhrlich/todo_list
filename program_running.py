import todo_functions

def get_task_index_from_user() -> int:
    task_number = int(input('Task number of task?'))
    index = task_number-1
    return index

def main() -> None:
    tasks = todo_functions.todo_list
    while True:
        selection = todo_functions.user_selection(todo_functions.options(), tasks)
        if len(tasks) < 1 and selection != 1:
            print ('The task lists are empty')
            return
        if selection == 7:
            return todo_functions.brake(tasks)
        print (todo_functions.view_options(todo_functions.options()))
        selected_action = todo_functions.options()[selection][1]
        selected_action(tasks)
    return
main()