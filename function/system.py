import socket
from socket import gethostbyname,create_connection

def Meuip(des):
	if des == "local":
		ipl = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			ipl.connect(("8.8.8.8", 80))
			return ipl.getsockname()[0]
		except:
			return '127.0.0.1'

		ipl.close()
	else:
		return "foi mal"

def Internet():
    tentativas = 0
    servidorRemoto = 'www.google.com.br'

    while tentativas < 3:
        if tentativas == 1:
            servidorRemoto = 'www.lds.org'
        elif tentativas == 2:
            servidorRemoto = 'www.msn.com'

        try:
            host = gethostbyname(servidorRemoto)
            s = create_connection((host, 80), 2)
            return True
        except: tentativas += 1

    return False
