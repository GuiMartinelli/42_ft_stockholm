import argparse

def program_args():
	parser = argparse.ArgumentParser(description="This program is a Ransomware, be careful!!! This project is for educational purposes only. You should never use this type of program for malicious purposes.")
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v', '--version', action="store_true", help="show the version of the program")
	group.add_argument('-r', '--reverse', type=str, help="reverse the infection, must be followed by the key to decryption")
	group.add_argument('-s', '--silent', action="store_true", help="run the program in silent mode")
	return parser.parse_args()

def print_version():
	print("stockholm 1.0.0")

def reverse(key: str):
	print(key)

def main():
	args = program_args()
	if args.version:
		print_version()
	if args.reverse:
		reverse(args.reverse)

if __name__ == '__main__':
	main()