class output:
	@staticmethod
	def write(optimal_value, optimal_argument):
		file_name = 'output.txt'

		file = open(file_name, 'w')
		file.write('optimal value: ')
		file.write(str(optimal_value))
		file.write('\n')
		file.write('optimal argument: ')
		file.write(str(optimal_argument))
		file.close()