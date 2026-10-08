import json
import urllib.request
import subprocess

print("--- 1. IP DIAGNOSTICS ---")
ip_apis = [
    "https://ipinfo.io/json",
    "http://ip-api.com/json",
    "https://freeipapi.com/api/json",
    "https://ipwho.is/"
]
for api in ip_apis:
    try:
        req = urllib.request.Request(api, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode('utf-8'))
            print(f"API: {api}")
            print(f"  IP: {data.get('ip') or data.get('query')}")
            print(f"  City: {data.get('city')}")
            print(f"  Region: {data.get('region') or data.get('regionName')}")
            print(f"  Country: {data.get('country') or data.get('countryCode')}")
            print(f"  Coords: {data.get('loc') or (str(data.get('lat')) + ',' + str(data.get('lon')))}")
            print(f"  Org/ISP: {data.get('org') or data.get('isp')}")
    except Exception as e:
        print(f"API: {api} -> Error: {e}")

print("\n--- 2. WIFI & BSSID ---")
try:
    cmd = "netsh wlan show networks mode=bssid"
    out = subprocess.check_output(cmd, shell=True, text=True, errors='ignore')
    for line in out.splitlines():
        if any(k in line for k in ['SSID', 'BSSID', 'Signal', 'Authentication']):
            print(line.strip())
except Exception as e:
    print("Wifi error:", e)

print("\n--- 3. TRACEROUTE (First 3 hops) ---")
try:
    cmd = "tracert -d -h 4 8.8.8.8"
    out = subprocess.check_output(cmd, shell=True, text=True, errors='ignore')
    for line in out.splitlines():
        if line.strip():
            print(line.strip())
except Exception as e:
    print("Tracert error:", e)
