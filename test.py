a = 'אלימלך'
b = 'V '+a
c = ['אלימלך ארליך', 'גיטי ארליך']
print(b[::-1])

def search_tasks(tasks: list) -> list:
    keyword = str(input('The task you are looking for:'))
    task_with_keyword = []
    for i in range(len(tasks)):
        if keyword in tasks[i]:
            matching_task = (i, tasks[i])
            task_with_keyword.append(matching_task)
    if len(task_with_keyword) == 0:
        print ('There is no task that matches your search.')
        return
    print (task_with_keyword)
    return
search_tasks(c)