# Crawler para Quiz da plataforma AVA


Este crawler extrai dados do quiz ("recurso questionário"). 

Para cada tentativa realizada do questionário o programa gera uma pasta com o nome do aluno que fez a tentativa e que contém: 

* a página do quiz em formato html
* os arquivos anexados pelo aluno
* os arquivos anexados pelo professor

### Como usar

```
scrapy.py [-h] username
```

onde `username` é o CPF do usuário. Será pedido a senha e a página com as tentativas do quiz.



### Licença 
[MIT](https://choosealicense.com/licenses/mit/)



