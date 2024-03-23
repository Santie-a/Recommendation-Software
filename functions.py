import csv
from DoublyLinkedList import DoublyLinkedList
from Node import Node

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

def goodbye():
	print("Thank you for using the Gaming Recommendation Software!")

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

def search_possible_attribute(doubly_linked_list: DoublyLinkedList, attribute: str, value:str):
	current_node = doubly_linked_list.head_node
	possible = []
	while current_node is not None:
		if current_node.value[attribute].lower().startswith(value.lower()):
			if current_node.value[attribute] not in possible:
				possible.append(current_node.value[attribute])
		current_node = current_node.get_next_node()

	return possible

def print_list(l: list):
	for element in l:
		print(element, end="\t")

def get_decition(prompt: str, possible_answers: list):
	decition = input(prompt)
	if decition in possible_answers:
		return decition
	return ""

def get_genre(doubly_linked_list: DoublyLinkedList):
	while True:
		user_input = input("Introduce the start of the gender and to show the possible options or type the\ngenre to generate the recommendations (Leave blank to see all the options): ")
		possible = search_possible_attribute(doubly_linked_list, "Genre", user_input)
		if len(possible) == 1:
			print(f"The unique possible genre is: {possible[0]}")
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
			
def get_recommendations(genre: str, doubly_linked_list : DoublyLinkedList, range_recommendations: list = [0, 10]):
	print(range_recommendations)
	current_node = doubly_linked_list.head_node
	possible = DoublyLinkedList()
	counter = 0
	while current_node is not None and counter < range_recommendations[0]:
		current_genre = current_node.value["Genre"]
		if current_genre == genre:
			counter += 1
		current_node = current_node.get_next_node()
	while current_node is not None and counter < range_recommendations[1]:
		current_genre = current_node.value["Genre"]
		if current_genre == genre:
			possible.add_to_tail(current_node)
			counter += 1
		current_node = current_node.get_next_node()

	return possible

def print_recommendation(recommendation: Node):
	print(f"""--------------------------------------------------------
Game Name: {recommendation.value["Name"]}
Rank: {recommendation.value["Rank"]}
Year: {recommendation.value["Year"]}
Platform: {recommendation.value["Platform"]}
Publisher: {recommendation.value["Publisher"]}
Global Sales (In Millions): {recommendation.value["Global_Sales"]}
--------------------------------------------------------""")