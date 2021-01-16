#CARGA LAS CLASES DE TELETHON
#IMPORTS ALL TELETHON CLASSES
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

#IMPORTA LAS CLASES DE GOOGLE CLOUD Y SISTEMA DE ARCHIVOS
#IMPORTS ALL GOOGLE CLOUD AND FILESYSTEM CLASSES
import os
import csv
from google.cloud import storage
from google.appengine.api import app_identity

#CREDENCIALES PARA EL LOGIN
#LOGIN CREDENTIALS
api_id = ID DEL API CREADO
api_hash = 'HASH DEL API CREADO'
phone = '+TU NUMERO DE TELEFONO CON CODIGO DE PAIS, EJ +59896285042'
client = TelegramClient(phone, api_id, api_hash)

#VERIFICA SI ESTA AUTENTICADO EN TELEGRAM. EN CASO CONTRARIO, SOLICITA A TELEGRAM QUE ENVIE UN MENSAJE CON CODIGO
#CHECKS WHETHER THE USER IS CURRENTLY LOGGED INTO TELEGRAM OR NOT. IF NOT, TELEGRAM WILL SEND A CODE TO THE USER
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('No esta autenticado en telegram. Se le ha enviado un codigo a Telegram. Ingrese el codigo aqui: '))


chats = []
last_date = None
chunk_size = 200
grupos=[]

#OBTIENE LA LISTA DE SUPERGRUPOS DEL USUARIO QUE EJECUTA EL SCRIPT Y LOS MUESTRA EN PANTALLA.
#DISPLAYS THE LIST OF SUPERGROUPS THE USER BELONGS TO
resultado = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(resultado.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            grupos.append(chat)
    except:
        continue

print('Elija el grupo del cual quiera obtener los miembros:')
i=0
for g in grupos:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Ingrese el numero: ")
target_group=grupos[int(g_index)]

#OBTIENE LA LISTA DE PARTICIPANTES DEL CHAT SELECCIONADO, Y GUARDA LA LISTA EN ARCHIVO MIEMBROS.CSV
print('Obteniendo miembros...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Guardando en archivo...')
with open("miembros.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['user id', 'user hash','nombre'])
    for user in all_participants:
        if user.first_name:
            nombre= user.first_name
        else:
            nombre= ""
        if user.last_name:
            apellido= user.last_name
        else:
            apellido= ""
        nombreApellido= (nombre + ' ' + apellido).strip()
        writer.writerow([user.id,user.access_hash,nombreApellido])      
print('Miembros obtenidos exitosamente')

client = storage.Client.from_service_account_json(json_credentials_path='backups-xlv-7de34d8b6bdd.json')
bucket = client.get_bucket('backup_xlv')
object_name_in_gcs_bucket = bucket.blob('uruguayxlaverdad/miembros.csv')
object_name_in_gcs_bucket.upload_from_filename('miembros.csv')
