from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import BankTransfer
# Display Pixles

class MainApp(MDApp):
	def build(self):

		# Define Screen
		screen = Screen()

		bank = BankTransfer.Bank()
		bank.open_account("Bill", 42919502, "Massachutes", 4000)
		bank.open_account("John", 30503202104, "Cardiff", 4000)

		bank.deposit(42919502, 500,0,False)
		bank.withdraw(30503202104, 1200,0,False)

		print('\n===== before =====\n')
		#bank.show_accounts(show_history=True)

		bank.transfer(42919502, 30503202104, 100)
		bank.transfer(42919502, 30503202104, 300)
		bank.transfer(30503202104, 42919502, 500)

		print('\n===== after =====\n')
		#bank.show_accounts(show_history=True)
		print(bank.get_account(30503202104)['history'])

		# Define Table
		table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.5},
			size_hint =(0.9, 0.6),
			check = True,
			column_data = [
				("Date and Time", dp(40)),
				("AccountFrom", dp(25)),
				("AccountTo", dp(25)),
				("Transaction", dp(25)),
				("Amount", dp(25))
			],
			row_data = bank.get_account(30503202104)['history']


			)
		
		# Bind the table
		table.bind(on_check_press=self.checked)
		table.bind(on_row_press=self.row_checked)

		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		#return Builder.load_file('table.kv')
		# Add table widget to screen
		screen.add_widget(table)
		return screen
	
	# Function for check presses
	def checked(self, instance_table, current_row):
		print(instance_table, current_row)
	# Function for row presses
	def row_checked(self, instance_table, instance_row):
		print(instance_table, instance_row)

	
#bt = BankTransfer.Bank()
#print("*"*30)

MainApp().run()