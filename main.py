#!/usr/bin/env python3
from socket import gethostname

def main():
    hostname = gethostname()
    home.run(f'start Home from {hostname}', 'h.mqtt', '192.168.2.30')

# This is not a module, so run the main routine when executed
if __name__ == '__main__':
    main()
