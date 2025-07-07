# 🚀 Implementação de Provedor de Serviços de Internet Usando Micro Serviços Docker

## ℹ️ Visão Geral do Projeto

Este projeto implementa uma infraestrutura completa de Provedor de Serviços de Internet (ISP) utilizando microsserviços e Docker. Desenvolvido para a disciplina de Administração de Sistemas Abertos (ASA) no IFRN - Natal Central, ao longo de 8 semanas, sob a orientação do professor Sales Filho ([@salesfilho](https://github.com/salesfilho)), a solução integra princípios de Infrastructure as Code (IaC) e DevOps para um sistema modular e escalável.

## 👥 Equipe

* [@Donutzy](https://github.com/Donutzy) - Gilson dos Santos Filho
* [@VitorRamos05](https://github.com/VitorRamos05) - Vitor Hugo Ramos Crisóstomo 
* [@vazgabriel97](https://github.com/vazgabriel97) - Gabriel Vaz Fernandes de Oliveira

## 🧱 Arquitetura da Rede do ISP

A arquitetura da rede do ISP implementada neste projeto se baseia na distribuição de serviços para múltiplos clientes, garantindo isolamento e segurança. Os principais componentes incluem:

    Proxy Reverso: Atua como ponto de entrada para os serviços, distribuindo o tráfego e garantindo segurança SSL/TLS.

    Serviços de DNS, E-Mail e Webmail: Oferecidos centralmente pelo ISP.

    Portais e CMS dos Clientes: Cada cliente possui sua própria infraestrutura isolada, acessada via o proxy reverso.

## 📂 Estrutura
```plaintext
├── docker-compose.yml
├── ISP/
│   ├── DNS/
│   │   ├── Dockerfile
│   │   ├── db.asa.br
│   │   └── named.conf.local
│   ├── Proxy-Reverso/
│   │   └── Dockerfile
│   ├── E-Mail/
│   │   └── Dockerfile
│   └── Web-Mail/
│       └── Dockerfile
├── Client 1/
│   │
├── Client 2/
│   │
└── Client 3/
    │
```
## 📝 Descrição dos Diretórios

  * **DNS**: Contém as configurações para o servidor DNS (Bind9).
  * **E-Mail**: Inclui os arquivos necessários para os serviços de e-mail (Postfix e Dovecot).
  * **Web-Mail**: Inclui os arquivos necessários para o serviçi de web mail (Roundcube).
  * **Proxy-Reverso**: Contém as configurações para o proxy reverso (Traefik).

-----

## 📦 Lista de Entregas

As entregas do projeto são divididas para garantir o acompanhamento e a validação contínua:

| ID | Nome                          | Descrição                                                                                                                              |
| :-- | :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Artefatos de Gerenciamento    | Documentos de planejamento e execução (cronogramas, tarefas, atas de reunião, relatórios, etc.).                                       |
| 2  | Artefatos da Infraestrutura do Provedor | Códigos versionados, relatório de testes e manual de implantação (passo a passo em vídeo) para a infraestrutura central do ISP. |
| 3  | Artefatos da Infraestrutura do Cliente 1 | Códigos versionados, relatório de testes e manual de implantação (passo a passo em vídeo) para o Cliente 1.                         |
| 4  | Artefatos da Infraestrutura do Cliente 2 | Códigos versionados, relatório de testes e manual de implantação (passo a passo em vídeo) para o Cliente 2.                         |
| 5  | Artefatos da Infraestrutura do Cliente 3 | Códigos versionados, relatório de testes e manual de implantação (passo a passo em vídeo) para o Cliente 3.                         |
| 6  | Apresentação Final            | Pitch de final de projeto, apresentado em sala por toda a equipe, mostrando e explicando em slides e vídeo os resultados obtidos.       |

## 🗓️ Cronograma (8 Semanas)

O projeto foi estruturado em Sprints semanais para otimizar o desenvolvimento e as entregas:

  * **Semana 2 (Sprint 1):** Entregas 1 e 2 (Artefatos de gerenciamento e da Infraestrutura do Provedor).
  * **Semana 4 (Sprint 2):** Artefatos de gerenciamento e da Infraestrutura do Cliente 1.
  * **Semana 6 (Sprint 3):** Artefatos de gerenciamento, Infraestrutura dos Clientes 2 e 3.
  * **Semana 8 (Sprint 4):** Artefatos de gerenciamento, documentação e Apresentação final.

## 🏆 Resultados Esperados

Ao final do projeto, esperamos alcançar os seguintes resultados:

1.  Todas as entregas do projeto realizadas conforme especificado e dentro do prazo estabelecido.
2.  Desenvolvimento aprofundado de competências técnicas em Administração de Sistemas Abertos e serviços.
3.  Aprimoramento de habilidades interpessoais e de trabalho em equipe.
4.  Produção de material de alta qualidade para o portfólio dos discentes e da Diretoria.
5.  Aplicação e expansão dos conceitos técnicos aprendidos em sala de aula.


