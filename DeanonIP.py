def checkports(ip):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.09)
    try:
        connect = sock.connect((ip, i))
        print("Найден открытый порт:", i)
        sock.close()
    except:
        pass

def coords(ip):
    try:
        for i in ip:
            if i in "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя":
                import socket
                ip = socket.gethostbyname(ip)
                break
        import geocoder
        coord = geocoder.ipinfo(ip)
        print("Координаты IP-адреса:", coord.latlng)
        print("Примерное местоположение IP:", coord.city)
    except:
        pass

def who(ip):
    import whois
    print(whois.whois(ip))

def who2(ip):
    try:
        for i in ip:
            if i in "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя":
                import socket
                ip = socket.gethostbyname(ip)
                break
    except:
        pass
    import requests
    infoList1 = requests.get("https://ipinfo.io/" + ip + "/json")
    infoList = infoList1.json()
    try:
        print("IP: ", infoList["ip"])
        print("Город: ", infoList["city"])
        print("Регион: ", infoList["region"])
        print("Страна: ", infoList["country"])
        print("Организация: ", infoList["org"])
        print("Координаты: ", infoList["loc"])
        print("Индекс: ", infoList["postal"])
        print("Часовой пояс: ", infoList["timezone"])
        print("Хост: ", infoList["hostname"])
    except:
        pass

print("""DeanonIP 0.9 by Danil Pistoletov
github.com/DanilPistoletov""")
test = 0
while 1:
    ip = input("Напиши мне IP либо домен и я добуду информацию :з\n")
    for i in ip:
        if i in ".":
            test = 1
            break
    if test == 0:
        pass
    elif test == 0:
        print("Неправильный IP/домен, не играйся со мной >:(")
        ip = "127.0.0.1"
    ports = [7, 20, 21, 22, 23, 25, 53, 69, 79, 80, 81, 88, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
    for i in ports:
        checkports(ip)
    coords(ip)
    print("Whois №1:\n")
    who(ip)
    print("Whois №2:\n")
    who2(ip)
    ip = input("Готов ли ты к следующей проверке?\n")