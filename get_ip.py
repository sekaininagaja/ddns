import urllib.request, urllib.error
import settings

def main():
    try:
        response = urllib.request.urlopen(url=settings.IP_GET_URL, timeout=5)
        content = response.read()
        f = open(settings.IP_ADDR_FILE, 'w')
        f.write(content.decode('utf-8'))
        f.close()
    except urllib.error as e:
        print(type(e))

if __name__ == "__main__":
    main()
