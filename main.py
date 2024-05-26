from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    # Setup Authorizer
    authorizer = DummyAuthorizer()

    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    ftp_path = "/Users/root1/ftp"
    user_per = "elradfmw"

    authorizer.add_user(user_name, password, ftp_path, perm=user_per)

    authorizer.add_anonymous("/Users/root1/ftp", perm="elr")

    # Setup Handler
    handler = FTPHandler
    handler.authorizer = authorizer

    # Setup and Start Server
    address = ('0.0.0.0', 21)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
