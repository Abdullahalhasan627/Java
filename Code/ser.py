# import subprocess
# import os

# # تحقق من تشغيل البرنامج كمسؤول
# if os.name != 'posix':
#     print("يجب تشغيل هذا البرنامج كمسؤول (Administrator).")
#     exit()

# try:
#     # تثبيت خدمة OpenSSH على نظام Windows
#     subprocess.run(["powershell", "-Command", "Add-WindowsFeature -Name OpenSSH-Server"])

#     # تشغيل خدمة OpenSSH
#     subprocess.run(["powershell", "-Command", "Start-Service sshd"])

#     # ضبط خدمة OpenSSH للتشغيل التلقائي عند بدء تشغيل النظام
#     # subprocess.run(["powershell", "-Command", "Set-Service -Name sshd -StartupType 'Automatic'"])

#     print("تم تثبيت وتشغيل خدمة OpenSSH بنجاح.")

# except Exception as e:
#     print("حدث خطأ أثناء تثبيت أو تشغيل خدمة OpenSSH:")
#     print(str(e))

# import os
# import hashlib
# from tkinter import *
# from tkinter import filedialog

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def find_hash_file():

#     clear_console()
#     try:

#         type_hash_use = input("Enter th type hash: ")

#         def type_hash():
#             if type_hash_use == 'md5':
#                 return hashlib.md5(pass_line.encode('utf-8')).hexdigest()
#             elif type_hash_use == 'sha1':
#                 return hashlib.sha1(pass_line.encode('utf-8')).hexdigest()
#             elif type_hash_use == 'sha224':
#                 return hashlib.sha224(pass_line.encode('utf-8')).hexdigest()
#             elif type_hash_use == 'sha128':
#                 return hashlib.sha256(pass_line.encode('utf-8')).hexdigest()
#             elif type_hash_use == 'sha384':
#                 return hashlib.sha384(pass_line.encode('utf-8')).hexdigest()
#             elif type_hash_use == 'sha512':
#                 return hashlib.sha512(pass_line.encode('utf-8')).hexdigest()
#             elif type_hash_use == 'blake2b':
#                 return hashlib.blake2b(pass_line.encode('utf-8')).hexdigest()
#             elif type_hash_use == 'blake2s':
#                 return hashlib.blake2s(pass_line.encode('utf-8')).hexdigest()

#         file_hash_path = filedialog.askopenfilename(title="Select File Hash")
#         if not file_hash_path:
#             print("You are not selecting a hash file")
#             return

#         file_pass_path = filedialog.askopenfilename(title="Select File Passwords")
#         if not file_pass_path:
#             print("You are not selecting a passwords file")
#             return

#         print("-----------------------------------------------------------------------------")
#         print("| ///  An attempt is now made to guess the hash from the password file  \\\\\\ |")
#         print("-----------------------------------------------------------------------------")

#         with open(file_hash_path, 'r') as hash:
#             hash_target = hash.read().strip()

#         with open(file_pass_path, 'r') as password:

#             for line in password:
#                 pass_line = line.strip()
#                 hash_line = type_hash()

#                 if hash_line == hash_target:
#                     print(f"Found hash target: {pass_line}")
#                     break

#             else:
#                 print("No found hash target!")

#     except FileNotFoundError:
#         print("File not found")
#     except Exception as err:
#         print(f"Exception: {err}")

# if __name__ == "__main__":
#     root = Tk()
#     root.withdraw()
#     find_hash_file()


import hashlib





