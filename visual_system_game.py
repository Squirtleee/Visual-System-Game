#Plot: Start from the 3 pathways--LGN(vesicle event)--ventral/dorsal stream(intro V1~V2)(hint event)--numberlock--finalwin

#----------Import----------------#
import random
import time
from os import sys

#----------parameters and global variables----------------#
Roles = ['Sleepy action potential','Lazy action potential','Happy action potential','Nerdy action potential']			
HP = [3000,3000,3000,3000] 	
firstHPs=[3000,3000,3000,3000]
Lifes = [2,2,2,2]
HP = 0								
Life = 0							
Role = 'NONAME'
level = 1							
XP = 0								
#----------three levels----------------#
def level1():
	global XP
	global HP
	print('*************************')
	Q1=['What color does the L-M pathway code for?\n\n1.black and white\n2.yellow and blue\n3.red and green\n4.not color, it codes for brightness','Visual signal from our left eye goes to ____\n\n1.right hemisphere\n2.left hemisphere\n3.cerebellum\n4.left and right hemisphere','Humans have __ types of cones\n\n1.one\n2.two\n3.three\n4.infinite','Where on our retina has the highest color sensitivity?\n\n1.peripheral\n2.optic disk\n3.fovea\n4.all parts have equal color sensitivity','M cone has the highest sensitivity towards the color\n\n1.blue\n2.green\n3.red\n4.yellow','Where on our retina is our visual blindspot?\n\n1.optic disk\n2.fovea\n3.humans do not have blind spots\n4.our entire retina is a huge blind spot']
	A1=[3,4,3,3,2,1]
	items = range(6)                 #six questions
	nums = random.sample(items,6)    
	for i in nums:
		print(Q1[i])
		ans= int(input('Your answer (enter a number):'))
		if ans==A1[i]:
			time.sleep(0.5)
			print("Successfully travel to the next neuron,+1000XP")
			print(' ')
			time.sleep(1)
			XP += 1000
			if XP ==3000:
				win()
		else:
			time.sleep(1)
			print('Not enough sodium ions to boost action potential! the correct answer is',A1[i],',-1000HP')
			time.sleep(1)
			print(' ')
			HP-= 1000
			if HP == 0:
				global Life
				Life -= 1
				if Life == 0:
				  time.sleep(1)
				  print('Hop-hop blocked you on instagram, Life-1')
				  gameOver()
				else:
				  time.sleep(1)
				  print('Hop-hop unfollowed you on instagram, Life-1')
				  print('Current Life',Life)
				  print(' ')
				  HP+=3000
    
#----------levels----------------#
def level2():
	global XP
	global HP
	print('*************************')
	Q2=['What color does the L+M-S pathway code for?\n\n1.black and white\n2.yellow and blue\n3.red and green\n4.not color, it codes for brightness','Dory from the movie "Finding Nemo" suffers from ____\n\n1.overly optimistic disease\n2.dementia\n3.long term memory loss\n4.short term momory loss','Humans have _____ cerebrum\n\n1.one\n2.two\n3.thousands\n4.millions','Where on our retina is our visual blind spot\n\n1.optic disk\n2.fovea\n3.our entire retina is a huge blindspot\n4.we do not have a blind spot','S cone has the highest sensitivity towards the color ____\n\n1.black\n2.green\n3.red\n4.blue',"You are now an action potential inside a ____\n\n1.pencil\n2.apple\n3.neuron\n4.phone"]
	A2=[2,4,1,1,4,3]
	items = range(6)                 #six questions
	nums = random.sample(items,6)    
	for i in nums:
		print(Q2[i])
		ans= int(input('Your answer (enter a number):'))
		if ans==A2[i]:
			time.sleep(0.5)
			print("Successfully travel to the next neuron,+1000XP")
			print(' ')
			time.sleep(1)
			XP += 1000
			if XP == 3000:
				win()
		else:
			time.sleep(1)
			print('Not enough sodium ions to boost action potential! the correct answer is',A2[i],'-1000HP')
			time.sleep(1)
			print(' ')
			HP-= 1000
			if HP == 0:
				global Life
				Life -= 1
				if Life == 0:
				  time.sleep(1)
				  print('Hop-hop blocked you on instagram, Life-1')
				  gameOver()
				else:
				  time.sleep(1)
				  print('Hop-hop unfollowed you on instagram, Life-1')
				  print('Current Life',Life)
				  print(' ')
				  HP+=3000



