import random

user_input = ""


def rid(list):
    stp_list = []
    for item in list:
        stp_list.append(item.strip("\n"))
    return stp_list
    
def assign_teams(students):
    teams = {"team1":[], "team2":[]}
    pool = students
    while len(pool) > 0:
        to_add = []
        current_team1 = teams["team1"]
        current_team2 = teams["team2"]
        current_team1.append(pool.pop(random.choice(range(len(pool)))))
        current_team2.append(pool.pop(random.choice(range(len(pool)))))
        teams["team1"] = current_team1
        teams["team2"] = current_team2
    print("Team 1 is {team1}".format(team1 = teams["team1"]))
    print("Team 2 is {team2}".format(team2 = teams["team2"]))

    return teams

def generate_prompts():
    line = random.choice(lines)

    tone1 = random.choice(tones)

    tone2 = random.choice(tones)

    player1 = random.choice(team1)
    player2 = random.choice(team2)

    print("{student} must recite the line \"{line}\" for Team 1 with the following tone: {tone}".format(student = player1,line = line,tone = tone1 ))
    print("{student} must recite the line \"{line}\" for Team 2 with the following tone: {tone}".format(student = player2,line = line,tone = tone2 ))
    
    

#open files for use

with open("tone_list_real.txt") as tone_list:
    tones = rid(tone_list.readlines())
    
with open("s_list.txt") as students_file:
    students = rid(students_file.readlines())

with open("lines_list.txt") as lines_file:
    lines = rid(lines_file.readlines())


#assign teams from fuction
teams_dictionary = assign_teams(students)


team1 = teams_dictionary["team1"]
team2 = teams_dictionary["team2"]
team1_score = 0
team2_score = 0

while user_input != "quit":
    user_input = input()
    if user_input == 't1':
        team1_score += 1
        generate_prompts()
        continue
    elif user_input == "gen":
        generate_prompts()
    elif user_input == 't2':
        team2_score += 1
        generate_prompts()
        continue
    elif user_input == 'force1':
        print("What would you like team 1's score to be?")
        team1_score = input()
    elif user_input == 'force2':
        print("What would you like team 2's score to be?")
        team2_score = input()
    elif user_input == "score":
        print("Team 1:",team1_score)
        print("Team 2:",team2_score)
    
    
        


