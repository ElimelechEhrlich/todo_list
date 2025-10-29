todo_list = ['aaa', 'bbb']

def added_tesk(tesk:str, tesks:list):
    return tesks.append(tesk)
    # return 'The task was added successfully.'

def view_tasks(tesks:list):
    if len(tesks) == 0:
        return 'The task lists are empty.\n' \
        'If you want to add a task - select the Add task option'
    for i in range(len(tesks)):
        print (f'{i+1}. {tesks[i]}')
    return  




