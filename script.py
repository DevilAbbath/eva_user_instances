import json
import os
from datetime import datetime
from user import Usuario

def crear_usuarios_desde_archivo(archivo_usuarios, carpeta_log):
    usuarios = []
    errores_detectados = 0

    #validador de que la carpeta log exista, en caso de que no la crea
    os.makedirs(carpeta_log, exist_ok=True)
    archivo_errores = os.path.join(carpeta_log, 'error.log')
    
    with open(archivo_usuarios, 'r') as file:
        for linea in file:
            try:
                datos_usuario = json.loads(linea.strip())
                usuario = Usuario(**datos_usuario)  # Se crea lainstancia de Usuario
                usuarios.append(usuario)

            except Exception as e:
                # obetner fecha y hora actual
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # contador de errores detectados
                errores_detectados += 1
                
                with open(archivo_errores, 'a') as error_file:
                    error_file.write(f"[{timestamp}] Error al procesar la línea: {linea.strip()}\n")
                    error_file.write(f"[{timestamp}] Excepción: {str(e)}\n\n")
    
    usuarios_creados = len(usuarios)
    print(f"\nSe han creado un total de {usuarios_creados} usuarios")
    print(f"Se han detectado {errores_detectados} usuarios con errod de registro, favor revisar el archivo error.log \n")


    return usuarios

# Uso del script
usuarios = crear_usuarios_desde_archivo('usuarios.txt', 'log')

# Aquí podrías hacer algo con la lista de usuarios, como imprimirlos o procesarlos
for usuario in usuarios:
    print(f"Usuario creado: {usuario.nombre} {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")
