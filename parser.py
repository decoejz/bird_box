#Texto de teste
texto = "Aee @decoejz, o #canarinho ta cantando na sua pia!"

#Separa cada palavra do comentario para ser parseada e procurar as tags
for word in texto.split():
    if(word[0] == '#'):
        print("Coment tagueou o pássaro {}".format(word[1:]))
        #DO SOMETHIING 
    if(word[0] == '@'):
        print("Comment deu shout para o user {}".format(word[1:]))    
        #DO SOMETHIING 