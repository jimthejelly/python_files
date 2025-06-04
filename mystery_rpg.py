from datetime import time

def choice(choices):
    for i in range(len(choices)):
        print(str(i+1) + ") " + choices[i])

    choice_outcome = input("\nYour response: ").strip()

    print("-> " + choices[int(choice_outcome)-1] + "\n")
    return(int(choice_outcome))

victim = ""
culprit = ""
location = ""
people = ["Mrs. Null", "Col. Kernel", "Mrs. Esther", "Dr. Queue", "Miss Sudo", "Mr. Byte"]
people_trust = [0, 0, 0, 0, 0, 0]

current_time = time(hour=0, minute=0)

## Opening ##
print("Lightning. Thunder. A mansion on a cliff.")
print("Someone will die tonight. Can you stop the crime before it's too late?")

print("The Python Files...")
name = input("Enter your name to start: ")
name = name.lower()
name = name[0].upper() + name[1:]

print("\n========================================================================\n")

## Set up ##
current_time = time(hour=18, minute=55)
print("*** CURRENT TIME... " + current_time.strftime("%H:%M") + " ***\n")

print("You walk up to the grand doors of the mansion, invitation letter in hand.")
print("Mrs. Null greets you at the door. She looks at you with thinly disguised irritation.\n")
next_scene = input("((Press enter to unpause the text))\n")
print("     'You are late, Detective " + name + ".'\n")

choice1 = ["Terribly sorry, Ma'am. Weather's bad, you understand.", "My invitation begs to differ. It clearly reads 19:00.", "Sorry, is this not the creepy mansion on the hill?"]
print("((Pick a response: 1, 2, 3))")
response1 = choice(choice1)

if(response1 == 1):
    people_trust[0] += 7
    print("Mrs. Null clicks her tongue understandingly. She nods.")
    next_scene = input("")
    print("     'Hmm. Well, that's reasonable, I suppose. You best hurry in there, Detective. Everyone's already here and waiting.'")
elif(response1 == 2):
    people_trust[0] += 7
    print("Mrs. Null raises her eyebrow and snatches the letter from your hand.")
    next_scene = input("")
    print("     'I would never have made a mistake on your invitation!'")
    print("She pauses.")
    next_scene = input("")
    print("     'Oh. I... My apologies, Detective. It seems your letter truly does say 19:00... That's quite odd, considering I penned it myself... Ah, well, either way, everyone else is waiting inside. Please make your way in.'")
elif(response1 == 3):
    people_trust[0] += 7
    print("Mrs. Null looks at you with exasperation.")
    next_scene = input("")
    print("     'If you are done making unnecessary comments, Detective, everyone is inside, and you are in fact, quite late. If I were you, I wouldn't waste more of everyone else's time by standing out here in the rain.'")

print("\n((To go to the next scene, hit enter.))")
next_scene = input("")

print("========================================================================\n")

## Entrance of Mansion ##
current_time = time(hour=19, minute=00)
print("*** CURRENT TIME... " + current_time.strftime("%H:%M") + " ***\n")

print("You make your way into the mansion. The opulence immediately strikes you. Mrs. Null is completely unfazed. She continues to lead you deeper into the house, eventually stopping in the Parlour.")
print("You see a stocky, aged man looking pensively into the fireplace. He seems to be contemplating something.")
print("He is decked out in full military attire, his chest decorated with countless medals and shiny trinkets. He turns to you as the door opens and smiles widely.")
next_scene = input("")
print("     'My friend, how are you this good evening? I daresay you look better than I recall back then, in the midst of Operation Echo.'")
print("You shift in place, unsure how to respond.\n")

choice2 = ["Ah yes, I see you've attained even more awards since then. You were always the most outstanding of our team.", "You look very fine yourself, are you enjoying your retirement?", "Operation Echo? You must be mistaken, I was never a part of the military."]
response2 = choice(choice2)

if (response2 == 1):
    people_trust[1] += 5
    print("The colonel laughs boistrously and claps you on the back.")
    next_scene = input("")
    print("     'I knew there was a reason you were my favorite, old pal. What say we go get a drink after this and catch up on the good times?'")
elif (response2 == 2):
    people_trust[1] += 2
    print("He looks down appraisingly at himself, drawing your gaze again to the proof of all of his accomplishments.")
    next_scene = input("")
    print("     'I should hope so, I still follow protocol even after the end of active duty. A real soldier never retires. It seems you've moved on rather fast.'")
elif (response2 == 3):
    people_trust[1] -= 1
    print("He looks you up and down, scrunching his nose with distaste.")
    next_scene = input("")
    print("     'Ah, so not military then. I don't know how I could have been so mistaken.'")

