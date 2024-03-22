import csv

def get_data(filename: str):
	with open(filename, "r") as csvfile:
		csv_reader = csv.DictReader(csvfile)
		data_dict = []
		for row in csv_reader:
			data_dict.append(row)
	return data_dict

def welcome():
	print("""------------------------------------------------------------------
|                                                                |
|        Welcome to the Video Game Recommendation Software       |
|                                                                |
------------------------------------------------------------------
|          Let us recomend a videogame by the gender:            |
------------------------------------------------------------------""")
	
def print_classifications(classifications: list):
	for i in range(len(classifications)):
		print(f"| {i+1}. {classifications[i]}", end="\t|")
		if (i + 1) % 3 == 0:
			print()
	print()
	print("---------------------------------------------------------\t")

def get_classifications(sample: dict):
	classifications = []
	for element in sample:
		classifications.append(element)
	return classifications

def search_possible_genders(doubly_linked_list, value:str):
	head = doubly_linked_list.head_node
	possible = []
	while head is not None:
		if head.value["Genre"].lower().startswith(value.lower()):
			if head.value["Genre"] not in possible:
				possible.append(head.value["Genre"])
		head = head.get_next_node()

	return possible

def print_list(l: list):
	for element in l:
		print(element, end="\t")

def get_decition(prompt: str, possible_answers: list):
	decition = input(prompt)
	if decition in possible_answers:
		return decition
	return None

def get_gender(doubly_linked_list):
	while True:
		user_input = input("Introduce the start of the gender and to show the possible options or type the gender to generate the recommendations: ")
		possible = search_possible_genders(doubly_linked_list, user_input)
		if len(possible) == 1:
			print(f"The unique possible gender is: {possible[0]}")
			decition = get_decition("Type 'y' for conserving it or 'n' to search for others: ", ['y', 'n'])
			if decition == 'y':
				return possible[0]
		elif len(possible) > 1:
			print("The possible genders are:")
			for element in possible:
				print(f"- {element}")
		else:
			print(f"No gender starts with {user_input}")
			decition = get_decition("Type 'c' for introducing another prompt or 'e' to exit the program: ", ['c', 'e'])
			if decition == 'e':
				return None