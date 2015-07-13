import os
from tenon.api import TenonIO

URL = 'http://www.google.com'
DOCUMENT = '<html lang="en"><head><title>Test page</title><head><body><img src="test.jpg"></body></html>'
FRAGMENT = '<img src="test.jpg">'

tenonApi = TenonIO(key=os.environ['TENON_API_KEY'])

print('Tenon.checkUrl:\n %s' % tenonApi.checkUrl(URL).text)
print('Tenon.checkSrc:\n %s' % tenonApi.checkSrc(DOCUMENT).text)
print('Tenon.checkFragment:\n %s' % tenonApi.checkFragment(FRAGMENT).text)
print('Tenon.analyze(URL):\n %s' % tenonApi.analyze(URL).text)
print('Tenon.analyze(DOCUMENT):\n %s' % tenonApi.analyze(DOCUMENT).text)
print('Tenon.analyze(FRAGMENT):\n %s' % tenonApi.analyze(FRAGMENT).text)
