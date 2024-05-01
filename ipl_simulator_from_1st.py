import csv
import random

with open('ipl-2024-UTC.csv',mode='r+') as file:
   
    pointstable = {
        "Kolkata Knight Riders":0,
        "Chennai Super Kings":0,
        "Mumbai Indians":0,
        "Delhi Capitals":0,
        "Gujarat Titans":0,
        "Sunrisers Hyderabad":0,
        "Lucknow Super Giants":0,
        "Rajasthan Royals":0,
        "Royal Challengers Bengaluru":0,
        "Punjab Kings":0  
    }
    reader=csv.DictReader(file)
    i=0
    
    for row in reader:
        i+=1
        sorted_pointstable = sorted(pointstable.items(), key=lambda x: x[1], reverse=True)  
        if i<=70:
            # print(f"Match {i}:",end="")
            # print(row['Home Team'],end="")
            # print(" VS ",row['Away Team'])
            winner = random.choice([row['Home Team'],row['Away Team']])
            # # adding two points to the winner
            # print("winner",winner)
            pointstable[winner]+=2 
            if i==70:
                x=1
                print("mathes have ended, Final table is")
                for team, points in sorted_pointstable:
                    print(f"{str(x)}. {team}: {points} points")
                    x+=1
        
        #for the semi finals we add the teams as Preliminary final 1-> home= 1st team away=2nd team
        elif i==71:
            temp1=[team for team in sorted_pointstable[0][0]]
            temp2=[team for team in sorted_pointstable[1][0]]
            row["Home Team"]=''.join(temp1)
            row["Away Team"]=''.join(temp2)       
            print("\nsemi final-1")
            print("71",row['Home Team'],"vs",row["Away Team"])
            winner = random.choice([row['Home Team'],row['Away Team']])
            if winner==row["Home Team"]:
                loser=row["Away Team"]
            else:
                loser=row["Home Team"]
            print("winner",winner) 
            print("loser",loser) 
            
            finalist1=winner
            semi_finalist1=loser
            #qualifier 1 (1st vs 2nd) winner to home team in match 74, loser to home team in match 73  

        elif i==72:
            temp1=[team for team in sorted_pointstable[2][0]]
            temp2=[team for team in sorted_pointstable[3][0]]
            row["Home Team"]=''.join(temp1)
            row["Away Team"]=''.join(temp2)       
            print("\nEliminator")
            print("72",row['Home Team'],"vs",row["Away Team"])
            winner = random.choice([row['Home Team'],row['Away Team']])
            print("winner",winner) 
            semi_finalist2=winner
           
            #qualifier 1 (3rd vs 4rth) 
        elif i==73:
            print("\nsemi final-2")
            row["Home Team"]=semi_finalist1
            row["Away Team"]=semi_finalist2
            
            print(row['Home Team'],end="")
            print(" VS ",row['Away Team'])
            print("72",row['Home Team'],"vs",row["Away Team"])
            winner = random.choice([row['Home Team'],row['Away Team']])
            print("winner",winner) 
            finalist2=winner
           
            #qualifier 1 (loser 71 vs winner 72) 
        elif i==74:
            print("\n\nfinal:")
            row["Home Team"]=finalist1
            row["Away Team"]=finalist2
            print(row['Home Team'],end="")
            print(" VS ",row['Away Team'])
            winner = random.choice([row['Home Team'],row['Away Team']])
            print("\n\nwinner",winner,"\n\n")
            if (winner=="Royal Challengers Bengaluru"):
                print("ee sala cup namdu")
            
               
                
     
   


    