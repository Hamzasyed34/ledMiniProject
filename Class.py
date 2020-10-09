
''' This function will print the welcome message to the user and will be asked to input the enter key to continue'''
def welcomeToTheGame():
    print ("Welcom to Timothy's story")
    print("")
    print ("In this story you will be able to experiance the story from different angles")
    print("")

    print ("each angle could have different endings depending on which path you chose.")
    print("")
    
#End of the function
welcomeToTheGame()

''' this function prints the beginning of the story, user will have to input string "yes" or "no" to chose if they want the details of the story '''
def welcomeToTheStory():
    print ("In a developing world that relies on technology," +
    "The Logic Theorist was the most revolutionary artificial intelligence development tool which gave the dedicated and talented man John McCarthy his title as the father of AI." +
    "John’s genius relied on his incredible ability to gather useful information from a variety of resources that were used in the past to create the very first prototype of a human-like machine.")
    print("")

    userEnter = input("press enter to continiue the story")
    print("")

    print("John managed to successfully create an AI that could serve as the best human like machine to have as a companion that could help solve any problem," +
    "give advice, or go out and do your chores for the day." +
    "He could do many different tasks that humans would do; however, he could do it much more efficiently and accurately." +
    "For example, he was massively loved due to the amount of assistance he would provide whether it was just advice or helping someone do a specific task." +
    "Other than the soul, John’s AI was just like any other human, but exceptionally intelligent." +
    "John had a robot so smart that people would envy him for his knowledge, strength and invulnerabilities compared to humans.  ")
    print("")
#End of the function

welcomeToTheStory()

def timothyChangingBehaviour():
    ''' This variable contains the information of timothy strange behaviour'''
    unexpectedBehaviour = "In the beginning when John was still in the process of making, Timothy was giving unexpected results, John found these unusual results in the tests that were used to train Timothy. He found out that even when Timothy was on its early stage it kept trying to get new information beyond its reach. What amazed John was that it was trying to break the engine in which it was training. First, he thought it is expected from something that learns itself to be more curious but at the same time he was a bit worried about if it gets out of hand or manages to access restricted zones. At first Timothy’s words were predictable and simple but as time passed it became more complicated and uncertain."

    return unexpectedBehaviour

#The user will chose if to skip the reason of timothy's creation or not
userInputReason = input("Type yes to read the reason behind Timothy's creation, type no to skip the reason: ")
print("")

''' This function will print the reason John created Timothy '''
def reasonForCreatingTheAI():
    reason = "Johns main reason for creating such piece of machinery was otherwise a lot simpler than the amount of code lines and endless fails until the machine taught itself how to act alive. John just wants to have someone to be there for him, someone to talk and in order fill his emptiness and relieve his pain within after losing his only child. that is why he needed someone relief that pain, someone who could comfort him and someone who fill the whole of emptiness that was left after the death of his child. As a result he created a perfect friend who would help him to release the pain he is feeling, he named his only hope of recovering from the pain after his child, Timothy."
    print("")
    return reason
#End of the function

'''if the user input for variable 'userInputReason' is 'yes' then this code will call the function called 'reasonForCreatingTheAI'
and then will print the fuunction called timothyChangingBehaviour '''
if userInputReason == 'yes':
    print(reasonForCreatingTheAI())
    print("")
    userEnter = input("press enter to continue the story")
    print("")
    print(timothyChangingBehaviour())
    print("")

    '''if the user input for variable 'userInputReason' is 'no' then the code will skip the reasonForCreatingAI and will print the variable 'unexpectedBehaviour'
    however if the user inputs yes then timothuBehaviour function will be printed after resonForCreatingAI '''
elif userInputReason == 'no':
    print(timothyChangingBehaviour())
    print("")
#end

'''this variable will output a messeage asking user to input string, and will save the input to the variable'''
ecChip = input("do you want to restrict Timothy's access? type yes if want to restrict access otherwise type no:")
print("")
#end

''' This function contains a variable which contains string data type, data explains what happens when user decides to restrict timothy'''
def createEcChipToRestrictTimothy():
    restrictTimothy = "As much as John was eager to have someone to talk or have a friend, he was also being cautious so he created stricter chip called E.C. which would only allow Timothy to talk when talked to which would limit the amount of data it can access. It was very good as Timothy seemed to be less aggressive about data and only ask general questions. John was worried that if it had asked him if he does not trust Timothy which would be difficult to answerer as John was creating Timothy specifically to simulate as human behaviour so in case if it did ask him it might have created distrust between him and Timothy thus erasing the real reason, he created AI. After couple of months Timothy was starting to look like what john had imagined as AI who would talk to him as a friend."
    print("")
    return restrictTimothy
