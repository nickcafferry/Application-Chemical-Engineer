# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import urllib.request

response = urllib.request.urlopen("https://china.guidechem.com/")
response1 = urllib.request.urlopen("https://china.guidechem.com/")

f = open('a.html',mode='w', encoding='utf-8')

for everyline in range(len(response.read().decode('utf-8'))):
	print(response1.readline().decode('utf-8'), file=f)

f.close()


#from urllib import request, parse
#import json

#url = 'http://fanyi.baidu.com/sug'

#def translate(kw):
#    form = {
#        'kw':kw
#    }
#    form_str = parse.urlencode(form)
    
#    form_bytes = form_str.encode('utf-8')
 
#    response = request.urlopen(url,data = form_bytes)
 
#    res_dict = json.loads(response.read().decode('utf-8'))
 
#    result = res_dict['data'][0]['v']
 
#    return result

# if __name__ == '__main__':
#    res = translate('篮球')
#    print(res)
    
#    res = translate('足球')
#    print(res)

