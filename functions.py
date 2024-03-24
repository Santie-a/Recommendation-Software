import csv
from DoublyLinkedList import DoublyLinkedList
from Node import Node

def get_data(filename: str):
	"""
	Get data in form of a list of dictionaries from CSV file.
	"""
	with open(filename, "r") as csvfile:
		csv_reader = csv.DictReader(csvfile)
		data_dict = []
		for row in csv_reader:
			data_dict.append(row)
	return data_dict

def welcome():
	"""
	Function to welcome the user.
	"""
	print("""------------------------------------------------------------------
|                                                                |
|        Welcome to the Video Game Recommendation Software       |
|                                                                |
------------------------------------------------------------------
|          Let us recomend a videogame by the gender:            |
------------------------------------------------------------------""")

def goodbye():
	"""
	Function to say goodbye to the user.
	"""
	print("Thank you for using the Gaming Recommendation Software!")

def search_possible_attribute(doubly_linked_list: DoublyLinkedList, attribute: str, value:str):
	"""
	Search for the possible values of a given attribute of the data.
	"""
	current_node = doubly_linked_list.head_node
	possible = []
	while current_node is not None:
		if current_node.value[attribute].lower().startswith(value.lower()):
			if current_node.value[attribute] not in possible:
				possible.append(current_node.value[attribute])
		current_node = current_node.get_next_node()

	return possible

def get_decition(prompt: str, possible_answers: list):
	"""
	Function that gets a prompt to be displayed and returns the value if it is in the given possible answers, otherwise return an empty string.
	"""
	decition = input(prompt)
	if decition in possible_answers:
		return decition
	return ""

def get_genre(doubly_linked_list: DoublyLinkedList):
	"""
	Function that returns the genre of the given data.
	It asks for the first part of the genre, until there is only one math and the user confirms that selection.
	"""
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
				return ""
			
def get_recommendations(genre: str, doubly_linked_list : DoublyLinkedList, range_recommendations: list = [0, 10]):
	"""
	Function that returns the recomendations in the range of range_recommendations based on a given genre.
	"""
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
	"""
	Prints some data of the node.
	"""
	print(f"""--------------------------------------------------------
Game Name: {recommendation.value["Name"]}
Rank: {recommendation.value["Rank"]}
Year: {recommendation.value["Year"]}
Platform: {recommendation.value["Platform"]}
Publisher: {recommendation.value["Publisher"]}
Global Sales (In Millions): {recommendation.value["Global_Sales"]}
--------------------------------------------------------""")