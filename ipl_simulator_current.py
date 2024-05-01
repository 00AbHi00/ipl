import csv
import random

# opening the csv in r-w mode although write has not been initiated
with open('ipl-2024-UTC.csv',mode='r+') as file:
   
#   enter current table after match 46
    
    pointstable = {
        "Kolkata Knight Riders":12,
        "Chennai Super Kings":10,
        "Mumbai Indians":6,
        "Delhi Capitals":10,
        "Gujarat Titans":8,
        "Sunrisers Hyderabad":10,
        "Lucknow Super Giants":10,
        "Rajasthan Royals":16,
        "Royal Challengers Bengaluru":6,
        "Punjab Kings":6  
    }
    # this is a method in csv to read files
    reader=csv.DictReader(file)
    
    i=0
    current_game=47
    for row in reader:
        i+=1
       
        #sorting points table after each match
        sorted_pointstable = sorted(pointstable.items(), key=lambda x: x[1], reverse=True)  
        
        #loop till current match
        #the reader row has to increase only when the  
        if i<current_game:
            continue
        
        if i==current_game:
            x=1
            #printing current table
            print("mathes have ended, Final table is")
            for team, points in sorted_pointstable:
                print(f"{str(x)}. {team}: {points} points")
                x+=1
            print("OK")
            
        if i>47 and i<=70:        
            print(f"Match {i}:",end="")
            print(row['Home Team'],end="")
            print(" VS ",row['Away Team'])
            winner = random.choice([row['Home Team'],row['Away Team']])
            # adding two points to the winner
        
        #user give condition
        #
        #
        #condition : RR losing all games, other games can also be controlled here
            
            # if(row["Home Team"]=="Rajasthan Royals"):
            #     winner=row["Away Team"]
            # elif(row["Away Team"]=="Rajasthan Royals"):
            #     winner=row["Home Team"]
            
            print("winner",winner)
            pointstable[winner]+=2  
            #final table
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
            
               
                
     
   


    