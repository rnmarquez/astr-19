import math

def main():
	with open('sin_table.txt', 'w') as f:
		f.write("x\tsin(x)\n")
		for i in range(1000):
			x = 2 * math.pi * i / 1000
			sin_x = math.sin(x)
			f.write(f"{x}\t{sin_x}\n")
			

if __name__ == '__main__':
    main()