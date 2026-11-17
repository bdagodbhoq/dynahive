"""Fixed network client for Mininet; never executes model-supplied code."""
import json
import sys
import urllib.request


def main():
    payload = json.load(sys.stdin)
    body = None
    headers = {'Content-Type': 'application/json'}
    if 'action' in payload:
        headers['X-Session-ID'] = payload['session']
        body = {'session_id': payload['session'], 'action': payload['action']} if payload['control'] else payload['action']
    request = urllib.request.Request(payload['url'], data=json.dumps(body).encode() if body else None,
                                    headers=headers)
    # Explicitly ignore host proxy settings; traffic stays inside the lab.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(request, timeout=15) as response:
        print(response.read().decode())


if __name__ == '__main__': main()
