morality_points = 0
logic_points = 0



answer = input("When choosing a path in life would you rather A) choose a career path that makes the most sense sense to you, B) focus on things that align with your sense of inner self, or C) choose something for the sake of making the most sense to others even if its not true in your heart?")
if answer == "A":
    logic_points += 1
elif answer == "B":
    morality_points += 1
elif answer == "C": 
    morality_points += 1 
elif answer == "C":
    logic_points += 1


answer = input("Which do you agree with better? A) I can have deep or important feelings, both internally and applied to the outside world, but I typically have somewhat ignored them in favor of detached analysis of my situation even when trying to do what feels right, or B) I have quite a lot of knowledge about the world, but when I make decisions I typically end up doing what I feel is the right thing to do even when trying to be objective")
if answer == "A":
    logic_points += 1
elif answer == "B":
    morality_points += 1
   
answer = input("When making group decisions do you A) Look at the statistics or the logical way for your brain to problem solve or B) Focus more on how you and/or other people feel when making a decision for the group")
if answer == "A":
    logic_points += 1
elif answer == "B":
    morality_points += 1


answer = input("Would you say when thinking about things logically you A) base them off your own inner rules or B) Base them off societies rules and/or expectations")
if answer == "B":
    logic_points += 1
elif answer == "A":
    morality_points += 1

answer = input("Do you think you A) base decisions based on thinking or B) base them off your morals")
if answer == "B":
    logic_points += 1
elif answer == "A":
    morality_points += 1

# end of quiz:
if morality_points > logic_points:
    print("You make decisions based on your morals")
elif morality_points < logic_points:
    print("You make decisions based on logic ")