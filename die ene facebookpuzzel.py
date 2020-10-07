ops = ["+", "-", "*", "/"]

def func():
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
