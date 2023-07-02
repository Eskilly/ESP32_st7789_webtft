import network
import socket
import time

html = """
<!DOCTYPE html>
<html>
<head> <title>WiFi Configuration</title> </head>
<body>
<h1>WiFi Configuration</h1>
<form method="post" action="/">
    <label>SSID:</label>
    <input type="text" name="ssid"><br>
    <label>Password:</label>
    <input type="password" name="password"><br><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>
"""

ap_ssid = "ESP32"
ap_password = "esp32wifisetup"

def start_ap_mode():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ap_ssid,authmode=network.AUTH_WPA_WPA2_PSK, password=ap_password)

    return ap

def wifi_config_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 80))
    s.listen(5)
    print('Web server running on port', 80)

    while True:
        
            conn, addr = s.accept()
            request = conn.recv(1024).decode()
            if request.find('ssid='):
                parameters = request[request.find('ssid='):]
                if "ssid=" in parameters and "password=" in parameters:
                    ssid = parameters.split("&")[0].split("=")[1]
                    password = parameters.split("&")[1].split("=")[1]
                    print("55555"+parameters+"5555")
                    print("Received configuration: SSID=", ssid, ", password=", password)

                    # Connect to new Access Point
                    sta_if = network.WLAN(network.STA_IF)
                    sta_if.active(True)
                    sta_if.connect(ssid, password)
                    time.sleep(2)
                    print('Connected to', ssid)
                    if sta_if.isconnected():
                        break
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n')
            #conn.send(b'Refresh: 3; url=/\n\n')
            conn.sendall(html)
            conn.close()
access_point = start_ap_mode()
wifi_config_server()
access_point.active(False)