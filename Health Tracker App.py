'''Question 4: Health Tracker App
Create a function check_activity_goal(steps_taken, goal) for a Health Tracker App. If the user has 
achieved their daily step goal (given as input), return "Goal achieved," otherwise, provide a message 
indicating how many more steps are needed to reach the goal.'''

def check_activity_goal(steps_taken, goal):
    if steps_taken == goal:
        print("Goal achieved")
    else:
        print(goal-steps_taken,"Need More Steps")
    return goal,steps_taken
goal = int(input("Enter The Today's Goal "))
steps_taken = int(input("Enter the steps Taken "))
print(check_activity_goal(steps_taken, goal))