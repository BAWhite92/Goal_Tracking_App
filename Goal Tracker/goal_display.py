import matplotlib.pyplot as plt 
import re
import goal_database

class GoalTracker:
    """Class to show current progress for goals"""

    def __init__ (self):
        self.doc = "user_goals.txt"
    
    def set_goal(self, goal_name):
        #set a new goal to be tracked
        if goal_database.check_goal_exists:
            print("Goal already exists!")
        else:
            goal_database.update_goals_data(goal_name, 0)
            print(f"Goal {goal_name} Set!")

    def update_goal_progress(self, goal_name, progress):
        #update an existing goal, only progress to be altered
        if goal_database.check_goal_exists(goal_name):
            goal_database.update_goals_data(goal_name, progress)
        else:
            print("No such goal exists")


    def see_progress(self, goal):
        present = False
        #make sure that the goal exists.
        if goal_database.check_goal_exists(goal):
            present = True
            #get the goal information from the database
            cur_goal = goal_database.get_goal_data(goal)
            completed = cur_goal[1]
            goal_name = cur_goal[0]
            #start prepping data for graphing
            if completed > 0:
                labels = "Progression", "Remaining"
            else:
                labels = "Remaining", ""
            sizes = [completed, (100 - completed)]
            title = goal_name
            pie = self.create_pie_chart(labels, sizes, title)
            plt.show() 
        if present == False:
            print("No such Goal, please try again")

    def create_pie_chart(self, labels, sizes, title):
        fig1, ax = plt.subplots()
        ax.pie(sizes, labels=labels, shadow=True)
        ax.axis("Equal")
        ax.set_title(title, fontsize = 24)
        return ax

ben = GoalTracker()
ben.set_goal("Keep On Going")
ben.see_progress("Keep on going")
ben.update_goal_progress("Keep on going", 55)
ben.see_progress("Keep on going")