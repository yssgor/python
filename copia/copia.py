#Até agora vimos como escrever e ler texto de um arquivo. Agora vamos trabalhar com arquivos binários. Nesse exemplo usaremos uma imagem, o logo do Python.

#O código é praticamente idêntico aos exemplos anteriores. A única coisa que muda é o flag. Agora estamos usando rb para leitura binária e wb para escrita binária.


#arquivo copia.py
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()
