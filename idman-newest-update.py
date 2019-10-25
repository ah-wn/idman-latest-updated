from requests import Session
import delorean

http = Session()

http.headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Host': 'www.internetdownloadmanager.com',
    'Referer': 'http://www.internetdownloadmanager.com/data/fv/',
    'Accept': '*/*',
    'Accept-Encoding': 'identity'
}

print('INTERNET DOWNLOAD MANAGER')
# http://www.internetdownloadmanager.com/data/fv/idmupdt2.exe?v=635b05
res = http.post('http://www.internetdownloadmanager.com/data/fv/idmupdt2.exe', data={'lng':9}, stream=True)
headers = res.headers
modified = delorean.parse(headers['Last-Modified'])
length = int(headers['Content-Length'])
length /= 1024**2 # FROM BITS TO MB

print('LAST UPDATED:', modified.humanize())
print(f'SIZE: {length:.3f} MB')
# print(headers)