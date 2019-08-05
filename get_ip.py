# -*- coding: utf-8 -*-

import urllib.request, urllib.error
import settings

def main():
    try:
        response = urllib.request.urlopen(url=settings.IP_GET_URL, timeout=5)
        content = response.read().decode('utf-8')
        with open(settings.IP_ADDR_FILE, mode='w+t', encoding='utf-8') as f:
            ip = f.readline()
            if ip != content:
                f.write(content)
    except urllib.error as e:
        print(type(e))

if __name__ == "__main__":
    main()