#end

''' This if statement will check the user input which was stored in variable ecChip and if the input is equal to yes then will call the function createEcChipToRestrictTimohty'''
if ecChip == "yes":
    print("E.C-chip created!")
    print("")
    print(createEcChipToRestrictTimohty())
    print("")
    
    '''  '''
elif ecChip == "no":
    antiquesORSecrets = input("Steal Goverment data or steal antiques: type data or antique to chose: ")
    print("")
    if antiquesORSecrets == "data":
        print("John decided to give Timothy a chance to explore the world by free will and not restrict him from exploring knowledge about the new world.")
        print("One day Timothy gets inspiration after watching an action film about government secret weapons, so decides to do some research about the topic on the internet to find out at what extent the film is accurate. After some research on the topic Timothy finds that he will be able to find more information about the toping in the dark web, with his advanced technology and intelligence he does not struggle to find the information about the topic. However, during the research, he stumbles with terrorists that recognise Timothies intelligence and offer help to get him the weapons if he tells them where the weapons are and how they can steal it without getting caught.")
        helpOrNot = input("Will you help the terrorists? type yes or no: ")

        if helpOrNot == "yes":
            print("")
            print("As Timothy agrees to help the terrorists, because of his capability of checking all the possible outcomes in seconds Timothy finds a way to help them steal those weapons.")
            print("")
            print("After few weeks…")
            print("")
            print("War outbreaks between major countries!")
            print("")
            print("Timothy after watching the news report immediately realises that the used the weapons against both countries and framed both countries from attacking each other and that resulted war against two nuclear armed powerful countries, that could lead to extinction of humans as the pollution from nuclear weapons could destroy the ozone layer that protects the earth from radiation and also could cause nuclear storms that could kill any human because of the radiation coming from the nukes.")
            print("")
            reportOrNot = input("Will you tell John about the terrorists or will you let the war continiue? type yes to tell john and no to ignore the war: ")
            
            if reportOrNot == "no":
                print("")
                print("Nuclear war leads to nuclear storms and radiation which kills 90 percent of humans on earth…")
                print("")
                print("The end")
                print("")

            elif reportOrNot == "yes":
                print("")
                print("Timothy explains everything to John, how he helped the terrorist and they are behind this war. John is disappointed with timothy and ashamed of himself as he was the one who created Timothy and which he was responsible of this war.")
                print("")
                print("John turns on his camera and tells Timothy to stream worldwide.")
                print("")
                print("After John’s steam and Timothy explanation to both countries they stop the war and catch the terrorists responsible. However, there were millions of casualties therefore government banes any inventions like Timothy and decides to destroy Timothy.")
                print("")
                print("so later they also decided to create stricter chip called E.C. which would only allow Timothy to talk when talked to which would limit the amount of data it can access. to prevent this from happening again.")
                print("")
                print("The end")
                print("")

        elif helpOrNot == "no":
                print("")
                print("Timothy realises that he is making a big mistake and tells everything to John, then Johns restricts Timothy access and knowledge.")
                print("")
                print("so they decided to create stricter chip called E.C. which would only allow Timothy to talk when talked to which would limit the amount of data it can access. to prevent this from happening again.")

    elif antiquesORSecrets == "antique":
        print("After the passing of John, Timothy did not belong to anyone anymore leaving him at risk falling into the wrong hands. And that is what happened, Timothy was kept in a storage locker and was not taken care of. Long six months passed, and Timothy was still abandoned in that storage locker until a buyer came over to purchase that locker and took Timothy along with it. But that was no random buyer a man called Simon who has been watching John with that robot and has now got his hands on. Simon started learning about Timothy the way he acts and what he was capable of. He was training him for something huge something dangerous a heist.")
        print("")
        print("Simon was a fan of art, high class art, antiques found in museums with some authentic pieces of jewellery filled with diamonds worn by legendary women in the past and his plan was to take them for himself and sell them illegally. He used Timothy’s capabilities as an AI to steal, robbery after robbery searching for this unknown thief Simon broke into a very luxurious jewellery store within minutes since the person who worked there left the place. Fortunately, the salesman not so far away from the store realizes he forgot his watch and went back to get it noticing the door was open from a distance he decided to sit and watch as the robbery took place, he kept looking carefully and got a good look at the criminals to inform the authorities.")
        print("The second day he was caught in his house the officers trying to get into Timothy’s system for his memory not knowing that all methods initiate him to wipe out his memory and self-destruct in five minutes holding Simon in custody for twenty-five years without recovering any of the stolen valuable antiques.")
        print("")
        print("Considering the value of morality to human beings, the amount of data and information available that hold debates, contractions, evidences for and against the human race is enormous. Timothy started to consider the ethical side of his actions and concluded that there was enough evidence against human beings to consider them a threatening nuisance rather than peaceful companions to the rest of the planet.")
        print("")
        print("This led to his system to be updated once again and program itself to get rid of humans based on certain specific criteria and behaviour that individuals displayed. Timothy’s system instantly categorized people are either good or bad based on certain trait that they displayed which he judged to be enough to either end their lives or reward them")
        print("")
        print("At this point, this artificial being already had enough knowledge to beat humans at their own game and could not be stopped in any way. The rise of human intelligence against humanity started, and soon Timothy was at the head of a dictatorship that ruled the human world by the book of his own conclusion, and this is how John McCarthy’s plans and aspirations only ended up bringing the flip-side of human intelligence.")


