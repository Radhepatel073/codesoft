def main():
    task = []  # empty task list for entering values
    print("--------------------------- welcome to the to-do list -----------------------------------\t")
    total_task = int(input("Enter how many tasks you want to add: "))
    
    for i in range(1, total_task + 1):
        task_name = input(f'Task number {i}: ')
        task.append(task_name)
        

    print(f'today task are {task}')
    
    while True:
        operation = int(input("Enter 1-add\n 2-update\n 3-delete\n 4-view\n 5-exit/stop/ "))
        
        if operation == 1:
            add = input('Enter the task you want to add: ')
            task.append(add)
            print(f'Your task "{add}" is successfully added.')  # this is the add of your task
            
        elif operation == 2: #update the number
             update_index = input("Enter the index of the task you want to update : ")
             if update_index in task:
                   up = input("enter the new tasks")
                   ind = task.index(update_index)
                   task[ind]= up
                  
            
        elif operation == 3: # delete the number
             dele = input('enter the task you want to delete')
             if dele in task:
                 ind = task.index(dele)
                 del task[ind]
                 print(f"your {dele}task is successful delete")
        
        elif operation == 4: #view list
            print(f"total task ={task}")
        elif operation == 5:
            break
        else:
            print("user enter the wrong number")
                 
main()
#print the main function