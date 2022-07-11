import pickle

# Values
# First Number - List Number
# Second Number - Value / Reward
# Status - 0 Open, 1 In Progress, 2 Closed

taskList = [(1,10,1),(2,50,2),(3,25,0),(4,69,1)]


#pickle
pickle_out = open("taskList.pickle", "wb")
pickle.dump(taskList, pickle_out)
pickle_out.close()
print("Finished","\n")


#unpickle
pickle_in = open("taskList.pickle", "rb")
taskList = pickle.load(pickle_in)


print(taskList,"\n")
task = input("Please select a task ")
task = int(task)
print("Selected",taskList[task-1][0],"\n")

if taskList[task-1][2] == 0:
    status = "Open"
elif taskList[task-1][2] == 1:
    status = "In Progress"
elif taskList[task-1][2] == 2:
    status = "Closed"

print("---------------------")
print(" Task selected:",taskList[task-1][0],"\n","Reward:",taskList[task-1][1],"\n","Status:",status)
print("---------------------","\n")



# taskValue = [0][1]
# print(taskValue)

# print("Selected", taskList[0][1])

# print("Task")



# -----------------
# Task:1
# Reward: 1ETH
# Status: Open
# -----------------