#----------levels----------------#
def	level3():
	global XP
	global HP
	print('*************************')
	Q3=['What color does the L+M+S pathway code for?\n\n1.black and white\n2.yellow and blue\n3.red and green\n4.not color, it codes for brightness','L cone has the highest sensitivity towards the color ____\n\n1.black\n2.green\n3.red\n4.blue','Humans have _____ eyes\n\n1.one\n2.two\n3.three\n4.four','Humans have ____ cerebellum\n\n1.one\n2.two\n3.three\n4.four','Humans have __ cerebral hemispheres\n\n1.one\n2.two\n3.three\n4.four','What signals are cones primarily responsible for?\n\n1.colors\n2.brightness\n3.sounds\n4.odors']
	A3=[1,3,2,1,2,1]
	items = range(6)                 
	nums = random.sample(items,6)    
	for i in nums:
		print(Q3[i])
		ans= int(input('Your answer (enter a number):'))
		if ans==A3[i]:
			time.sleep(0.5)
			print("Successfully travel to the next neuron,+1000XP")
			print(' ')
			time.sleep(1)
			XP += 1000
			if XP == 3000:
				win()
		else:
			time.sleep(1)
			print('Not enough sodium ions to boost action potential! the correct answer is',A3[i],',-1000HP')
			time.sleep(1)
			print(' ')
			HP-= 1000
			if HP == 0:
				global Life
				Life -= 1
				if Life == 0:
				  time.sleep(1)
				  print('Hop-hop blocked you on instagram, Life-1')
				  gameOver()
				else:
				  time.sleep(1)
				  print('Hop-hop unfollowed you on instagram, Life-1')
				  print('Current Life',Life)
				  print(' ')
				  HP+=3000
		

#----------Choose a Role----------------#
def chooseRole():
	global Role
	global HP
	global Life

	choose = input('Press enter to start ➽  ')
	k = random.randint(0,3)		
	Role = Roles[k]
	HP += firstHPs[k]
	Life = Lifes[k]
	print('Your character:', Role)

#----------SHOW GAME MESSAGE----------------#
def showGameMessage():
  print("Welcome to Hop-hop's visual system!")
  time.sleep(2)
  print("Once upon a time, a bug accidently flew into Hop-hop's eye")
  time.sleep(2.5)
  print("Being one of his friends, you must turn into an action potential warrior and enter Hop-hop's visual system")
  time.sleep(2)
  print("Find the bug and DESTROY it!")
  time.sleep(2.5)
  print("Good luck, player.")
  print('----------------------------------')
  time.sleep(3)
  print("In this game, you will start at Hop-hop's cones.")
  print("Cones are cells located on our retina responsible for processing color information")
  time.sleep(4)
  print("S cones primarily process short wavelength signal, which is mostly caused by the color blue.")
  print("M cones primarily process medium wavelength signal, which is mostly caused by the color green.")
  print("L cones primarily process long wavelength signal, which is mostly caused by the color red.")
  time.sleep(6)
  print("Different visual pathways, through combining and comparing signals from these cones")
  time.sleep(2)
  print("Give humans the ability to make sense of colors")
  time.sleep(2)
  chooseRole()

	

#----------Show Status----------------#
def showStatus():
	print('*************************')
	print('Current HP:',HP)
	print('Current Life:',Life)
	print('Current XP:',XP)	
	print('*************************')

#----------cloose level----------------#
def chooseLevel():
	global level
	print("*************************")
	print("Which pathway do you choose?")
	print("1:L-M (Codes for the color red and green) {difficulty:advanced}")
	print('2:L+M-S (Codes for the color yellow and blue) {difficulty:medium}')
	print('3:L+M+S (Codes for the color black and white) {difficulty:easy}')
	print("0:I don't wanna play. Let's quit.")
	print('*************************')
	level = int(input('Your choice (enter a number):'))

#----------GAME OVER----------------#
def gameOver():
	print('You failed.\nHop-hop is no longer your friend, and he will also unfollow you on Instagram.')
	sys.exit()