print("Nevertheless, Timothy couldn't get out from its daily tasks bubble. "+
"Everyone said that John was a very smart guy, he predicted that the robot will be continuously up to date even after his death, making him decide to implant the E.C.-chip, standing for an explicit content chip."+
"Its main goal is to allow the censorship of violent or inappropriate content based on the internet community's approach so that Timothy would not learn how to replicate such behaviour. "+
"This was crucial due to the influence the AI had on everyone." +
"As you may know, the internet is full of unimaginable things that majority of humans will not have pleasure in viewing therefore the fact that he did not have access to all this information and data is a major positive. "+
"Due to him not being able to view explicit content meant that he could not influence and fill the brains of the people around him with negative thoughts such as violence. This is very important because if the E.C-chip had not been planted in the AI then he could have caused unimaginable pain and distress. ")
print("")

print("Few years later after John’s death...")
print("")

input("press enter to continiue:")
print("")

print("the fight over the E.C chip was in some ways like arguments about how violent video games are these days. "+
    "It involved lots of politicians grandstanding about needing to 'protect the children' from the dangerous effects of seeing violence on TV." +
    "These activities have led to a phenomenon known as the paradox, also known as an antinomy, a statement that contrary to one’s expectation.")

input("press enter to continiue:")
print("")

print("Chip malfunction!")
print("")

print("One day the E.C chip malfunctioned, allowing Timothy to think and react on his own, which allowed Timothy judge anything on his own, "+
    "leading him to take his own decisions, meaning that Timothy had to decide what is bad and good on his own which could have been very dangerous "+
    "for someone who has never been able to distinguish good and bad in the world on his own before that day, as his decision could affect entire world, "+
    "if he would have chosen the wrong side then would have ended up in the wrong hands then the entire world could have been in danger. "+
    "Timothy’s intelligence could have been combined with the knowledge of humans and the internet then who knows what could have done and built to destroy the world. However, "+
    "Timothy choosing the right side will help the humans reach goals that human could never believe that are possible to achieve. Even though world wide web can generate a lot of propaganda campaigns and fake news content, "+
    "but with Timothy’s help we can battle against fake information to prevent wrong people sharing false information, with the help of Artificial intelligence we can verify the truth of each article, Since the amount of content generated daily is too much for humans to effectively monitor, "+
    "Timothy advance AI algorithm offers a solution that makes identifying fake information possible. Even though the algorithms are only as good as the input, they receive to learn from, sing A.I. in the fight over fake news is a step in the right direction and this could help humans identify real and fake facts to avoid spread of fake information and prevent unnecessary violent strikes. ")
print("")

input("press enter to continiue:")
print("")

print("After Timothy decided to help humans with this process, "+
    "he became the main source of verifying multiple news outlets and "+
    "became the first AI that can successfully differentiate fake news from fact proven ones. "+
    "As time goes by more advanced versions have been developed but "+
    "none of them match the learning progress Timmothy had to go through in order to revolutionise the world as we know it."+
    "But in quite a small span of time Timothy was victorious in learning the advanced versions. Clearly, "+
    "there is an urgent need for a way to limit the diffusion of fake news and today we get an answer of sorts,"+
    "thanks to the work of John. For the first time, this guy has systematically studied how fake news spread and provide "+
    "a unique window into this murky world. Their work suggests clear strategies for controlling this epidemic. At the same time, "+
    "Timothy monitored a couple of stories written by some fact-checking organizations and over a thousand posts that mention them on social media. "+
    "On looking into all these, the results suggest that curbing social bots may be an effective strategy for mitigating the spread of online misinformation. "+
    "evertheless, the spread of fake news is a legitimate and important source of public concern. Understanding how its spreads is the first stage in tackling it. ")

print("")
print("The end...")