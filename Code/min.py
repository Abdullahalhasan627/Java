import os
import time
import hashlib
from tkinter import *
from tkinter import filedialog

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_hash_file():
    clear_console()
    
    try:
        def type_hash():
            if type_hash_use == 'md5':
                return hashlib.md5(pass_line.encode()).hexdigest()
            elif type_hash_use == 'sha1':
                return hashlib.sha1(pass_line.encode()).hexdigest()
            elif type_hash_use == 'shake_128':
                return hashlib.shake_128(pass_line.encode()).hexdigest()
            elif type_hash_use == 'sha224':
                return hashlib.sha224(pass_line.encode()).hexdigest()
            elif type_hash_use == 'sha256':
                return hashlib.sha256(pass_line.encode()).hexdigest()
            elif type_hash_use == 'sha384':
                return hashlib.sha384(pass_line.encode()).hexdigest()
            elif type_hash_use == 'sha512':
                return hashlib.sha512(pass_line.encode()).hexdigest()
            elif type_hash_use == 'blake2b':
                return hashlib.blake2b(pass_line.encode()).hexdigest()
            elif type_hash_use == 'blake2s':
                return hashlib.blake2s(pass_line.encode()).hexdigest()
            elif type_hash_use == 'sha3_224':
                return hashlib.type_hash_use(pass_line.encode()).hexdigest()
            
        type_of_hash = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", ]
        type_hash_use = input("Enter the type hash: ")
        print("\n")
        
        if type_hash_use in type_of_hash:
            print(f"Use this cryptographic hash: {type_hash_use}\n")
            time.sleep(1.5)
            pass
        else:
            print(f"Hash type is not supported!: {type_hash_use}")
            time.sleep(2)
            return

        print("Locate the hash file\n")
        time.sleep(2.5)
        file_hash_path = filedialog.askopenfilename(title="Select File Hash")
        if not file_hash_path:
            print("\n|  You are not selecting a hash file  |\n")
            return

        time.sleep(2.5)
        print("Locate the password file")
        file_pass_path = filedialog.askopenfilename(title="Select File Passwords")
        if not file_pass_path:
            print("\n|  You are not selecting a passwords file  |\n")
            return

        print("-----------------------------------------------------------------------------")
        print("| ///  An attempt is now made to guess the hash from the password file  \\\\\\ |")
        print("-----------------------------------------------------------------------------\n")

        with open(file_hash_path, 'r') as hash:
            hash_target = hash.read().strip()

        with open(file_pass_path, 'r') as password:
            for line in password:
                pass_line = line.strip()
                hash_line = type_hash()

                if hash_line == hash_target:
                    print(f"Found hash target: {pass_line}\n")
                    break
            else:
                print("No found hash target!")

    except FileNotFoundError:
        print("File not found")
    except Exception as err:
        print(f"Exception: {err}")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    find_hash_file()