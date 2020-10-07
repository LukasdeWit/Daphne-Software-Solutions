ops = ["+", "-", "*", "/"]

def func():
	"""
	Een functie om Daphne's breinbrekende facebookpuzzel op te lossen.
	
	Het doel van deze puzzel is om een som op te lossen door operatoren in te vullen in de som.
	
	Pas op als je computer bijzonder aardappel is, omdat er wel 4^4=256 opties getest worden!
	"""
	corr_lines = []
	for op1 in ops:
		for op2 in ops:
			for op3 in ops:
				for op4 in ops:
					sol = "8 " + op1 + " 4 " + op2 + " 6 == 6 " + op3 + " 7 " + op4 + " 4"
					corr = eval(sol)
					if corr:
						corr_lines.append(sol)
	print("answers:")
	for line in corr_lines:
		print(line)

func()
