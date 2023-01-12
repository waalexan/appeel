eel.expose(pythonSay)
eel.expose(ip)
eel.expose(internet)

function pythonSay(info) {
	console.log(info)
}

function ip(meuip) {
	console.log(meuip)
}

function internet(internet) {
	console.log(internet)
}

eel.javascriptSay("Cliente javascript escutando")
                    
$("#send").click(function(){
    eel.javascriptSay("Teste feito com sucesso")
})