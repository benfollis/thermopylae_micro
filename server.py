import socket

def start(config, therm_control, therm):
    server_config = config['server']
    port = server_config['port']
    my_addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
    name = server_config['thermometer_name']
    server_socket = socket.socket()
    server_socket.bind(my_addr)
    server_socket.listen(5)
    while True:
        client, client_addr = server_socket.accept()
        client_output = client.makefile('rwb', 0)
        asked_for_discovery = False
        # read their get
        while True:
            line = client_output.readline()
            print(line)
            if line.startswith("GET /discovery"):
                asked_for_discovery = True
            if not line or line == b'\r\n':
                break
        # must not have been discover, so just send the temp
        client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
        if asked_for_discovery:
            client.send('["' + name + '"]\r\n')
        else:
            therm_control.scan()
            therm_control.convert_temp()
            temp = therm_control.read_temp(therm)
            client.send('{ "unit": "C", "temperature": ' + str(temp) + '}\r\n')
        client.close()