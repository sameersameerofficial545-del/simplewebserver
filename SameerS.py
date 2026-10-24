from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
        <title>My laptop Specifications</title>
    </head>
        <body>
            <h1 align="center">Name: Sameer S</h1>
            <h1 align="center">Reg no: 26014119</h1>
            <table border="6" cellspacing="12" cellpadding="12" >
                <caption align="center">My laptop Specifications</caption>
                <tr>
                    <td>S.No</td>
                    <td>Device specifications</td>
                    <td>Device Info</td>
                </tr>
                <tr>
                    <td>1.</td>
                    <td>Device Name</td>
                    <td>sameer-pc</td>
                </tr>
                <tr>
                    <td>2.</td>
                    <td>Processor</td>
                    <td>intel(R) Core(TM) 5 210H (2.20 GHz)</td>
                </tr>
                <tr>
                    <td>3.</td>
                    <td>Installed RAM</td>
                    <td>16.0 GB (15.7 GB usable)</td>
                </tr>
                <tr>
                    <td>4.</td>
                    <td>Graphics Card</td>
                    <td>Intel(R) Graphics (128 MB)</td>
                </tr>
                <tr>
                    <td>5.</td>
                    <td>Storage</td>
                    <td>124 GB of 477 GB used</td>
                </tr>
                <tr>
                    <td>6.</td>
                    <td>Device ID</td>
                    <td>0748DB463-070A-488E-93D6-7558AB870C7A</td>
                </tr>
                <tr>
                    <td>7.</td>
                    <td>Product ID</td>
                    <td>00342-42954-11749-AAOEM</td>
                </tr>
                <tr>
                    <td>8.</td>
                    <td>System Type</td>
                    <td>64-bit operating system, x64-based processor</td>
                </tr>
                <tr>
                    <td>9.</td>
                    <td>Pen and Touch Support</td>
                    <td>No pen or touch input is available for this display</td>
                </tr>
            </table>
        </body>        
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()