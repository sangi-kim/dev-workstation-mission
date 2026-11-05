import ssl
from urllib import request as urllib_request

try:
    import requests
except ModuleNotFoundError:  # pragma: no cover - fallback for environments without requests
    requests = None

print("--- Python environment test ---")
try:
    if requests is not None:
        response = requests.get("https://www.google.com", timeout=10, verify=False)
        print(f"Google access status: {response.status_code} (200 means success)")
    else:
        req = urllib_request.Request("https://www.google.com", headers={"User-Agent": "Mozilla/5.0"})
        context = ssl._create_unverified_context()
        with urllib_request.urlopen(req, timeout=10, context=context) as response:
            print(f"Google access status: {response.status} (200 means success)")
    print("The Python environment setup is complete.")
except Exception as e:
    print(f"Error: {e}")