#WIN
def win():
	print("Great job! You've successfully traveled to LGN.")
	time.sleep(3)
	print("LGN stands for Lateral Geniculate Nucleus, and it is located on our thalamus.")
	time.sleep(3)
	print("LGN is essential to our visual system")
	time.sleep(2)
	print("It connects optic nerves (nerves carrying visual signals from retina) to the occipital lobe (brain's visual processing center)")
	time.sleep(4)
	print("Our LGN is normally described as having six distinctive layers.")
	time.sleep(3)
	print("Magnocellular layers receive inputs from the rods (which is primarily responsible for detecting difference in brightness).")
	time.sleep(3)
	print("Parvocellular layers receive inputs from long and medium wavelength cones.")
	time.sleep(3)
	print("Koniocellular layers receive inputs from short wavelength cones.")
	print('---------------------------------------')
	time.sleep(3)
	if input("Do you wish to continue your journey?(enter 'yes')")=='yes':
		win2()

#----------V1~V3---------------------------------#
def v1():
  print('---------------------------------------')
  print("You are now at the V1 processing layer.")
  time.sleep(2)
  print('V1 is highly associated with motion processing')
  time.sleep(2)
  print("V1 has a very precise space map\nThat means the correspondence between a specific location in V1 and in the human visual field is very precise")
  time.sleep(3.5)
  print("In primates, V1 marks out what is important in our visual input, and this helps guide primates' shift of attention")
  time.sleep(2)
  print("In general, the tasks which V1 perform are simpler than the latter layers")
  time.sleep(2)
  print("At V1, the difference between ventral and dorsal stream isn't yet significant")
  time.sleep(2)
  if input("Ready to continue your journey?(enter 'yes')")=='yes':
    v2()

def v2():
  print('---------------------------------------')
  print("Right when you're trying to enter V2 processing layer, you get stopped at the axon terminal")
  time.sleep(2)
  print("Axon terminal is a place in the neuron where you initiate the release of neurotransmitters and begin your journey in the next neuron")
  time.sleep(2)
  print("Suprisingly, you find out that you've gotten stopped by a weeping potassium ion")
  time.sleep(3)
  print("The potassium ion begs you to give him the magic to turn him into a sodium ion")
  time.sleep(2)
  print("Because action potentials, like you, are mostly caused by an influx of sodium ions into neurons")
  time.sleep(2)
  print("This potassium ion thinks that being one of you gives him a purpose")
  time.sleep(3)
  print("No matter whether you wish to help him or not, remember, choose WISELY.\n")
  time.sleep(2)
  sod=int(input("Are you willing to help this poor potassium ion?\n1.YES!!Help him\n2.Nope!!This is kind of suspicious\n3.I'll wipe his tears but won't give him my magic\n"))
  if sod ==1:
    print('---------------------------------------')
    print("You chose to give him part of your magic.")
    time.sleep(2)
    print("Helping others is indeed a great and powerful move")
    time.sleep(2)
    print("You helped this potassium ion to finally reach his dream and turn into a sodium ion")
    time.sleep(3)
    print("In order to show his gratitude")
    time.sleep(2)
    print("This new sodium ion left you a hint before he left")
    time.sleep(2)
    print('He said, "Being hideous is the true beauty, only in hideosity will you find simplicity"')
    time.sleep(3)
    print("Although these words probably make no sense")
    time.sleep(2)
    print("You've decided to remember them either way since these words sound really deep")
    time.sleep(3)
    if input("Ready to enter V2?(enter 'yes')")=='yes':
      print("-----------------------------------------")
  elif sod==2:
    print("---------------------------------------")
    print("You chose to turn him down")
    time.sleep(2)
    print("Being conservative sometimes brings you safety, other times it can cost you an opportunity")
    time.sleep(2)
    print("Anyway, although you've disappointed this poor potassium ion")
    time.sleep(3)
    print("You've safely gone past him")
    time.sleep(2)
    if input("Ready to enter V2?(enter 'yes')")=='yes':
      print("-----------------------------------------")
  else:
    print("---------------------------------------")
    print("You chose to give this poor potassium ion warm hugs")
    time.sleep(2)
    print("Instead of giving him your magic")
    time.sleep(2)
    print("You told him that action potentials are actually made possible because of them, the potassium ions")
    time.sleep(3)
    print("After every action potential come the outflow of potassium ions")
    time.sleep(2)
    print("Due to the outflow of potassium ions, neurons are able to return to their normal resting state")
    time.sleep(2)
    print("Without potassium ions, the next action potential wouldn't be created because neurons couldn't return to their original state")
    time.sleep(3)
    print("Your words have truly comforted this poor potassium ion")
    time.sleep(2)
    print("In order to show his gratitude")
    time.sleep(2)
    print("This new sodium ion left you a hint before he left")
    time.sleep(3)
    print('He said, "Being hideous is the true beauty, only in hideosity will you find simplicity"')
    time.sleep(2)
    print("Although these words probably make no sense")
    time.sleep(2)
    print("You've decided to remember them either way since these words sound really deep")
    time.sleep(3)
    if input("Ready to enter V2?(enter 'yes')")=='yes':
      print("-----------------------------------------")

  print("You are now at the V2 processing layer.")
  time.sleep(2)
  print("Starting here, the visual processing layers of the ventral and dorsal stream carry out different tasks")
  time.sleep(2.5)
  print("V2 is split into four sections: dorsal and ventral stream on both the right and left hemisphere")
  time.sleep(2)
  print('These sections receive processed signals from V1\nThey then send their processed signals down to V3,V4,and V5\n')
  time.sleep(3.5)
  print("V2 is highly associated with:\nProcessing complex visual orientation\nBinocular disparity (which contributes to human's sense of depth)\nFigure ground configuration (decide what is figure and what is background)")
  time.sleep(5)
  print("V2 also contributes to attention guidance, just like V1")
  time.sleep(2)
  v3()

