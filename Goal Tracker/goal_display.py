import matplotlib.pyplot as plt 
import re

class GoalTracker:
    """Class to show current progress for goals"""

    def __init__ (self):
        self.doc = "user_goals.txt"
    
    def set_goal(self, goal_name):
        #set a new goal to be tracked
        if self.check_goal_exists(goal_name) == False:
            with open(self.doc, "a+") as goal_doc:
                goal_doc.write(f"{goal_name}: 0\n")
        else:
            print("You already have this goal!")

    def update_goal_progress(self, goal_name, progress):
        #update an existing goal, only progress to be altered
        if self.check_goal_exists(goal_name):
            with open(self.doc, "r") as txt:
                lines = txt.readlines()
                with open(self.doc, "w+") as txt:
                    for goal in lines:
                        if goal_name not in goal:
                            txt.write(goal)
                    txt.write(f"{goal_name}: {progress}\n")
        else:
            print("No such Goal Exists!")

    def check_goal_exists(self, goal_name):
        #check if a goal exists already
        with open(self.doc, "r") as txt:
            lines = txt.readlines()
            test_for_goal = ' '.join([line for line in lines])
            if re.findall("%s" % goal_name, test_for_goal):
                return True
            else:
                return False

    def see_progress(self, goal):
        present = False
        with open(self.doc) as goal_doc:
            for line in goal_doc:
                goal_name = line.split(":")
                if goal == goal_name[0]:
                    present = True
                    completed = int(goal_name[1])
                    if completed > 0:
                        labels = "Progression", "Remaining"
                    else:
                        labels = "Remaining", ""
                    sizes = [completed, (100 - completed)]
                    title = goal_name[0]
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
str = "Upload GitHub Repository"
ben.see_progress(str)
ben.set_goal(str)
ben.see_progress(str)
ben.update_goal_progress("Upload GitHub Repository", 35)
ben.see_progress(str)