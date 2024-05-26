from ftplib import FTP
from print_colors import YELLOW, ENDC, BLUE, RED, PURPLE
import os

# Define FTP server details

ftp_server = 'localhost'
ftp_user = '1'
ftp_password = '12'

# Connect to the FTP server
ftp = FTP(ftp_server)
ftp.login(user=ftp_user, passwd=ftp_password)


def get_files_data() -> None:
    files = ftp.nlst()
    for file in files:
        print(file)
    if len(files) == 0:
        print(f"{PURPLE}[?] No files in that directory...")


def make_dir() -> None:
    directory_name = input(f"{YELLOW}Enter directory name: {ENDC}")
    file_list = ftp.nlst()
    if directory_name in file_list:
        print(f"{RED}[-] This directory currently exist !!!{ENDC}")
    else:
        ftp.mkd(directory_name)


def change_directory() -> None:
    remote_path = input(f"{YELLOW}Enter destination path: {ENDC}")
    try:
        ftp.cwd(remote_path)
        print(f"{BLUE}[+] Working directory moves successfully{ENDC}")
    except Exception as e:
        print(f"{RED}[-] this path does not exist in the FTP server !!!{ENDC}")


def upload_file(file_to_upload) -> None:
    files_and_dirs = os.listdir('.')
    files = [f for f in files_and_dirs if os.path.isfile(f)]
    if file_to_upload not in files:
        print(f"{RED}[-] This file does not exist !!!{ENDC}")
    else:
        with open(file_to_upload, 'rb') as file:
            # Upload the file
            ftp.storbinary(f'STOR {file_to_upload}', file)
            print(f"{BLUE}[+]'{file_to_upload}' file uploaded successfully ")


def delete_file() -> None:
    file_to_delete = input(f"{YELLOW}Enter file name to delete in the server: {ENDC}")
    files_list = ftp.nlst()
    if file_to_delete not in files_list:
        print(f"{RED}[-] This file does not exist in FTP server !!!{ENDC}")
    else:
        ftp.delete(file_to_delete)
        print(f"{BLUE}[+] File deleted successfully")


def download_file(remote_file: str) -> None:
    files_list = ftp.nlst()
    if remote_file not in files_list:
        print(f"{RED}[-] file does not exist !!!{ENDC}")
    else:
        with open(f"files_from_ftp/{remote_file}", 'wb') as file:
            # Download the file
            ftp.retrbinary(f'RETR {remote_file}', file.write)
        print(f"{BLUE}[+] Downloaded successfully{ENDC}")


def virus_scanner() -> None:
    pass


# Your command with color formatting
while True:
    option = int(
        input(
            f"{YELLOW}Query list: \n1 --> list ftp file\n2 --> download file\n3 --> upload file\n4 --> Delete a file\n5 --> Create a directory\n6 --> Change working directory\n7 --> Scan virus at the FTP server\n8 --> Exit{ENDC}\n"))

    while option > 8 or option < 1:
        option = int(input("Invalid input...\nEnter value between 1-8: "))

    if option == 1:
        get_files_data()
    elif option == 2:
        remote_file_name = input(f"{YELLOW}Enter the remote file name: {ENDC}")
        download_file(remote_file_name)
    elif option == 3:
        file_name = input(f"{YELLOW}Enter file name to upload: {ENDC}")
        upload_file(file_name)
        pass
    elif option == 4:
        delete_file()
    elif option == 5:
        make_dir()
    elif option == 6:
        change_directory()
    elif option == 7:
        virus_scanner()
        pass
    else:
        break

ftp.quit()
