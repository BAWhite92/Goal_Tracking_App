import sqlite3

def create_goals_data():
    '''Will create a new SQLite database to save goals in'''

    #connect to database with name goaltracker.sqlite, will create file when it runs if it doesn't exist
    conn = sqlite3.connect('goaltracker.sqlite')

    #set the cursor (send sql commands through cursor)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Goals (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            goal TEXT NOT NULL,
            progress INTEGER NOT NULL)''')
    conn.commit()

def create_sub_goal_data():
    '''Will create a new SQLite database for subgoal is required.
        subgoals will have a foreign key for main goals'''

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS SubGoals (
            subgoal TEXT NOT NULL,
            progress INTEGER NOT NULL
            goal_id INTEGER )''')
    conn.commit()

def update_sub_goal(sgoal, progress, goal):
    '''Method to add a new subgoal or update an existing one'''
    #make sure sub goal is titled to ensure database match.
    sgoal  = sgoal.title()
    #ensure database exists, if not create it.
    create_sub_goal_data()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()
    #get id of the main goal the subgoal will support
    cur.execute('SELECT id FROM Goals WHERE goal = ?', (goal,))
    goal_id = cur.fetchone()[0]

    if goal_id is None:
        return False
    elif check_sub_goal_exists(sgoal):
        cur.execute('UPDATE SubGoals SET progress = ? WHERE subgoal = ?',
                (progress, sgoal))
    else:
        cur.execute('''INSERT INTO SubGoals (subgoal, progress, goal_id)
                VALUES (?, ?, ?)''', (sgoal, 0, goal_id))
    conn.commit()


def update_goals_data(goal, progress):
    '''Method to add goals and progress to the database of update them'''

    #make sure goal is titled to ensure matches in database
    goal = goal.title()
    #ensure that the database exists, if not create it.
    create_goals_data()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()

    if check_goal_exists(goal):
        cur.execute('UPDATE Goals SET progress = ? WHERE goal = ?',
                    (progress, goal))
    else:
        cur.execute('INSERT INTO Goals (goal, progress) VALUES (?, ?)',
                    (goal, 0))
    conn.commit()


def check_goal_exists(goal):
    #make sure goal is titled to ensure database matches
    goal = goal.title()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()

    #get the data for the goal that you are searching for.
    cur.execute('SELECT goal, progress FROM Goals WHERE goal = ?', (goal,))
    #set row to the info returned from the database.
    row = cur.fetchone()
    if row is None:
        return False
    else:
        return True

def check_sub_goal_exists(sgoal):
    #make sure goal is titled to ensure database matches
    sgoal = sgoal.title()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()

    #get the data for the goal that you are searching for.
    cur.execute('SELECT subgoal, progress FROM SubGoals WHERE subgoal = ?',
            (sgoal,))
    #set row to the info returned from the database.
    row = cur.fetchone()
    if row is None:
        return False
    else:
        return True

def get_goal_data(goal):
    #make sure goal is titled to ensure database matches
    goal = goal.title()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()

    #get the data for the goal that you are searching for.
    cur.execute('SELECT goal, progress FROM Goals WHERE goal = ?', (goal,))
    #set row to the info returned from the database.
    row = cur.fetchone()
    #the calling method will use check_goal_exists so no check are required.
    return row

def get_sub_goal_data(sgoal):
    #make sure goal is titled to ensure database matches
    sgoal = sgoal.title()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()

    #get the data for the goal that you are searching for.
    cur.execute('SELECT subgoal, progress FROM SubGoals WHERE subgoal = ?',
            (sgoal,))
    #set row to the info returned from the database.
    row = cur.fetchone()
    #the calling method will use check_goal_exists so no check are required.
    return row

def delete_goal(goal):
    goal = goal.title()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()

    if check_goal_exists(goal):
        cur.execute('DELETE * FROM Goals where goal = ?', (goal,))
        return True
    else:
        return False
