import eel	
from function.system import *

eel.init('web')                     

@eel.expose                        
def javascriptSay(resposta):
	print(resposta)

eel.pythonSay("Servidor python conectado")

eel.ip(Meuip("local"))   

if Internet():
	eel.internet("online")
else:
	eel.internet("offline")     

eel.start('app.html', size=(800, 500))
