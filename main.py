import st7789
import tft_config
import NotoSerif_32 as noto_serif

def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><script>
  function sendRequest() {
        var xhr = new XMLHttpRequest();
        var text = document.getElementById('text_input').value
        xhr.open('POST', '/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(text);
    }</script></head><body>
  <h1>ESP Web Server</h1>
  <input type="text" id="text_input">
  <button onclick="sendRequest()">send</button><span class="slider">
  </span></label></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8080))
s.listen(5)
tft = tft_config.config(rotation=1,buffer_size=16*32*2)
    # init display
tft.init()
tft.fill(st7789.BLACK)
    # center the name of the first font, using the font
row = 16
    # center the name of the second font, using the font
def center(font, s, row, color=st7789.WHITE):
    screen = tft.width()                     # get screen width
    width = tft.write_len(font, s)           # get the width of the string
    if width and width < screen:             # if the string < display
        col = tft.width() // 2 - width // 2  # find the column to center
    else:                                    # otherwise
        col = 0                              # left justify
    tft.write(font, s, col, row, color)      # and write the string

tft.png('pic.png',0,0)
while True:
        if gc.mem_free() < 102000:
          gc.collect()
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        if not request:
            continue
        #print(request)
        index = request.find(b"\r\n\r\n")
        if index != -1:
            text = request[index+4:]
            if text == b'Eskilly':
                break
            tft.png('pic.png',0,0)
        center(noto_serif, text.decode(), 48, st7789.RED)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
import webrepl
webrepl.start(password='12345687')