def v3():
  print('---------------------------------------')
  print("Hope now you have a  general concept on how visual signals are processed.")
  time.sleep(2)
  print("Every layer performs more sophisticated tasks than the previous layers.")
  time.sleep(2)
  print("For ventral and dorsal stream, they each have to go through approaximately five or six visual processing layers")
  time.sleep(2)
  print("Now, you will quickly travel through the rest of the processing layers and reach your final destination.")
  time.sleep(3)
  if input("Ready to continue your journey?(enter 'yes')")=='yes':
    numlock()

#----------ventral\dorsal stream----------------#
def streams():
  print('---------------------------------------')
  print("You have reached the visual cortex")
  time.sleep(1.5)
  print('Whcih processing stream do you wish to enter? (enter a number)')
  print('1. Ventral Stream: responsible for object recognition')
  print('2. Dorsal Stream: responsible for human spatial navigation')
  def ven():
    print('---------------------------------------')
    print("Welcome to ventral stream! Ventral stream is mainly associated with object recognition!")
    time.sleep(2)
    print("Visual signals traveling the ventral stream will start from our primary visual cortex (V1)\nThan they'll travel down our visual processing layers(V2,V3...), at last they arrive at our temporal lobe")
    time.sleep(3.5)
    print('Ventral stream is also called the "what" stream\nIt is linked to the medial temporal lobe (stores long-term memories), the limbic system (controls emotions), and the dorsal stream(spatial navigation)')
    time.sleep(3.5)
    print("Damage to the ventral stream can cause inability to recognize faces or interpret facial expression")
    time.sleep(2)
    if input("Ready to continue your journey?(enter 'yes')")=='yes':
     v1()

  def dor():
    print('---------------------------------------')
    print("Welcome to the dorsal stream! Dorsal stream is mainly associated with spatial navigation")
    time.sleep(2.5)
    print("Visual signals traveling the dorsal stream will start from our primary visual cortex (V1)\nThan they'll travel down our visual processing layers(V2,V3...), at last they arrive at our parietal lobe")
    time.sleep(3.5)
    print('The posterior parietal cortex is mostly responsible for perceiving spatial relationships and coordinating the human body')
    time.sleep(3.5)
    print('Dorsal stream is also called the "what" stream\nIt is highly connected with the ventral stream which performs object recognition')
    time.sleep(3.5)
    print("Damage to the dorsal stream can cause inability to perceive motion")
    time.sleep(2.5)
    if input("Ready to continue your journey?(enter 'yes')")=='yes':
      v1()

  if int(input('Your choice?'))==1:
    ven()
  else:
    dor()


