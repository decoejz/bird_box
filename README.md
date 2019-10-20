# Bird Box

|Membros|
|---------|
|André Ejzenmesser|
|Wesley Gabriel Albano da Silva|

* [Introdução](#introdução)
* [Requisitos](#requisitos)
* [Modelo Entidade Relacionamento](#modelo-entidade-relacionamento)
* [Modelo Relacional](#modelo-relacional)
* [Dicionário de Dados](#dicionário-de-dados)

## Introdução

Projeto 1 da disciplina de Megadados

Esse projeto visa a construção de uma base de dados de uma rede social de pássaros. Nele existem usuários que podem fazer posts com fotos de pássaros e nelas marcar os pássaros que gostam e referenciar outros usuários.

Os dados podem ser melhor visualizados no [Modelo Entidade Relacionamento](#modelo-entidade-relacionamento) a baixo, assim como no [Modelo Relacional](#modelo-relacional). Para entender melhor o que é cada tipo de dado, basta visualizar o [Dicionário de Dados](#dicionário-de-dados).

Os arquivos de criação do banco de dados podem ser encontrados na pasta sql. Todos os scripts, com excessão do [script_007.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_007.sql), devem ser executados para a criação do banco de dados completo.

O [script_007.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_007.sql) é apenas para teste, onde diversos dados são adicionados ao banco.

* Arquivos sql
  * [script_001.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_001.sql)
    * Criação inicial do banco de dados
  * [script_002.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_002.sql)
    * Criar o trigger que adiciona pássaros na tabela dos pássaros, quando vem de adicição de prefêrencia ou quando um pássaro novo é mencionado em um post
  * [script_003.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_003.sql)
    * Criar o trigger que deleta lógicamente um post e todas as linhas de outras tabelas que são dependentes do mesmo post
  * [script_005.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_005.sql)
    * Altera algumas tabelas do banco de dados com novas colunas
  * [script_006.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_006.sql)
    * Criar a view que possibilita a visualização dos usuários mais populares de cada cidade, ordenado por ordem alfabetica de cidade
  * [script_007.sql](https://github.com/decoejz/bird_box/blob/master/sql/script_007.sql)
    * Adicição de dados apenas para testes

## Requisitos

O projeto veio com a necessidade de diversos requisitos. Eles podem ser vistos na lista a baixo:

* Usuários
  * Adicionar um usuário novo
  * Adicionar prefêrencia de pássaros
* Post
  * Adicionar post
  * Apagar logicamente um post
  * Referenciar outros usuários
  * Referenciar pássaros
  * Guardar informações de visualização
  * Joinhas e anti-joinhas dos usuários que visualizarem
  
Devem existir alguns tipos de visualização basicas para consultas:

* Basicas
  * Usuários existentes
  * Post existente por usuário em ordem cronológica reversa
  * Usuário mais popular de cada cidade
* Avançados
  * Lista de usuários que referenciam um dado usuário
  * Tabela cruzada de quantidade de aparelhos por tipo de sistema operacional e por browser
  * Lista com URLs de imagens e respectivos #tags de tipo de pássaro
* Extra
  * Visualização de quantos joinhas, anti-joinhas e indiferenças um dado post teve

O arquivo com a definição dos métodos disponíveis esta em [projeto.py](https://github.com/decoejz/bird_box/blob/master/projeto.py).

## Modelo Entidade Relacionamento
![Imagem Indisponível](https://github.com/decoejz/bird_box/blob/master/img/ent_rela.PNG)

## Modelo Relacional

![Imagem Indisponível](https://github.com/decoejz/bird_box/blob/master/img/modelo-relacional.PNG)

## Dicionário de Dados

![Imagem Indisponível](https://github.com/decoejz/bird_box/blob/master/img/dicionario.PNG)
