import sys

from .token_utils import get_token_from_authorization_code



if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or len(args) != 2:
        print("-- Authorization code argument is missing -- ")
    if args[0] == "-c" or args[0] == "--c":
        code = args[1]
        access_token, refresh_token = get_token_from_authorization_code(authorization_code=code)
        print("Access Token: ", access_token)
        print("Refresh Token: ", refresh_token)
       
    else:
        print("Argument option is not recognized")
