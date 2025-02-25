# FT_STOCKHOLM

## Introduction to File Manipulation and Ransomware through a Harmless Malware Simulation

This project explores file manipulation techniques and the fundamentals of ransomware by creating a **harmless** proof-of-concept malware. The goal is to understand how real-world ransomware operates—encrypting files, demanding ransoms, and implementing persistence—without causing any actual harm.

### Key Learning Objectives:
- Encrypting and decrypting files securely
- Understanding how ransomware spreads and executes
- Implementing basic persistence techniques
- Studying countermeasures and defenses against ransomware attacks

⚠ **Disclaimer:** This project is strictly for educational purposes. **Do not deploy it in unauthorized environments.**<br/><br/>

### What is Ransomware?
Ransomware is a type of malware that **encrypts the victim's data** and demands a **payment** in exchange for the decryption key to recover the files. It is one of the most **common** and **damaging** types of cyberattacks, often targeting individuals, businesses, and even government institutions.
<br/><br/>

### How Does Ransomware Encrypt Your Data?
Modern ransomware uses a **hybrid encryption** approach. It generates a **symmetric key** to encrypt the victim's files, and then stores this key encrypted with a **public asymmetric encryption algorithm**. The attackers retain control of the **private key**, which is used to decrypt the symmetric key and, ultimately, the files.
This hybrid encryption method makes it extremely difficult to recover the key through other means, leaving **negotiation with hackers** as the only alternative for victims.  
In this program, i used this same hybrid encryption approach, utilizing **AES-CBC** for file encryption and **RSA** for encrypting the AES key.
<br/><br/>

### Is it safe to test this project?
Yes, this malware only encrypts files inside the `~/infection/` directory, limiting its potential damage. However, **I strongly recommend** that this project be tested **only within the Docker container** to ensure a controlled environment. Do not modify the directory or security settings, as doing so may expose your system to unintended risks.
<br/><br/>

### Usage
- Clone the repository ```git clone```
- Generate a 1024 RSA Key Par in the [RSA Key Generator](https://cryptotools.net/rsagen). Assing the PUBLIC_KEY global variable in the `stockholm.py` file with your generated Public Key and store your Private Key (If you lose it, your encrypted files can never be recovered.).
- Start up the Container with ```make``` command (make sure you have Make and Docker installed).
- Once the container is running, it will have the malware and the ~/infection/ directory inside. Access the container's terminal: ```docker exec -it <mycontainer> sh```
- You can view the available flags and usage manual by running: ```python3 stockholm.py -h```.
- Run the malware with: ```python3 stockholm.py```.
- This will encrypt all files in the ~/infection/ directory and change their extensions to .ft. The directory will also contain a file with the encrypted AES symmetric key.
- To restore your files, run ```python3 stockholm.py -r <private_key>```. You can store your Private Key in a text file and run ```python3 stockholm.py -r "$(cat <file>)"``` for example.
<br/><br/>


### Resources
[Wana Decrypt0r (Wanacry Ransomware) - Computerphile](https://www.youtube.com/watch?v=88jkB1V6N9w&t=448s&pp=ygUWd2FubmFjcnkgY29tcHV0ZXJwaGlsZQ%3D%3D)<br/>
[How WanaCrypt Encrypts Your Files - Computerphile](https://www.youtube.com/watch?v=pLluFxHrc30&ab_channel=Computerphile)<br/>
[AES Encryption & Decryption In Python: Implementation, Modes & Key Management](https://onboardbase.com/blog/aes-encryption-decryption/)<br/>
[How to Encrypt and Decrypt Files in Python Using AES: A Step-by-Step Guide](https://medium.com/@dheeraj.mickey/how-to-encrypt-and-decrypt-files-in-python-using-aes-a-step-by-step-guide-d0eb6f525e4e)<br/>
[Asymmetric Encryption](https://elc.github.io/python-security/chapters/07_Asymmetric_Encryption.html)<br/>
[Symmetric vs. asymmetric encryption: Practical Python examples](https://snyk.io/pt-BR/blog/symmetric-vs-asymmetric-encryption-python/?_x_tr_hist=true)<br/>
[Asymmetric Cryptography with Python](https://medium.com/@ashiqgiga07/asymmetric-cryptography-with-python-5eed86772731)<br/>