def win2():
  print('-----------------------------')
  print("But right when you're trying to leave LGN")
  time.sleep(2)
  print("A group of stubborn vesicles refuse to release their neurotransmitters")
  time.sleep(2)
  print("If neurontransmitters are not released, action potentials, like you, can't travel to the next neuron")
  time.sleep(3)
  print("Luckily, you have a few weapons at hand, and if you choose wisely, you might be able to make the stubborn vesicles cooperate")
  print("-------------------------------")
  time.sleep(3)
  print('1.arrow\n2.karaoke machine\n3.banana')
  print("-------------------------------")
  def event1():
    print("GOOD CHOICE!")
    time.sleep(1)
    print(Role,"takes an excellent aim at the stubborn vesicles' leader")
    time.sleep(2)
    print("Fires an amazing shot")
    time.sleep(1.5)
    print("The arrow penatrated stubborn vesicles' leader")
    time.sleep(2)
    print("Challenge Succeeded！")
    streams()
		
  def event2():
    print("AWFUL CHOICE!")
    time.sleep(1)
    print("The truth is, everybody knows that",Role,"can not sing")
    time.sleep(2)
    print("Even though you've really tried your best")
    time.sleep(2.5)
    print("You still couldn't defeat the stubborn vesicles' leader")
    time.sleep(2.5)
    print("Even the karaoke machine thinks that you're horrible at singing")
    time.sleep(2.5)
    print("At last")
    time.sleep(1)
    print(Role,"was defeated")
    time.sleep(2)
    print("And gave up and left")
    time.sleep(1)
    gameOver()
  
  def event3():
    print("EXCELLENT CHOICE!")
    time.sleep(1)
    print(Role,"pulled out a golden banana")
    time.sleep(2)
    print("The stubborn vesicles' leader laughed hysterically")
    time.sleep(2)
    print("While the stubborn vesicles' leader wasn't paying attention and not taking you seriously")
    time.sleep(2.5)
    print("You took a perfect aim at the stubborn vesicles' leader's head")
    time.sleep(2)
    print("Throw the golden banana towards him")
    time.sleep(2)
    print("When the banana hits him, the stubborn vesicles' leader screamed and passed out immediately")
    time.sleep(2)
    print("Congratulations! You beat the stubborn vesicles' leader with the golden banana")
    time.sleep(2.5)
    print("Challenge Succedded!")
    streams()
  a=int(input('Please select a weapon (enter "1" or "2" or "3"):'))
  if a==1:
    event1()
  elif a==2:
    event2()
  else:
    event3()
		

def finalwin():
  time.sleep(2)
  print("Congratulations on saving Hop-hop!")
  time.sleep(2)
  print("You have reached the end of this game")
  print("----------------------------------")
  time.sleep(3)
  print("I sincerely thank you for playing this game")
  time.sleep(2)
  print("Sorry this turns out to be such a waste of time")
  time.sleep(2)
  print("But I still appreciate your effort from the botton of my heart")
  print("----------------------------------")
  time.sleep(3)
  print("Special thanks to Dr. Jay Baraban for the amazing courses")
  time.sleep(2)
  print("Special thanks to instructor Rachel Xian for those really nice lectures and also for making lots of announcements to keep us informed")
  time.sleep(5)
  print("Special thanks to instructor Mike Wang for making really cool jokes in those really cool/amazing videos")
  print("----------------------------------")
  time.sleep(3.5)
  print("Here are my references\nhttps://en.wikipedia.org/wiki/Visual_cortex\nFundamentals of color vision I: color processing in the eye (By: Andrew Stockman and David H. Brainard)")
  print("Module 2--Visual System")
  time.sleep(5)
  print("----------------------------------")
  print("I am Chih-Hsien Huang from Taiwan, and I am the designer of this game")
  time.sleep(3.5)
  print("Best wishes to you in your future")
  time.sleep(2.5)
  print("Take care and have a wonderful day!")
  time.sleep(2)
  sys.exit()

