from socket import *
import argparse

def printBanner(sock,port):

    try:

        if int(port) == 80:

            sock.send('GET HTTP/1.1 \r\n'.encode())

        else:
            sock.send('\r\n'.encode())
        
        data = sock.recv(4096).decode()

        print('\nBanner: %s\n' %(data))
    
    except:
        
        print('[-] Banner Not Available\n')

def conn(ipv4, port):


    s = socket(AF_INET, SOCK_STREAM)

    addr = (ipv4, int(port))

    try:

        s.connect(addr)

        print('Port %s\%s is open on %s\n' %(int(port), getservbyport(int(port)), ipv4))


        printBanner(s, int(port))

    except Exception as e:

        try:

            print('Port %s\%s is closed on %s\n' %(int(port), getservbyport(int(port)), ipv4))

        except:

            print('Port %s is closed on %s\n' %(int(port), ipv4))
            
    finally:

            s.close()

def ipValidation(ipv4, portlist):

    try:

        ip = gethostbyname(ipv4)

    except:

        print('\n[-] Unknown Host\n')

        exit(0)

    try:

        hostname = gethostbyaddr(ipv4)


        print('\nResult for ' + hostname[0] + ' ...\n' + '='*60 + '\n')

    except:

        print('\nResult for ' + ip + ' ...\n' + '='*30 + '\n')
    
    for port in portlist:

        conn(ip, port)



def main():

    parser = argparse.ArgumentParser(description='Coded By Apkaless')

    parser.add_argument('-p', '--port', type=str, default='9999', help='The Ports To Connect With. Separated by comma (,) ')
    
    parser.add_argument('-a', '--address', type=str, default='localhost', help='The IP Address That You Wanna Scan')

    args = parser.parse_args()

    address = args.address

    portlist = args.port.split(',')

    ipValidation(address, portlist)

if __name__ == '__main__':

    main()