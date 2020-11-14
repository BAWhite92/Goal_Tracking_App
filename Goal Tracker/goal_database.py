import sqlite3

def create_goals_data():
    '''Will create a new SQLite database to save goals in'''

    #connect to database with name emaildb.sqlite, will create file when it runs if it doesn't exist
    conn = sqlite3.connect('goaltracker.sqlite')

    #set the cursor (send sql commands through cursor)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Goals (
            goal TEXT NOT NULL, 
            progress INTEGER NOT NULL)''')
    conn.commit()


def update_goals_data(goal, progress):    
    '''Method to add goals and progress to the database of update them'''

    #make sure goal is titled to ensure matches in database
    goal = goal.title()
    #ensure that the database exists, if not create it.
    create_goals_data()

    conn = sqlite3.connect('goaltracker.sqlite')
    cur = conn.cursor()
    
    cur.execute('SELECT goal FROM Goals WHERE goal = ?', (goal,)) 
    #row will be info we get back from the database
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Goals (goal, progress) VALUES (?, ?)', 
                    (goal, 0))
    else:
        cur.execute('UPDATE Goals SET progress = ? WHERE goal = ?',
                    (progress, goal))
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
