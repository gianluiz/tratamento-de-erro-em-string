# tratamento de erro em string
Esse tratamento de erro básico serve para cadastros em geral:

-> Caso o usuário digite números, o programa retornará uma mensagem de erro, mas o programa não será interrompido.

-> Caso o o usuário digite o nome com sobrenome, que é o mais correto em qualquer cadastro, se utilizar apenas
o isalpha(), o programa dará um erro, pois não entenderá o espaço como letra.
Para isso é preciso utilizar também o método replace(), conforme demonstrado neste código.

-> Com esses tratamentos de erro, o programa não será interrompido e só aceitará seguir adiante caso o usuário digite
apenas letras.



