Resumen
Programa desarrollado en python para verificar correos que son o no spam.
 
Funciones: crear_interfaz()
Hace la interfaz gráfica usando Tkinter

Texto:
-Sección Autor
-Sección Mensaje
-Sección Link
-Lista de correos
Botones:
  -Verificar Autor: este llama a comprobarAmigos()
  -Escanear Correos: este llama a  escanear_correos()
  -Aplicar Reglas: este llama a aplicar_codigo()

 comprobarAmigos():
1. Obtiene el autor del campo correspondiente
2. Importa la lista de amigos (importar_excel('amigos'))
3. Verifica si el autor está en la lista
4. Llama a comprobarPalabra() para analizar el mensaje
5. Muestra resultados en ventanas emergentes

 escanear_correos()`
Lee el archivo mail_data.csv(contien todos los correo) 

aplicar_codigo()
1. Obtiene el mensaje seleccionado en el Listbox
2. Verifica el autor contra la lista de amigos
3. Analiza el mensaje con comprobarPalabra()
4. Muestra los resultados

 comprobarPalabra()
(Requiere un parametro string que sea el mensaje que se quiere analizar

1. Divide el mensaje en palabras
2. Importa palabras baneadas usando importar_excel
3. Compara cada palabra del mensaje con la lista prohibida
4. Muestra alertas si encuentra coincidencias
 importar_excel()
(Requiere un parametro string con el nombre de la columna que se quiere llamar)
1. Lee el excel
2. Extrae los datos de la columna especificada
3. Devuelve una lista con los datos que saco de la columna