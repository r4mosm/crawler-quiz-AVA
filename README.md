# Scrapper para Quiz da plataforma AVA


Este scrapper extrai dados do quiz (recurso questionário). 

Para cada tentativa realizada do questionário o programa gera uma pasta com o nome do aluno que fez a tentativa e que contém: 

* a página do quiz em formato html
* os arquivos anexados pelo aluno
* os arquivos anexados pelo professor

### Como usar

```
python3 scrapy.py username
```

onde `username` é o CPF do usuário. Será pedido a senha e a página com as tentativas do quiz.



### Licença 
[MIT](https://choosealicense.com/licenses/mit/)

### Exemplo

Veja um exemplo de página que deve ser passada para o script. Para melhor controle, organize as tentativas por ordem alfabética do nome dos alunos.

![alt text](https://github.com/r4mosm/crawler-quiz-AVA/blob/main/AVA_page_quiz.png?raw=true)