print("Mrs. Null watches the interaction in boredom. Before you can formulate a fitting response, she gestures for you to hurry along.")
next_scene = input("")
print("     'Apologies, Detective, but we are in a bit of a rush. Due to your tardiness, Mr. Byte has been waiting expectantly for your arrival.'")
print("The colonel frowns, tilting his head at Mrs. Null's words.")
next_scene = input("")
print("     'I'm sure Silas can wait five minutes, I know he's a busy man - believe me, he's made that all too clear - but what's a mere five minutes for a friend?'")
print("Mrs. Null seems to catch some undertone that you don't understand the implications of. She gives him a haughty look and walks off. You hesitatingly follow her.")

next_scene = input("")

print("========================================================================\n")

## Library ##
current_time = time(hour=19, minute=10)
print("*** CURRENT TIME... " + current_time.strftime("%H:%M") + " ***\n")

print("You are led into the next room, which turns out to be the master library. It is a large room filled with books from ceiling to floor. You observe that the genres range from scientific journals to self-help novels.")
print("Mrs. Null clears her throat and you look forward to see a stately, well-dressed woman seated in a plush armchair. In her lap rests a thick tome that you can't see the title of.")
next_scene = input("")
print("     'Good evening Madam Esther, may I introduce to you Detective " + name + ". They are here for an audience with the master regarding the recent security issues.'")
print("Mrs. Esther eyes Mrs. Null over her glasses before turning her gaze upon you. You feel the judgement radiating from her silently. She addresses Mrs. Null without taking her eyes off of you.")
next_scene = input("")
print("     'And why would you think to hire a detective and not, for instance, a bodyguard if my husband's personal security is in question?'")
print("You can see that Mrs. Null does not have a readily prepared response, so you take it upon yourself to jump to her defense.\n")

choice3 = ["I can assure you madam, my caliber of detective is unmatched. I am here not only for your husband's security, but naturally the lady of the house as well. I am completely at your disposal.", "As you say, madam, I am here purely in an investigative position in order to confirm any danger. After my job here is done, hiring a bodyguard would be my first recommendation if there is a threat.", "Evidently, nobody as of yet has an idea to the invisible spectre looming over this house which is why I was called. Investigation into wrongful doings is my job, after all."]
response3 = choice(choice3)

if (response3 == 1):
    people_trust[2] += 5
    print("Mrs. Esther finally rises from her chair, setting the book down. She approaches you gracefully and clasps your hand in hers.")
    next_scene = input("")
    print("     'What a charming investigator, I am pleased to make your acquaintance and look forward to discussing your role here in the future.'")
    print("Mrs. Null titters awkwardly, saving you from having to respond to the offer of private employment. She clearly regrets having started the conversation.")
    next_scene = input("")
    print("     'Well, we must be going. We mustn't hold up the master by exchanging pleasantries. Wonderful to see you, madam, I'm sure the good detective would enjoy carrying on this conversation after dinner.'")
    print("She half curtsies, and turns to leave, ushering you along with her.")
elif (response3 == 2):
    people_trust[2] += 1
    print("Mrs. Esther nods distractedly, already peering back down at the page she had open. Her silent dismissal rings loud. Mrs. Null doesn't seem to take it to heart and ushers you out of the library.")
elif (response3 == 3):
    people_trust[2] -= 3
    print("Mrs. Esther purses her lips and shuts the book close, putting it down on an endtable next to her chair. She stands up and briskly walks past the two of you.")
    next_scene = input("")
    print("     'I can assure you, detective, that you will find nothing besides the obvious out of place here. Our family is always dedicated to the pursuit of truth and justice.'")
    print("She must read something on your face because she pauses and elaborates unprompted.")
    next_scene = input("")
    print("     'The obvious being the death threat letter that my husband received a couple of days ago. I'm sure you must already know of it. I promise you however that this is a rare exception to the stability of this house.'")
    print("With this final proclamation, she continues on and leaves the library. You can hear the click of her heels on the marble floor in the hallway. It isn't until they are so faint you are sure she isn't coming back that you step forward to take a look at the book she was reading.")
    print("It has a dark cover, but the title and image are so worn away that you cannot make them out. The author's name, however, is still barely legible and you recognize as a famous mystery novelist.")

next_scene = input("")

print("========================================================================\n")

## Dining Room ##
current_time = time(hour=19, minute=20)
print("*** CURRENT TIME... " + current_time.strftime("%H:%M") + " ***\n")

print("The dining room is just as grandiose and")