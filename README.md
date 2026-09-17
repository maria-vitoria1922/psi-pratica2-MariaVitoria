# README.md

1. Onde estão os modelos ORM no seu projeto?
 Os modelos ORM estão no arquivo models.py nas classes Autor e Livro.

2. Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?
 A classe Autor é o lado "um", pois um autor pode ter vários livros, já a classe Livro é o lado "muitos", pois vários livros podem pertencer a um autor.

3. Para que serve o ForeignKey em Livro.autor_id ?
O ForeignKey em autor_id serve para ligar um livro a um autor
No código:

```
autor_id: Mapped[int] = mapped_column(ForeignKey('autores.id'))
```

Ele indica que o autor_i` é usado para fazer essa ligação.
