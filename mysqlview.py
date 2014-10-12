import bufer

def show_tab (di):
	for i in di:
		print di[i]

""" test bufer block """

A = bufer.tabl_products()
show_tab ( A.view_all() )