def xAxB():
  ("------------------------------------------")
  print("Here are the game rules")
  print("This system will generate a random 4-digit number, and you need to guess it")
  time.sleep(3.5)
  print("For guessing a correct number at its correct position, you will get an A")
  print("For guessing a correct number at its incorrect position, you will get an B")
  print("------------------------------------------")
  time.sleep(5)
  print("For example, if the correct answer is 1234")
  time.sleep(2)
  print("And if your guess is 3456")
  time.sleep(2)
  print("You will get 0A2B because you have correctly guessed the number 3 and 4")
  print("But you didn't guess their correct position")
  time.sleep(4.5)
  print("And if your guess is 7834")
  time.sleep(2)
  print("You will get 2A0B because you have correctly guessed the number 3 and 4")
  print("And you have also guessed their correct position")
  time.sleep(4.5)
  print("This four-digit number won't have repeating numbers")
  time.sleep(2.5)
  print("For instance, the correct answer won't be 2344 because the number 4 appeared twice")
  time.sleep(2.5)
  print("In order to get the correct password, you must get 4A0B")
  time.sleep(2.5)
  print("Let's activate this CUTE bomb!")
  print("------------------------------------------")

  nums=range(1,10)
  ans=random.sample(nums,4)
  count=0
  while True:
	  guess=input("Guess a 4-digit number: ")
	  count=+1
	  A=0
	  B=0
	  for i in range(4):
	    if ans[i]==int(guess[i]):
	  	  A=A+1
	  for i in range(4):
	  	for j in range(4):
	  	  	if ans[i]==int(guess[j]):
	  	  	  if i!=j:
	  	  	  	B=B+1
	  if A==4:
	  	  print("Correct!!!")
	  	  time.sleep(0.5)
	  	  print('Bomb activated! Hop-hop saved!')
	  	  time.sleep(0.5)
	  	  print("You are truly Hop-hop's best friend")
	  	  finalwin()
	  elif count==25:
	  	  print("You have used up all your chances")
	  	  print("Hop-hop is truly disappointed with your performance")
	  	  time.sleep(1)
	  	  gameOver()
	  else:
	  	  print(A,"A",B,"B")

def numlock():
	time.sleep(1)
	print("------------------------------------------")
	print('Congratulations on making it to the end of this stream! You have reached your final destination!')
	time.sleep(2.5)
	print("You can now see the horrible bug which had flown into Hop-hop's visual system")
	time.sleep(2.5)
	print("Remember, you must defeat it to save Hop-hop")
	time.sleep(2.5)
	print("You see two bombs which you can use to defeat the bug")
	time.sleep(2.5)
	print("In order to activate the bomb, you must enter the correct password")
	time.sleep(3)
	print(Role,", your last mission is to guess the correct password and activate the bomb")
	time.sleep(2.5)
	print("May all neuroscience's force be with you")
	time.sleep(2)
	print("-------------------------------------------")
	print('1.Cute but EXPLOSIVE bomb\n2.Hideous but still EXPLOSIVE bomb')
	bomb=int(input('Which bomb do you choose to activate? (enter "1" or "2")'))
	if bomb==1:
		time.sleep(1)
		xAxB()
	if bomb==2:
		guessnumber()

def guessnumber():
	ans=random.randint(1,200)
	count=0
	while True:
		print("-----------------------------------------")
		g=int(input("Guess the number!(Between 1 and 200)"))
		if count==20:
			print("Your have gussed too many times")
			print("Hop-hop no longer has faith in you and decided to go to an ophthalmologist")
			break
			sys.exit()
		elif g>ans:
			print("Smaller than this")
			count+=1
			print("You have gussed")
			print(count,'time')
			print("-----------------------------------------")
		elif g<ans:
			print("Bigger than this")
			count+=1
			print("You have gussed")
			print(count,"time")
			print("-----------------------------------------")
		else:
			print('-----------------------------')
			print("Correct!You have successfully activated the bomb!")
			print("VICTORY!!!!!!!!!!!!!!!")
			time.sleep(1.5)
			print("You are truly Hop-hop's best friend！！！")
			finalwin()

#----------Start of Main Program----------------#
showGameMessage()
chooseLevel()
showStatus()
if level==1:
  level1()
elif level==2:
  level2()
elif level==3:
  level3()
else:
  print('You choose to quit the game, and now you and Hop-hop will never be friends again.:(:(')
  sys.exit()
