import requests
from bs4 import BeautifulSoup
#Realizar solicitud GETdelaurl

URL='https://quotes.toscrape.com/'
response=requests.get(URL)

if response.status_code ==200:
    #Obtengo la respuesta en un forma legible
    html_content=response.text
    #print(html_content)
    soup=BeautifulSoup(html_content,'html.parser')
    #Imprime el objeto con una estructura mas legible
    #print(soup.prettify())
    citas=soup.find_all('div',class_='quote')
    diccionario_citas={}
    for cita in citas:
        texto=cita.find('span',class_='text').get_text()
        autor=cita.find('small',class_='author').get_text()
        diccionario_citas[autor]=texto
    print(diccionario_citas)
else:
    print(f'Ocurrio un error{response.status_code}')