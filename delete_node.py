class LinkedListNode(object):
	def __init__(self, value):
		self.value = value
		self.next = None 

def delete_node (node_to_delete):
	next_node = node_to_delete.next 

	if next_node:
		