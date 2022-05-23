from os.path import expanduser


class Logger:
    '''
        Some colors
    '''

    LOG_PATH = f"{expanduser('~')}/.LeetMarker/app/LOG"
    CRITICAL_LOG_PATH = expanduser('~') + '/'
    RESET = "\x1b[39m"
    CYAN = "\x1b[36m"
    LIGHTBLUE = "\x1b[94m"
    RED = "\x1b[31m"
    LIGHTRED = "\x1b[91m"
    YELLOW = "\x1b[33m"
    LIGHTYELLOW = "\x1b[93m"
    GREEN = "\x1b[32m"
    MAGENTA = "\x1b[35m"
    WHITE = "\x1b[37m"
    LIGHTWHITE = "\x1b[97m"

    @staticmethod
    def __log(string: str):
        print(f"[-] {string}", file=Logger.CRITICAL_LOG_PATH)

    @staticmethod
    def log(string: str, mode: chr):
        '''
            :mode: can be:
                - w <- warning
                - i <- info
                - e <- error
                - c <- critical
        '''

        try:
            if mode not in {'w', 'i', 'e', 'c'}:
                print(string, file=Logger.CRITICAL_LOG_PATH)

            if mode == 'w':
                print(f"{Logger.YELLOW}[!] ", end='', file=Logger.LOG_PATH)

            elif mode == 'i':
                print(f"{Logger.LIGHTBLUE}[i] ", end='', file=Logger.LOG_PATH)

            elif mode == 'e':
                print(f"{Logger.LIGHTRED}[-] ", end='', file=Logger.LOG_PATH)

            print(f"{string}{Logger.RESET}", file=Logger.LOG_PATH)
        except PermissionError:
            Logger.__log(
                f"PERMISSION ERROR WHILE LOGGING: {string} ; EXITING WITH STATUS -1")

        if mode == 'c':
            Logger.__log(string)
