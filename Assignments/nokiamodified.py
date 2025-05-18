import string

user_input1 = -1
while user_input1 != 0:


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
	user_input1 = int(input('Enter number of choice: '))

	match(user_input1):
		case 1: 
			customer_choice1 = -1
			while customer_choice1 != 0:

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
				0. Press 0 to go back
					"""

				print(Phonebook)
				customer_choice1 = int(input('Pick your choice: '))

				match(customer_choice1):

					case 1: 
						search = -1
						while search != 0:

							print('Search')
							print('Press 0 to go back')
						
							search = int(input('Choose:'))
					
							match(search):
								
								case 0: break
								case _:	
									default: print('Invalid input')
						

					case 2: 
						service_nos = -1
						while service_nos != 0:

							print('Service Nos')
							print('Press 0 to go back')
	
							service_nos = int(input('Pick your choice: '))
							
							match(service_nos):
								case 0: break
								case _: 
									default: print('Invalid input')



					case 3:
						add_name = -1
						while add_name != 0:
	
							print("Add name")
							print('Press 0 to go back')
		
							add_name = int(input('Choose:'))
						
							match(add_name):
								case 0: break
								case _: 
									default: print('Invalid input')


					case 4: 
						erase = -1
						while erase != 0:
	
							print("Erase")
							print('Press 0 to go back')
		
							erase = int(input('Choose:'))
						
							match(erase):
								case 0: break
								case _: 
									default: print('Invalid input')




					case 5: 
						edit = -1
						while edit != 0:
	
							print("edit")
							print('Press 0 to go back')
		
							edit = int(input('Choose:'))
						
							match(edit):
								case 0: break
								case _: 
									default: print('Invalid input')



					case 6:
						assign_tone = -1
						while assign_tone != 0:
	
							print("Assign Tone")
							print('Press 0 to go back')
		
							assign_tone = int(input('Choose:'))
						
							match(assign_tone):
								case 0: break
								case _: 
									default: print('Invalid input')


	
					case 7: 
						send_bcard = -1
						while send_bcard != 0:
	
							print("Send b card")
							print('Press 0 to go back')
		
							send_bcard = int(input('Choose:'))
						
							match(send_bcard):
								case 0: break
								case _: 
									default: print('Invalid input')


			
					case 8: 
						user_input = -1
						while user_input != 0:

							Options = """
							Options
							1. Type of view
							2. Memory status
							0. Press 0 to go back
									"""

							print(Options)
							user_input2 = int(input('Choose: '))

							match(user_input2):

								case 1: 
									type_of_view = -1
									while type_of_view != 0:
									
										print('Type of view')
										print('Press 0 to go back')
										
										type_of_view = int(input('Choose:'))
										
										match(type_of_view):
											case 0: break
											case _:
												default: print('Invalid input')


								case 2: 
									memory_status = -1
									while memory_status != 0:
									
										print('Memory status')
										print('Press 0 to go back')
										
										memory_status = int(input('Choose:'))
										
										match(memory_status):
											case 0: break
											case _:
												default: print('Invalid input')
								case 0: break
								case _:
									default: print("Invalid Input")



					case 9: 
						speed_dials = -1
						while speed_dials != 0:
	
							print("Speed dials")
							print('Press 0 to go back')
		
							speed_dials = int(input('Choose:'))
						
							match(speed_dials):
								case 0: break
								case _: 
									default: print('Invalid input')

		
					case 10: 
						voice_tags = -1
						while voice_tags != 0:
	
							print("Voice tags")
							print('Press 0 to go back')
		
							voice_tags = int(input('Choose:'))
						
							match(voice_tags):
								case 0: break
								case _: 
									default: print('Invalid input')
	
			
					case 0: break
					case _:
						default: print("Invalid Input")



		case 2: 
			customer_choice2 = -1
			while customer_choice2 != 0:

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
				0. Press 0 to go back
						"""

				print(Messages)
				customer_choice2 = int(input('Pick your choice: '))
			
				match(customer_choice2):

					case 1: 
						write_messages = -1
						while write_messages != 0:

							print('Write messages')
							print('Press 0 to go back')
						
							write_messages = int(input('Choose:'))
					
							match(write_messages):
								
								case 0: break
								case _:	
									default: print('Invalid input')
						

		
					case 2: 
						inbox = -1
						while inbox != 0:

							print('Inbox')
							print('Press 0 to go back')
						
							inbox = int(input('Choose:'))
					
							match(inbox):
								
								case 0: break
								case _:	
									default: print('Invalid input')
						


					case 3: 
						outbox = -1
						while outbox != 0:

							print('Outbox')
							print('Press 0 to go back')
						
							outbox = int(input('Choose:'))
					
							match(outbox):
								
								case 0: break
								case _:	
									default: print('Invalid input')
						

	
					case 4: 
						picture_messages = -1
						while picture_messages != 0:

							print('Picture messages')
							print('Press 0 to go back')
						
							picture_messages = int(input('Choose:'))
					
							match(picture_messages):
								
								case 0: break
								case _:	
									default: print('Invalid input')
						


		
					case 5: 
						templates = -1
						while templates != 0:

							print('Templates')
							print('Press 0 to go back')
						
							templates = int(input('Choose:'))
					
							match(templates):
								
								case 0: break
								case _:	
									default: print('Invalid input')
					


					case 6: 
						smileys = -1
						while smileys != 0:

							print('Smileys')
							print('Press 0 to go back')
						
							smileys = int(input('Choose:'))
					
							match(smileys):
								
								case 0: break
								case _:	
									default: print('Invalid input')



					case 7: 
						user_input3 = -1
						while user_input3 != 0:

							Messagesettings = """
							Message settings
							1. Set 1
							2. Common
							0. Press 0 to go back
								"""

							print(Messagesettings)					
							user_input3 = int(input('Choose:'))
				
							match(user_input3):

								case 1:
									set = -1
									while set != 0:

										Set1 = """
										Set 1
										1. Message center number
										2. Messages sent as
										3. Message validity
										0. Press 0 to go back
											"""

										print(Set1)
										set = int(input('Choose:')) 
		
										match(set):
											case 1: 
												message_center = -1
												while message_center != 0:
														
													print('Message center number')
													print('Press 0 to go back')
				
													message_center = int(input('Choose: '))	
	
													match(message_center):

														case 0: break
														case _:
															default: print('Invalid Input')
													

		
											case 2: 
												message_sent = -1
												while message_sent != 0:
														
													print('Message sent as')
													print('Press 0 to go back')														
													message_sent = int(input('Choose: '))											
													match(message_sent):

														case 0: break
														case _:
															default: print('Invalid Input')
														
	
											case 3: 
												message_validity = -1
												while message_validity != 0:
														
													print('Message validity')
													print('Press 0 to go back')														
													message_validity = int(input('Choose: '))											
													match(message_validity):

														case 0: break
														case _:
															default: print('Invalid Input')
													
											case 0: break
											case _:
												default: print("Invalid Input")	

		
								case 2: 
									common = -1
									while common != 0:

										Common = """
										Common
										1. Delivery reports
										2. Reply via same centre
										3. Character support
										0. Press 0 to go back
												"""
										print(Common)
										common = int(input('Choose:'))
		
										match(common):
											case 1:
												delivery_report = -1
												while delivery_report != 0:
														
													print('Delivery report')
													print('Press 0 to go back')														
													delivery_report = int(input('Choose: '))											
													match(delivery_report):

														case 0: break
														case _:
															default: print('Invalid Input')
													 

			
											case 2: 
												reply_via = -1
												while reply_via != 0:
														
													print('Reply via')
													print('Press 0 to go back')														
													reply_via = int(input('Choose: '))
											
													match(reply_via):

														case 0: break
														case _:
															default: print('Invalid Input')
													

		
											case 3:
												character_support = -1
												while character_support != 0:
														
													print('Character support')
													print('Press 0 to go back')														
													character_support = int(input('Choose: '))
											
													match(character_support):

														case 0: break
														case _:
															default: print('Invalid Input')
													

									

								case 0: break
								case _:
									default: print("Invalid Input")

					case 8: 
						info_services = -1
						while info_services != 0:

							print('Info services')	
							print('Press 0 to go back')
				
							info_services = int(input('Choose:'))
				
							match(info_services):
								case 0: break
								case _: 
									default: print('Invalid Input')



					case 9: 
						voice_mailbox = -1
						while voice_mailbox != 0:

							print('Voice mailbox number')	
							print('Press 0 to go back')	
			
							voice_mailbox = int(input('Choose:'))
				
							match(voice_mailbox):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 10:
						service_command = -1
						while service_command != 0:

							print('Service command editor')	
							print('Press 0 to go back')
				
							service_command = int(input('Choose:'))
				
							match(service_command):
								case 0: break
								case _: 
									default: print('Invalid Input')




			
		case 3:
			chat = -1
			while chat != 0: 

				print('Chat')	
				print()
				print('Press 0 to go back')
				
				chat = int(input('Choose:'))
				
				match(chat):
					case 0: break
					case _: 
						default: print('Invalid Input')


		case 4: 
			call_register = -1
			while call_register != 0:

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
				0. Press 0 to go back
						"""
				print(CallRegister)
				customer_choice3 = int(input('Choose:')) 
	
				match(customer_choice3):
							
					case 1: 
						missed_calls = -1
						while missed_calls != 0:

								print('Missed Calls')	
								print('Press 0 to go back')
				
								missed_calls = int(input('Choose:'))
				
								match(missed_calls):
									case 0: break
									case _: 
										default: print('Invalid Input')

		
					case 2: 
						received_calls = -1
						while received_calls != 0: 

								print('Received Calls')	
								print('Press 0 to go back')
				
								received_calls = int(input('Choose:'))
				
								match(received_calls):
									case 0: break
									case _: 
										default: print('Invalid Input')


					case 3: 
						dialled_numbers = -1
						while dialled_numbers != 0:

								print('Dialled numbers')
								print('Press 0 to go back')
					
								dialled_numbers = int(input('Choose:'))
				
								match(dialled_numbers):
									case 0: break
									case _: 
										default: print('Invalid Input')


					case 4: 
						erase_recent = -1
						while erase_recent != 0: 

								print('Erase recent')	
								print('Press 0 to go back')
				
								erase_recent = int(input('Choose:'))
				
								match(erase_recent):
									case 0: break
									case _: 
										default: print('Invalid Input')


					case 5:
						show_call = -1
						while show_call != 0:

							Showcallduration = """
							Show call duration 
							1. Last call duration
							2. All calls duration
							3. Received calls duration
							4. Dialled calls duration
							5. Clear timers 
							0.Press 0 to go back
									"""
							print(Showcallduration)
							user_input4 = int(input('Choose:'))

							match(user_input4):
								case 1: 
									last_call_duration = -1
									while last_call_duration != 0:

										print('Last call duration')
										print('Press 0 to go back')
			
										last_call_duration = int(input('Choose:'))
					
										match(last_call_duration):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 2: 
									all_call_duration = -1
									while all_call_duration != 0:

										print('All call duration')
										print('Press 0 to go back')
			
										all_call_duration = int(input('Choose:'))
					
										match(all_call_duration):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 3: 
									received_call_duration = -1
									while received_call_duration != 0:

										print('Received call duration')
										print('Press 0 to go back')
			
										received_call_duration = int(input('Choose:'))
					
										match(received_call_duration):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 4: 
									dialled_call_duration = -1
									while dialled_call_duration != 0:

										print('Dialled call duration')
										print('Press 0 to go back')
			
										dialled_call_duration = int(input('Choose:'))
					
										match(dialled_call_duration):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 5:
									clear_timer = -1
									while clear_timer != 0:

										print('Clear timer')
										print('Press 0 to go back')
				
										clear_timer = int(input('Choose:'))
					
										match(clear_timer):
											case 0: break
											case _: 
												default: print('Invalid Input')

								case 0: break
								case _:
									default: print("Invalid input") 

					case 6:
						show_call_cost = -1
						while show_call_cost != 0:

							Showcallcosts = """
							Show call costs 
						 	1. Last call costs
							2. All calls cost
							3. Clear counters
							0. Press 0 to go back
									"""
							print(Showcallcosts)
							user_input5 = int(input('Choose:')) 
	
							match(user_input5):
								case 1:
									last_call_cost = -1
									while last_call_cost != 0:

										print('Last call cost')	
										print('Press 0 to go back')
			
										last_call_cost = int(input('Choose:'))
					
										match(last_call_cost):
											case 0: break
											case _: 
												default: print('Invalid Input')
				
								case 2:
									all_call_cost = -1
									while all_call_cost != 0:

										print('all call cost')
										print('Press 0 to go back')
				
										all_call_cost = int(input('Choose:'))
					
										match(all_call_cost):
											case 0: break
											case _: 
												default: print('Invalid Input')
				


								case 3: 
									clear_counter = -1
									while clear_counter != 0:

										print('Clear counter')
										print('Press 0 to go back')
				
										clear_counter = int(input('Choose:'))
					
										match(clear_counter):
											case 0: break
											case _: 
												default: print('Invalid Input')

								case 0: break
								case _:
									default: print("Invalid input")

					case 7:
						call_cost_setting = -1
						while call_cost_setting != 0:

							Callcostsettings = """
							Call cost settings 
							1. Call cost limit
							2. Show costs in
							0. Press 0 to go back
									"""
							print(Callcostsettings)
							user_input6 = int(input('Choose:'))

							match(user_input6):

								case 1:
									call_cost_limit = -1
									while call_cost_limit != 0:

										print('Call cost limit')
										print('Press 0 to go back')
				
										call_cost_limit = int(input('Choose:'))
					
										match(call_cost_limit):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 2:
									show_cost = -1
									while show_cost != 0:

										print('Show cost in')
										print('Press 0 to go back')
				
										show_cost = int(input('Choose:'))
					
										match(show_cost):
											case 0: break
											case _: 
												default: print('Invalid Input')

								case 0: break
								case _:
									default: print("Invalid input")


					case 8:
						prepaid_credit = -1
						while prepaid_credit != 0:

							print('Prepaid credit')	
							print('Press 0 to go back')
			
							prepaid_credit = int(input('Choose:'))
		
							match(prepaid_credit):
								case 0: break
								case _: 
									default: print('Invalid Input')

					case 0: break
					case _:
						default: print("Invalid input")


		case 5: 
			tones = -1
			while tones != 0:
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
				0. Press 0 to go back
						"""

				print(Tones)
				customer_choice4 = int(input('Choose:'))
			
				match(customer_choice4):

					case 1: 
						ringing_tone = -1
						while ringing_tone != 0: 

							print('Ringing tone')	
							print('Press 0 to go back')
				
							ringing_tone = int(input('Choose:'))
				
							match(ringing_tone):
								case 0: break
								case _: 
									default: print('Invalid Input')



					case 2: 
						ringing_volume = -1
						while ringing_volume != 0: 

							print('Ringing volume')	
							print('Press 0 to go back')
					
							ringing_volume = int(input('Choose:'))
				
							match(ringing_volume):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 3:
						incoming_call = -1
						while incoming_call != 0: 

							print('Incoming call')	
							print('Press 0 to go back')
						
							incoming_call = int(input('Choose:'))
				
							match(incoming_call):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 4:
						composer = -1
						while composer != 0: 

							print('Composer')	
							print('Press 0 to go back')
				
							composer = int(input('Choose:'))
				
							match(composer):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 5:
						message_alert = -1
						while message_alert != 0: 
	
							print('Message alert')	
							print('Press 0 to go back')
				
							message_alert = int(input('Choose:'))
				
							match(message_alert):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 6: 
						keypad_tone = -1
						while keypad_tone != 0: 

							print('Keypad tone')	
							print('Press 0 to go back')
				
							keypad_tone = int(input('Choose:'))
				
							match(keypad_tone):
								case 0: break
								case _: 
									default: print('Invalid Input')

	
					case 7: 
						warning_games = -1
						while warning_games != 0: 

							print('Warning and games tones')	
							print('Press 0 to go back')
				
							warning_games = int(input('Choose:'))
				
							match(warning_games):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 8: 
						vibrating_alert = -1
						while vibrating_alert != 0: 

							print('Vibrating alert')	
							print('Press 0 to go back')
				
							vibrating_alert = int(input('Choose:'))
				
							match(vibrating_alert):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 9: 
						screen_saver = -1
						while screen_saver != 0: 

							print('Screen saver')	
							print('Press 0 to go back')
				
							screen_saver = int(input('Choose:'))
				
							match(screen_saver):
								case 0: break
								case _: 
									default: print('Invalid Input')

					case 0: break
					case _: 
						default: print("Invalid Input")


		case 6: 
			settings = -1
			while settings != 0:

				Settings = """
				Settings	
				1. Call settings
				2. Phone settings
				3. Security settings
				4. Restore factory settings
				0. Press 0 to go back
						"""

				print(Settings)
				customer_choice5 = int(input('Choose:'))
			
				match(customer_choice5): 
					case 1:
						call_settings = -1
						while call_settings != 0:

							Callsettings = """
							Call settings 
							1. Automatic redial
							2. Speed dialling
							3. Call waiting options
							4. Own number sending
							5. Phone line in use
							6. Automatic answer
							0. Press 0 to go back
									"""
							print(Callsettings)
							user_input7 = int(input('Choose:'))
			
							match(user_input7): 
								case 1: 
									automatic_redial = -1
									while automatic_redial != 0:

										print('Automatic redail')
										print('Press 0 to go back')
				
										automatic_redial = int(input('Choose:'))
					
										match(automatic_redial):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 2: 
									speed_dialling = -1
									while speed_dialling != 0:

										print('Speed dialling')
										print('Press 0 to go back')
				
										speed_dialling = int(input('Choose:'))
					
										match(speed_dialling):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 3: 
									call_waiting = -1
									while call_waiting != 0:

										print('Call waiting options')
										print('Press 0 to go back')
				
										call_waiting = int(input('Choose:'))
					
										match(call_waiting):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 4:
									own_number = -1
									while own_number != 0:

										print('Own number sending')
										print('Press 0 to go back')
				
										own_number = int(input('Choose:'))
					
										match(own_number):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 5:
									phone_line = -1
									while phone_line != 0:

										print('Phone line in use')
										print('Press 0 to go back')
				
										phone_line = int(input('Choose:'))
					
										match(phone_line):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 6:
									automatic_answer = -1
									while automatic_answer != 0:

										print('Automatic answer')
										print('Press 0 to go back')
				
										automatic_answer = int(input('Choose:'))
					
										match(automatic_answer):
											case 0: break
											case _: 
												default: print('Invalid Input')

								case 0: break
								case _:
									default: print("Invalid input")

			
					
					case 2:
						phone_settings = -1
						while phone_settings != 0:

							Phonesettings = """
							Phone settings 
							1. Language
							2. Cell info display
							3. Welcome note
							4. Network selection
							5. Lights
							6. Confirm SIM service actions
							0. Press 0 to go back
									"""
							print(Phonesettings)
							user_input8 = int(input('Choose:'))
	
							match(user_input8):
								case 1:	
									language = -1
									while language != 0:

										print('Language')
										print()
										print('Press 0 to go back')
				
										language = int(input('Choose:'))
			
										match(language):
											case 0: break
											case _: 
												default: print('Invalid Input')

								case 2:
									cell_info = -1
									while cell_info != 0:

										print('Cell info display')
										print('Press 0 to go back')
				
										cell_info = int(input('Choose:'))
			
										match(cell_info):
											case 0: break
											case _: 
												default: print('Invalid Input')

					
								case 3:
									welcome_note = -1
									while welcome_note != 0:

										print('Welcome note')
										print('Press 0 to go back')
			
										welcome_note = int(input('Choose:'))
					
										match(welcome_note):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 4: 
									network_selection = -1
									while network_selection != 0:

										print('Network_selection')
										print('Press 0 to go back')
		
										network_selection = int(input('Choose:'))
			
										match(network_selection):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 5:
									lights = -1
									while lights != 0:

										print('Lights')
										print('Press 0 to go back')
				
										lights = int(input('Choose:'))
					
										match(lights):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 6:
									confirm_SIM = -1
									while confirm_SIM != 0:

										print('Confirm SIM service actions')
										print()			
										print('Press 0 to go back')
				
										confirm_SIM = int(input('Choose:'))
					
										match(confirm_SIM):
											case 0: break
											case _: 
												default: print('Invalid Input')
									
								case 0: break
								case _:
									default: print("Invalid input")

		


												
					case 3:
						security_settings = -1
						while security_settings != 0:
	
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
								case 1:
									pin_code = -1
									while pin_code != 0:

										print('PIN code request')
										print()
										print('Press 0 to go back')
				
										pin_code = int(input('Choose:'))
			
										match(pin_code):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 2: 
									call_barring = -1
									while call_barring != 0:

										print('Call barring service')
										print()
										print('Press 0 to go back')
				
										call_barring = int(input('Choose:'))
			
										match(call_barring):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 3:
									fixed_dialling = -1
									while fixed_dialling != 0:

										print('Fixed dialling')
										print()
										print('Press 0 to go back')
				
										fixed_dialling = int(input('Choose:'))
			
										match(fixed_dialling):
											case 0: break
											case _: 
												default: print('Invalid Input')

				
								case 4:
									closed_user = -1
									while closed_user != 0:

										print('Closed user group')
										print()
										print('Press 0 to go back')
				
										closed_user = int(input('Choose:'))
			
										match(closed_user):
											case 0: break
											case _: 
												default: print('Invalid Input')


								case 5:
									phone_security = -1
									while phone_security != 0:

										print('Phone security')
										print()
										print('Press 0 to go back')
				
										phone_security = int(input('Choose:'))
			
										match(phone_security):
											case 0: break
											case _: 
												default: print('Invalid Input')

			
								case 6:
									change_access = -1
									while change_access != 0:

										print('Change access codes')
										print()
										print('Press 0 to go back')
				
										change_access = int(input('Choose:'))
			
										match(change_access):
											case 0: break
											case _: 
												default: print('Invalid Input')

								case 0: break
								case _:
									default: print("Invalid input")

					case 4: 
						restore_factory = -1
						while restore_factory != 0:

							print('Restore factory settings')
							print()
							print('Press 0 to go back')
			
							restore_factory = int(input('Choose:'))
			
							match(restore_factory):
								case 0: break
								case _: 
									default: print('Invalid Input')

					case 0: break
					case _:
						default: print("Invalid Input")


		case 7:
			call_divert = -1
			while call_divert != 0: 

				print('Call divert')	
				print()
				print('Press 0 to go back')
				
				call_divert = int(input('Choose:'))
				
				match(call_divert):
					case 0: break
					case _: 
						default: print('Invalid Input')

				

		case 8: 
			games = -1
			while games != 0: 

				print('Games')	
				print()
				print('Press 0 to go back')
				
				games = int(input('Choose:'))
				
				match(games):
					case 0: break
					case _: 
						default: print('Invalid Input')

		
	
		case 9:
			calculator = -1
			while calculator != 0: 

				print('Calculator')	
				print()
				print('Press 0 to go back')
				
				calculator = int(input('Choose:'))
				
				match(calculator):
					case 0: break
					case _: 
						default: print('Invalid Input')

		

		case 10:
			remainder = -1
			while remainder != 0: 

				print('Remainder')	
				print()
				print('Press 0 to go back')
				
				remainder = int(input('Choose:'))
				
				match(remainder):
					case 0: break
					case _: 
						default: print('Invalid Input')


		case 11: 
			clock = -1
			while clock != 0:

				Clock = """
				Clock
				1. Alarm clock
				2. Clock settings
				3. Date setting
				4. Stopwatch
				5. Countdown timer
				6. Auto update of date and time	
				0. Press 0 to go back
						"""

				print(Clock)
				customer_choice7 = int(input('Choice:'))
			
				match(customer_choice7):

					case 1: 
						alarm_clock = -1
						while alarm_clock != 0:

							print('Alarm clock')
							print()
							print('Press 0 to go back')
			
							alarm_clock = int(input('Choose:'))
			
							match(alarm_clock):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 2: 
						clock_settings = -1
						while clock_settings != 0:

							print('Clock settings')
							print()
							print('Press 0 to go back')
			
							clock_settings = int(input('Choose:'))
			
							match(clock_settings):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 3:
						date_settings = -1
						while date_settings != 0:

							print('Date settings')
							print()
							print('Press 0 to go back')
			
							date_settings = int(input('Choose:'))
			
							match(date_settings):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 4:
						stopwatch = -1
						while stopwatch != 0:

							print('Stopwatch')
							print()
							print('Press 0 to go back')
			
							stopwatch = int(input('Choose:'))
			
							match(stopwatch):
								case 0: break
								case _: 
									default: print('Invalid Input')


					case 5:
						countdown_timer = -1
						while countdown_timer != 0:

							print('Countdown timer')
							print()
							print('Press 0 to go back')
			
							countdown_timer = int(input('Choose:'))
			
							match(countdown_timer):
								case 0: break
								case _: 
									default: print('Invalid Input')

		
					case 6:
						auto_update = -1
						while auto_update != 0:

							print('Auto update of date and time')
							print()
							print('Press 0 to go back')
			
							auto_update = int(input('Choose:'))
		
							match(auto_update):
								case 0: break
								case _: 
									default: print('Invalid Input')

					case 0: break
					case _:
						default: print("Invalid Input")



		case 12: 
			profiles = -1
			while profiles != 0: 

				print('Profiles')	
				print()
				print('Press 0 to go back')
				
				profiles = int(input('Choose:'))
				
				match(profiles):
					case 0: break
					case _: 
						default: print('Invalid Input')



		case 13:
			sim_services = -1
			while sim_services != 0: 

				print('SIM services')	
				print()
				print('Press 0 to go back')
				
				sim_services = int(input('Choose:'))
				
				match(sim_services):
					case 0: break
					case _: 
						default: print('Invalid Input')

		case _:
			default: print("Invalid input, Try Again!.");
	
