from functions import get_data, welcome, get_gender
from DoublyLinkedList import DoublyLinkedList

if __name__ == '__main__':
	data = get_data("vgsales.csv")
	data_DLL = DoublyLinkedList()
	for row in data:
		data_DLL.add_to_tail(row)
	welcome()
	gender = get_gender(data_DLL)
	if gender is not None:
		pass