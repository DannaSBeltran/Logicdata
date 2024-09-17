# Importa las librerías necesarias
import requests, json


# Define una función para obtener la IP y la región a partir de un dominio
def obtenerIpDedeDominio(dominio):
    # Imprime el dominio que se está procesando
    print("---------Dominio -> " + str(dominio) + "-----------")

    # Realiza una solicitud GET a la API de networkcalc para buscar información DNS del dominio
    resultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/" + str(dominio))

    # Verifica si la respuesta JSON contiene registros
    if resultadoBusqueda.json()['records'] != None:
        # Itera sobre cada registro de tipo 'A' (que asocia el dominio con una dirección IP)
        for i in range(len(resultadoBusqueda.json()['records']['A'])):
            # Extrae la dirección IP del registro
            ip = resultadoBusqueda.json()['records']['A'][i]['address']

            # Realiza una solicitud GET a la API de ipinfo.io para obtener la región de la IP
            resultadoRegion = requests.get("https://ipinfo.io/" + str(ip) + "?token=74bc917a25b741")

            # Imprime la región asociada con la IP
            print("la region de la ip -> " + str(ip) + " es " + str(resultadoRegion.json()['region']))


# Define una función para obtener correos electrónicos asociados a un dominio
def optenerEmail(dominio):
    # Realiza una solicitud GET a la API de Hunter para buscar correos electrónicos en el dominio
    resultadosEmail = requests.get("https://api.hunter.io/v2/domain-search?domain=" + str(
        dominio) + "&api_key=344ff07dbe78869fe56eba9c0f1ebc3bf225fb08")

    # Verifica si la respuesta JSON contiene correos electrónicos
    if resultadosEmail.json()["data"]["emails"] != None:
        # Itera sobre cada correo electrónico en la respuesta
        for correo in range(len(resultadosEmail.json()["data"]["emails"])):
            # Imprime cada dirección de correo electrónico
            print("correo: " + str(resultadosEmail.json()["data"]["emails"][correo]["value"]))


# Lista de dominios de empresas famosas en Colombia
dominios_empresas_colombianas = [
    "ecopetrol.com.co",
    "grupoavvillas.com.co",
    "bancolombia.com",
    "santander.com.co",
    "grupoargos.com.co",
    "nexenta.com",
    "grupoexito.com",
    "celsia.com",
    "caracoltv.com",
    "rcn.com.co",
    "postobon.com.co",
    "avianca.com",
    "sodimac.com.co",
    "bancafianc.com",
    "d1.com.co",
    "supranational.com",
    "tigo.com.co",
    "entelchile.net",
    "colpatria.com.co",
    "carreras.com.co",
    "panamericana.com.co",
    "falabella.com.co",
    "centauro.com.co",
    "samsclub.com.co",
    "carulla.com",
    "mintransporte.gov.co",
    "mueblesdico.com",
    "colfondos.com",
    "pepsi.com.co",
    "mercedesbenz.com.co",
    "renault.com.co",
    "chevrolet.com.co",
    "honda.com.co",
]

# Itera sobre cada dominio en la lista
for i in dominios_empresas_colombianas:
    # Llama a la función para obtener la IP y la región del dominio
    obtenerIpDedeDominio(i)
    # Llama a la función para obtener los correos electrónicos del dominio
    optenerEmail(i)
