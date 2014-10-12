import MySQLdb

class _connect2db():
	def __init__ (self):
		db = MySQLdb.connect (host= "85.10.205.173", user= "lamp128",
							passwd= "Rfhnjyrf", db="testbase128", charset= 'utf8' )
		self.cursor = db.cursor()


class tabl_products (_connect2db):
	
	def __init__ (self):
		_connect2db.__init__(self)
		self.rows = {}
		self.all_colums = ["ProductID", "ProductName", "SupplierID", 
				"CategoryID", "QuantityPerUnit", "UnitPrice", "UnitsInStock",
				"UnitsOnOrder", "ReorderLevel", "Discontinued"]
		self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]

	def view_all(self):
		self.cursor.execute ("SELECT * FROM Products")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows

	def view_data(self):
		self.cursor.execute ("SELECT Products.ProductID, \
			Products.ProductName, Products.QuantityPerUnit, \
			Products.UnitPrice, Products.UnitsInStock, \
			Products.UnitsOnOrder FROM Products")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows

	def product_row (self, colum_name, symbol, colum_data):
		if colum_name in self.all_colums:
			if symbol in self.all_symbol:
				sql = "SELECT * FROM Products WHERE Products."
				sql += colum_name + " " + symbol + " " + colum_data
				self.cursor.execute (sql)
				numrows = int(self.cursor.rowcount)
				for x in range(0,numrows):
					self.rows[x] = self.cursor.fetchone()
				return self.rows
			else:
				return ValueError, "Wrong symbol"
		else:
			return ValueError, "Wrong colum name"


class tabl_categories (_connect2db):
	
	def __init__ (self):
		_connect2db.__init__(self)
		self.rows = {}
		self.all_colums = ["CategoryID", "CategoryName", "Description"]
		self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]

	def view_all(self):
		self.cursor.execute ("SELECT * FROM Category")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows

	def product_row (self, colum_name, symbol, colum_data):
		if colum_name in self.all_colums:
			if symbol in self.all_symbol:
				sql = "SELECT * FROM Category WHERE Category."
				sql += colum_name + " " + symbol + " " + colum_data
				self.cursor.execute (sql)
				numrows = int(self.cursor.rowcount)
				for x in range(0,numrows):
					self.rows[x] = self.cursor.fetchone()
				return self.rows
			else:
				return ValueError, "Wrong symbol"
		else:
			return ValueError, "Wrong colum name"
