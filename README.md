<h1 align="center">Sistema de Votação</h1>

<p align="center">
 <a href="#sobre">Sobre</a> &nbsp;|&nbsp;
 <a href="#porque">Por Que</a> &nbsp;|&nbsp;
 <a href="#tecnologias">Tecnologias</a> &nbsp;|&nbsp;
 <a href="#funcionalidades">Funcionalidades</a> &nbsp;|&nbsp;
 <a href="#autor">Autor</a> &nbsp;|&nbsp;
 <a href="#license">Licença</a>
</p>

<h6 align="center"> 
	Se você quiser visualizar as imagens do aplicativo, clique <a href="#autor">aqui</a>.
</h6>

<h3 id="sobre">:information_source: Sobre</h3>

> Este projeto foi desenvolvido utilizando o django framework como back-end o framework Materialize como front-end. 

A ideia é:

_"Criar um Sistema de Votação onde o mesma tenha um design simples e belo, com intuito de promover o aprendizado utilizando o Django framework"_

--------------------------------------------------------------------------------------

<h3 id="porque">:question: Por Que</h3>

Este projeto faz parte do meu portfólio pessoal, então, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer funcionalidade&melhoria que você possa relatar para melhora-lo.

Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você que manda!

Este é um projeto totalmente grátis!

--------------------------------------------------------------------------------------

<h3 id="tecnologias">:rocket: Tecnologias</h3>

As seguintes ferramentas foram usadas na construção do projeto:

- [Django Framework](https://www.djangoproject.com/)
- [Materialize](https://materializecss.com/)

--------------------------------------------------------------------------------------

<h3 id="funcionalidades">:sparkles: Funcionalidades</h3>

-[] CRUD de votações

--------------------------------------------------------------------------------------

<h3 id="instalando">:computer: Instalando o Projeto</h3>

#### Linux

> **Observação:** Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

**Clonando o Repositório**

```
git init

git clone git@github.com:LucasSantus/sistema-votacao.git

cd sistema-votacao
```

**Preparando Ambiente Virtual**

Com o terminal aberto, digite:

```
python3 -m venv env

source env/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

**Iniciando o Projeto**

```
python manage.py makemigrations home

python manage.py makemigrations usuarios

python manage.py makemigrations votacao

python manage.py makemigrations usuarios

python manage.py migrate

python manage.py runserver
```

**Criando Super Usuário**

```
python manage.py createsuperuser
```

para visualizar o projeto: http://127.0.0.1:8000/


**Acessando o Admin**

Com o projeto rodando, adicione o 'admin/' dps da URL:

http://127.0.0.1:8000/admin/

--------------------------------------------------------------------------------------

<h3 id="autor">:bust_in_silhouette: Autor</h3>

<div align="left"> 
	<a href="https://github.com/LucasSantus">
		<img style="border-radius: 50%;" src="https://github.com/LucasSantus.png" width="100px;" alt=""/>
		<br />
		Lucas Santus
	</a>
</div>
<br />
Feito com ❤️ por Lucas Santus!<br />
Obrigado por visitar e boa codificação!<br />

--------------------------------------------------------------------------------------

<h3 id="license">:memo: License</h3>

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/sistema-votacao/blob/master/LICENSE) para melhores detalhes.
