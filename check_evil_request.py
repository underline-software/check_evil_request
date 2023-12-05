import re
from collections import defaultdict

log_file_path = 'monitoring.log'

/*
* Log with this format
* LogFormat "%h;%l;%u;%t;\"%r\";%>s;%b;\"%{Referer}i\";\"%{User-Agent}i\"" monitoring
*/

def with_url():
    # Patrón para extraer información relevante del log
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?"(.*?)".*?(\d{3})')

    # Diccionario para almacenar las estadísticas
    stats = defaultdict(lambda: defaultdict(int))

    # Leer el archivo de logs
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = log_pattern.search(line)
            if match:
                ip_address = match.group(1)
                url = match.group(2)
                http_status_code = match.group(3)

                # Incrementar el contador para la combinación de IP, URL y código HTTP
                stats[ip_address][(url, http_status_code)] += 1

    # Imprimir las estadísticas
    for ip_address, url_status_counts in stats.items():
            print(f"IP: {ip_address}")
            for (url, http_status_code), count in url_status_counts.items():
                print(f"URL: {url}; Código HTTP: {http_status_code}; Cantidad: {count}")
            print("=" * 50)

def with_url_less():
    # Patrón para extraer información relevante del log
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?"(.*?)".*?(\d{3})')

    # Diccionario para almacenar las estadísticas
    stats = defaultdict(lambda: defaultdict(int))

    # Leer el archivo de logs
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = log_pattern.search(line)
            if match:
                ip_address = match.group(1)
                url = match.group(2)
                http_status_code = match.group(3)

                # Extraer el método HTTP a partir de la URL (ej. GET, POST)
                http_method = re.match(r'(\w+)', url).group(1) if re.match(r'(\w+)', url) else 'UNKNOWN'

                # Incrementar el contador para la combinación de IP, método HTTP y código HTTP
                stats[ip_address][(http_method, http_status_code)] += 1

    # Imprimir las estadísticas
    print("=" * 50)
    print(f"IP;Método HTTP;Código HTTP;Cantidad")
    for ip_address, method_status_counts in stats.items():
        #print(f"IP: {ip_address}")
        for (http_method, http_status_code), count in method_status_counts.items():
            print(f"{ip_address};{http_method};{http_status_code};{count}")
    print("=" * 50)
def with_url_all():
    # Patrón para extraer información relevante del log
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*?"(\w+) (.*?)".*?(\d{3})')

    # Diccionario para almacenar las estadísticas
    stats = defaultdict(lambda: defaultdict(int))

    # Leer el archivo de logs
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = log_pattern.search(line)
            if match:
                ip_address = match.group(1)
                http_method = match.group(2)
                url = match.group(3)
                http_status_code = match.group(4)

                # Incrementar el contador para la combinación de IP, método HTTP, URL y código HTTP
                stats[ip_address][(http_method, url, http_status_code)] += 1

    # Imprimir las estadísticas
    for ip_address, method_url_status_counts in stats.items():
        #print(f"IP: {ip_address}")
        for (http_method, url, http_status_code), count in method_url_status_counts.items():
            print(f"IP:{ip_address} |  Método HTTP: {http_method}  |  URL: {url}  |  Código HTTP: {http_status_code}  |  Cantidad: {count}")
        print("=" * 50)

#with_url("3.8.144.169")
#with_url("104.199.118.216")
with_url_all()
