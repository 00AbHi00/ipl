# ipl
In this repository using python and libraries like csv and random i have created a ipl simulator.  

this ipl simulation was created by Abhishek Silwal with a little help from ChatGpt.

The working of this simulation is fairly simple. The working can be divided in steps:

1. Importing the files, meaning I have collected the match schedule as ipl-2024-UTC.csv and opened it in the python script
csv and random were imported.

with open('ipl-2024-UTC.csv',mode='r+') as file:

2. I have created 2 programs 
    ipl_simulator_current- In this we can use current points table values to see if possibilty is there for a team to qualify or not
    ipl_simulator_from_1st- In this we can simulate ipl from the begining.

3. Points table:
In a dictionary i have stored the points. In this the key is the name of the team meaning that
pointstable["Chennai Super Kings"] will return the current point of the team chennai super Kings
 For extension we can use dictionary inside dictionary as well
 
 this could be a further improvement
 pointstable = {
    "Kolkata Knight Riders": {"points": 0, "run_rate": 0.0},
    "Chennai Super Kings": {"points": 0, "run_rate": 0.0},
    "Mumbai Indians": {"points": 0, "run_rate": 0.0},
    "Delhi Capitals": {"points": 0, "run_rate": 0.0},
    "Gujarat Titans": {"points": 0, "run_rate": 0.0},
    "Sunrisers Hyderabad": {"points": 0, "run_rate": 0.0},
    "Lucknow Super Giants": {"points": 0, "run_rate": 0.0},
    "Rajasthan Royals": {"points": 0, "run_rate": 0.0},
    "Royal Challengers Bengaluru": {"points": 0, "run_rate": 0.0},
    "Punjab Kings": {"points": 0, "run_rate": 0.0}
}
Accessing could be done as 
# Accessing points and run rate for Kolkata Knight Riders
points = pointstable["Kolkata Knight Riders"]["points"]
run_rate = pointstable["Kolkata Knight Riders"]["run_rate"]

# Updating points and run rate for Kolkata Knight Riders
pointstable["Kolkata Knight Riders"]["points"] += 2
pointstable["Kolkata Knight Riders"]["run_rate"] = 3.5

4. Then, using csv reader to read each line
reader=csv.DictReader(file)
    i=0

5. After that i have  used while loop which runs until there are no more lines in the file.
 and in each i have updated the points table value 
  sorted_pointstable = sorted(pointstable.items(), key=lambda x: x[1], reverse=True)  

6. I have divided the mathces on the  basis 
   Inside the while loop i have seperated matches on the basis of format in which ipl is played
   
   1-70 Group stage match
     winner is selected on random
     winner = random.choice([row['Home Team'],row['Away Team']])   
     If a team wins then the team will  get 2 points 
   
   Displays the points table after group stage has ended. But since i have not taken runrates into consideration, if teams 
   finish with equal points there may be inconsistencies if teams have equal runs, so it is randomly selected.




   71 Semi-final 1 (1st vs 2nd)
    on the basis of points table the teams are selected 
    temp1=[team for team in sorted_pointstable[0][0]]
    however this gives list of individual characters
     ['K', 'o', 'l', 'k', 'a', 't', 'a', ' ', 'K', 'n', 'i', 'g', 'h', 't', ' ', 'R', 'i', 'd', 'e', 'r', 's']
    so they were joined using the join operation .join('', ['K', 'o', 'l', 'k', 'a', 't', 'a', ' ', 'K', 'n', 'i', 'g', 'h', 't', ' ', 'R', 'i', 'd', 'e', 'r', 's'])
    in this the seperator is ''
    loser is assigned as home team in match 73 and the winner is assigned the home team in match 74
    

   72 Eliminator (3rd vs 4rth)
    same logic as above
    winner is assigned the away team in match 73
    
   73 Semi-Final 2 (loser 71 vs winner 72)
        same logic as above
        winner is assigned the away team in match 74
    
   74 Final Match (winner 71 vs winner 73)
    this is a final match, the winner is randomly generated. 

7.Improvements,
 One could assign the game-play on which teams batted first and which team batted second and which player scored how-much runs 
 Stats at the end of the season could be maintained with orange cap and purple cap, there could be chances of rain
 -I have added comments to make it easy

Acknowledgment 
Huge thanks to the person who has maintained the database in csv format and obviously to ChatGpt with which i learn so much 
every day 



