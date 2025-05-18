import string

Nokia = """
Welcome to Nokia
	
MENU	
Select one number:
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM service
	"""

print(Nokia)
customer_choice1 = int(input('Enter number of choice: '))

match(customer_choice1):

	case 1:
		Phonebook = """
		Phone Book
		1. Search
		2. Service Nos.
		3. Add name
		4. Erase
		5. Edit
		6. Assign tone
		7. Send b'card
		8. Options
		9. Speed dials
		10. Voice tags
			"""

		print(Phonebook)
		user_input1 = int(input('Pick your choice: '))

		match(user_input1):

			case 1: print('Search')

			case 2: print('Service Nos.')

			case 3: print('Add name')

			case 4: print('Erase')

			case 5: print("Edit")
			case 6: print("Assign tone")
	
			case 7: print("Send b'card")			
			case 8: 
				Options = """
				Options
				1. Type of view
				2. Memory status
						"""
				print(Options)
				
				user_input2 = int(input('Choose: '))

				match(user_input2):
					case 1: print("Type of view")

					case 2: print("Memory status")
					
					case _: 
						default: print("Invalid Input")

			case 9: print("Speed dials")
		
			case 10: print("Voice tags")	
			
			case _:
				default: print("Invalid Input")



	case 2: 
		Messages = """
		Messages
		1. Write messages
		2. Inbox
		3. Outbox
		4. Picture messages
		5. Templates
		6. Smileys
		7. Message settings
		8. Info service
		9. Voice mailbox number
		10. Service commnad editor
					"""

		print(Messages)
	
		customer_choice2 = int(input('Pick your choice: '))
			
		match(customer_choice2):

			case 1: print("Write messages")
		
			case 2: print("Inbox")

			case 3: print("Outbox")

			case 4: print("Picture messages")

			case 5: print("Templates")

			case 6: print("Smileys")

			case 7: 
				Messagesettings = """
				Message settings
				1. Set 1
				2. Common
					"""

				print(Messagesettings)					
				user_input3 = int(input('Choose:'))
				
				match(user_input3):
					case 1:
						Set1 = """
						Set 1
						1. Message center number
						2. Messages sent as
						3. Message validity
							"""
						print(Set1)
						set = int(input('Pick:')) 
	
						match(set):
							case 1: print("Message center number")

							case 2: print("Messages sent as")

							case 3: print("Message validity")
				
							case _:
								default: print("Invalid Input")	

					case 2: 
						Common = """
						Common
						1. Delivery reports
						2. Reply via same centre
						3. Character support
								"""
						print(Common)
						common = int(input('Choose:'))
	
						match(common):
							case 1: print("Delivery reports")
		
							case 2: print("Reply via same center")

							case 3: print("Character support")
				
							case _:
								default: print("Invalid Input")


						default: System.out.println("Invalid Input")

			case 8: print("Info service")

			case 9: print("Voice mailbox number")

			case 10: print("Service command editor") 


			
	case 3: print("Chat")
			
		

	case 4: 
		CallRegister = """
		Call Register
		1. Missed calls
		2. Received calls
		3. Dialled calls
		4. Erase recent call lists
		5. Show call duration
		6. Show call costs
		7. Call cost settings
		8. Prepaid credit
				"""
		print(CallRegister)
		customer_choice3 = int(input('Choose:')) 
	
		match(customer_choice3):
			case 1: print("Missed calls")

			case 2: print("Received calls")

			case 3: print("Dialled calls")

			case 4: print("Erase recent call lists")

			case 5:
				Showcallduration = """
				Show call duration 
				1. Last call duration
				2. All calls duration
				3. Received calls duration
				4. Dialled calls duration
				5. Clear timers 
						"""
				print(Showcallduration)
				user_input4 = int(input('Choose:'))

				match(user_input4):
					case 1: print("Last call duration")

					case 2: print("All calls duration")

					case 3: print("Received calls duration")

					case 4: print("Dialled calls duration")

					case 5: print("Clear timers")

					case _:
						default: print("Invalid input") 

			case 6:
				Showcallcosts = """
				Show call costs 
				1. Last call costs
				2. All calls cost
				3. Clear counters
						"""
				print(Showcallcosts)
				user_input5 = int(input('Choose:')) 
	
				match(user_input5):
					case 1: print("Last call cost")

					case 2: print("All calls cost")

					case 3: print("Clear counters")

					case _:
						default: print("Invalid input")

			case 7:
				Callcostsettings = """
				Call cost settings 
				1. Call cost limit
				2. Show costs in
						"""
				print(Callcostsettings)
				user_input6 = int(input('Choose:'))

				match(user_input6):
					case 1: print("Cost cost limit")

					case 2: print("Show costs in")

					case _:
						default: print("Invalid input")


			case 8: print("Prepaid credit")
				
			case _:
				default: print("Invalid input")



	case 5: 
		Tones = """
		Tones
		1. Ringing tone
		2. Ringing volume
		3. Incoming call alert
		4. Composer
		5. Message alert tone
		6. Keypad tones
		7. Warning and games tones
		8. Vibrating alert
		9. Screen saver
				"""

		print(Tones)
		customer_choice4 = int(input('Choose:'))
			
		match(customer_choice4):
			case 1: print("Ringing tone")

			case 2: print("Ringing volume")

			case 3: print("Incoming call alert")

			case 4: print("Composer")

			case 5: print("Message alert tone")

			case 6: print("Keypad tones")
	
			case 7: print("Warning and game tones")

			case 8: print("Vibrating alert")

			case 9: print("Screen saver")

			case _: 
				default: print("Invalid Input")



	case 6: 
		Settings = """
		Settings
		1. Call settings
		2. Phone settings
		3. Security settings
		4. Restore factory settings
					"""

		print(Settings)
		customer_choice5 = int(input('Choose:'))
			
		match(customer_choice5): 
			case 1:
				Callsettings = """
				Call settings 
				1. Automatic redial
				2. Speed dialling
				3. Call waiting options
				4. Own number sending
				5. Phone line in use
				6. Automatic answer
						"""
				print(Callsettings)
				user_input7 = int(input('Choose:'))
			
				match(user_input7): 
					case 1: print("Automatic redial")

					case 2: print("Speed dialling")

					case 3: print("Call waiting options")

					case 4: print("Own number sending")

					case 5: print("Phone line in use")

					case 6: print("Automatic answer")

					case _:
						default: print("Invalid input")

		

	
			case 2:
				Phonesettings = """
				Phone settings 
				1. Language
				2. Cell info display
				3. WElcome note
				4. Network selection
				5. Lights
				6. Confirm SIM service actions
							"""
				print(Phonesettings)
				user_input8 = int(input('Choose:'))
	
				match(user_input8):
					case 1: print("Language")

					case 2: print("Cell info display")

					case 3: print("Welcome note")

					case 4: print("Network selection")

					case 5: print("Lights")

					case 6: print("Confirm SIM service actions")

					case _:
						default: print("Invalid input")

					
									
			case 3:
				Securitysettings = """
				Security settings
				1. PIN code request
				2. Call barring service
				3. Fixed dialling
				4. Closed user group
				5. Phone security
				6. Change access codes
						"""
				print(Securitysettings)
				user_Input9 = int(input('Choose:'))
	
				match(user_Input9):
					case 1: print("PIN code settings")

					case 2: print("Call barring service")

					case 3: print("Fixed dialling")

					case 4: print("Closed user group")

					case 5: print("Phone security")

					case 6: print("Change access codes")

					case _:
						default: print("Invalid input")

			case 4: print("Restore factory settings")

			case _:
				default: print("Invalid Input")




	case 7: print("Call divert")
				

	case 8: print("Games") 
		
	
	case 9: print("Calculator")
		

	case 10: print("Reminders")
		

	case 11: 
		Clock = """
		Clock
		1. Alarm clock
		2. Clock settings
		3. Date setting
		4. Stopwatch
		5. Countdown timer
		6. Auto update of date and time	
					"""

		print(Clock)
		customer_choice7 = int(input('Choice:'))
			
		match(customer_choice7):
			case 1: print("Alarm clock")

			case 2: print("Clock settings")

			case 3: print("Date setting")

			case 4: print("Stopwatch")

			case 5: print("Countdown timer")

			case 6: print("Auto update of date and time")

			case _:
				default: print("Invalid Input")

		
	

	case 12: print("Profiles")


	case 13: print("SIM services")
		
			
	case _: 
		default: print("Switched off!!!")


			

		
				

