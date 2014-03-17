__author__ = 'Jonathan' 
import threading, time, sys 

class Listen:
	def __init__(self):
 		print "Choose a direction. Forwards (1) or Backwards (2) or to quit type '3' " 
 		direction = 0 def run (threadName): 
 			while 1==1 : 
 				print "%s Listening for direction: " %(threadName) 
 				direction = input time.sleep(1) 
 				if (direction != 1 or 2):
 					print "You entered a incorrect value" 
 				elif (direction=='quit'):
 					break thread.exit() 
 				else: 
 					return direction 

class Store: 
	def __init__():
		def run (threadName, direction): 
			print "%s %s" %(threadName, direction) 
			


l = Listen() 
s = Store() 
listeningThread = threading.Thread(target=l.run, args=())
storingThread = threading.Thread(target=s.run, args=()) 
listeningThread.start() 
storingThread.start()