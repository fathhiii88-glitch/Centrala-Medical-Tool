class FTPManager:
    def __init__(self, host, username, password):
        print("Connecting to FTP server...")
        print("Connected successfully (simulated)")

    def list_files(self):
        print("Retrieving file list...")
        files = ["test.csv"]
        print(f"{len(files)} files found")
        return files

    def download_file(self, filename):
        print(f"Downloading {filename}...")
        print(f"{filename} downloaded")

    def close(self):
        print("FTP connection closed")

if __name__ == "__main__":
    ftp = FTPManager("ftp.example.com", "username", "password")
    
    files = ftp.list_files()
    
    for file in files:
        ftp.download_file(file)
    
    ftp.close()