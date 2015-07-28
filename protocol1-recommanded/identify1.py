import sys
import os
import base64
import hmac
import hashlib
import time
import requests  #sudo easy_install requests or sudo pip install requests

access_key = "xxxxxxxx"
access_secret = "xxxxxxxx"

requrl = "http://ap-southeast-1.api.acrcloud.com/v1/identify"
http_method = "POST"
http_uri = "/v1/identify"
data_type = "audio"
signature_version = "1"
timestamp = time.time()

string_to_sign = http_method+"\n"+http_uri+"\n"+access_key+"\n"+data_type+"\n"+signature_version+"\n"+str(timestamp)

sign = base64.b64encode(hmac.new(access_secret, string_to_sign, digestmod=hashlib.sha1).digest())

# suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC, etc
# File size: < 1M , You'de better cut large file to small file, within 15 seconds data size is better
f = open(sys.argv[1], "r")
sample_bytes = os.path.getsize(sys.argv[1])

files = {'sample':f}
data = {'access_key':access_key,
        'sample_bytes':sample_bytes,
        'timestamp':str(timestamp),
        'signature':sign,
        'data_type':data_type,
        "signature_version":signature_version}

r = requests.post(requrl, files=files, data=data)
r.encoding = "utf-8"
print r.text
