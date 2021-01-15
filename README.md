# Telegram_Backup

Como respaldar miembros de un grupo de telegram

Antes de ejecutar los scripts, se debe instalar PYTHON
Una vez instalado python, correr este comando: python pip install telethon. Telethon es una libreria que permite interactuar con Telegram. Para mas informacion, por favor referirse a https://docs.telethon.dev/en/latest/

Tambien se debe crear una api en telegram. Para ello, ingresar a http://my.telegram.org/apps y seguir los pasos. Debe guardar el App api_id y el App api_hash

Descargar el archivo backup_chat.py
Editar las lineas 8, 9 y 10. El valor api_id debe ser numerico, y el api_hash y telefono son strings

Ejecute el script. Si es la primera vez que lo ejecuta, telegram le enviara un codigo, el cual sera solicitado por el script
Seleccione el grupo del cual desea respaldar los participantes.
Los datos que se guardan son el user id, el user access hash y el nombre. El user id es el identificador numerico del usuario. NO ES EL USERNAME. El hash del usuario es diferente para cada cuenta que lo vea. Si hay 2 o mas personas intentando ver mi hash, todos lo van a ver diferente



