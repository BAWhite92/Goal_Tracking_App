import matplotlib.pyplot as plt 

class GoalTracker:
    """Class to show current progress for goals"""

    def __init__ (self):
        self.doc = "user_goals.txt"
    
    def set_goal(self, goal_name):
        with open(self.doc, "a+") as goal_doc:
            goal_doc.write(f"\n{goal_name}: 0")


    def see_progress(self, goal):
        with open(self.doc) as goal_doc:
            for line in goal_doc:
                print("line")
                goal_name = line.split(":")
                if goal in goal_name:
                    completed = int(goal_name[1])
                    if completed > 0:
                        labels = "Progression", "Remaining"
                    else:
                        labels = "Remaining", ""
                    sizes = [completed, (100 - completed)]
                    title = goal_name[0]
                    pie = self.create_pie_chart(labels, sizes, title)
                    plt.show() 

    def create_pie_chart(self, labels, sizes, title):
        fig1, ax = plt.subplots()
        ax.pie(sizes, labels=labels, shadow=True)
        ax.axis("Equal")
        ax.set_title(title, fontsize = 24)
        return ax

ben = GoalTracker()
str = "Upload GitHub Repository"
ben.see_progress(str)
#ben.set_goal("Upload GitHub Repository")