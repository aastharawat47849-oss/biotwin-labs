import urllib.request
import json

# 1. Test CRM Gate
content = urllib.request.urlopen('http://127.0.0.1:5050/founder-crm').read().decode('utf-8')
print('CRM Gate Active:', 'Founder Security Access' in content)
print('PIN Input Present:', 'pin' in content)

# 2. Test Anti-Fraud UTR Verification with fake UTR
req_bad = urllib.request.Request(
    'http://127.0.0.1:5050/api/verify-payment',
    data=json.dumps({'utr': '12345', 'name': 'Scammer'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)
try:
    urllib.request.urlopen(req_bad)
    print('Failed: Bad UTR was accepted!')
except urllib.error.HTTPError as e:
    print('Good: Bad UTR rejected with code:', e.code)

# 3. Test Valid 12-digit UTR
req_good = urllib.request.Request(
    'http://127.0.0.1:5050/api/verify-payment',
    data=json.dumps({'utr': '429182749102', 'name': 'Honest Client', 'amount': 199, 'phone': '9876543210'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)
res = urllib.request.urlopen(req_good)
print('Valid UTR Accepted:', json.loads(res.read().decode('utf-8')))

# 4. Test Duplicate Replay Prevention with the same UTR
req_dup = urllib.request.Request(
    'http://127.0.0.1:5050/api/verify-payment',
    data=json.dumps({'utr': '429182749102', 'name': 'Replay Hacker'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)
try:
    urllib.request.urlopen(req_dup)
    print('Failed: Duplicate UTR was accepted!')
except urllib.error.HTTPError as e:
    print('Good: Duplicate UTR blocked with code:', e.code)
