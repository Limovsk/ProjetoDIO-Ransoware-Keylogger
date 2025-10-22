# Projeto DIO - Ransoware & Keylogger

Este projeto tem o propósito de aplicar na prática os principais conceitos de segurança ofensiva em ambientes controlados. As ferramentas desenvolvidas reproduzem comportamentos reais de ameaças cibernéticas, possibilitando uma análise detalhada das técnicas empregadas em testes de invasão (*pentests*) e investigações forenses.

---

## Objetivos

- Projetar simulações controladas de ransomware para estudar criptografia, mensagens de resgate e técnicas de mitigação em ambiente isolado.
- Implementar um keylogger simulado com registro e encaminhamento seguro de logs para fins de avaliação de detecção e resposta.
- Analisar o ciclo de ataque — infiltração, evasão e exfiltração de dados — dentro de um laboratório seguro e controlado.
- Adotar e promover boas práticas de desenvolvimento seguro e conduta ética durante toda a pesquisa.

---

## Tecnologias Utilizadas

| Tecnologia       | Finalidade                                                                 |
|------------------|------------------------------------------------------------------------------|
| **Python**       | Linguagem predominante para a criação de scripts                    |
| **pynput**       | Registro de eventos de teclado para o keylogger                             |
| **smtplib**      | Envio de mensagens eletrônicas utilizando o protocolo SMTP                                      |
| **email.mime**   | Estruturação de mensagens para transmissão de registros                               |
| **threading.Timer** | Realização regular do envio de informações coletadas                        |
| **cryptography** | Ransomware com criptografia de arquivos simétrica                           |
| **pip**          | Gerenciador de pacotes para a instalação de bibliotecas                   |
| **stdlib**       | Utilitários nativos do Python para gerenciamento de arquivos e sistema       |

---

## Módulo 1 – Ransomware

- Realiza a criptografia de arquivos específicos ou de diretórios completos.
- Emprega uma chave secreta para o processo de descriptografia.
- Mostra mensagem de resgate como se fosse um ataque verdadeiro.
- Possibilita a segmentação com base na extensão do arquivo.

---

## Módulo 2 – Keylogger

- Registro de teclas com filtragem de caracteres indesejáveis.
- Execução discreta com a extensão `.pyw` para esconder a janela no Windows.
- Os registros são enviados automaticamente por e-mail a cada 60 segundos.
- Ativação da autenticação em dois fatores com senha de aplicativo no Gmail.

---

## Mitigações

**Antivírus**

* Use soluções renomadas (ex.: Bitdefender, Kaspersky, Windows Defender).
* Mantenha definições de vírus sempre atualizadas.
* Agende varreduras automáticas regulares.
* Ative a proteção em tempo real.

**Firewall**

* Habilite o firewall de rede.
* Configure regras de tráfego de saída.
* Monitore conexões suspeitas.
* Utilize firewall de aplicação quando possível.

**Conscientização do Usuário**

* Não abra anexos de e-mails de remetentes desconhecidos.
* Verifique URLs antes de clicar.
* Use senhas fortes e autenticação multifator.
* Mantenha sistemas e aplicações sempre atualizados.

---

## Aviso Legal

Este projeto foi desenvolvido **exclusivamente para fins educacionais** em ambiente controlado. O uso indevido das ferramentas aqui descritas pode violar leis de privacidade e segurança digital. Sempre obtenha autorização explícita antes de realizar qualquer teste de intrusão.

---

## Contato

**Autor:** Gustavo Lima Costa  
**Local:** São Bernardo do Campo, SP  
**LinkedIn:** (https://www.linkedin.com/in/gustavo-limac/)  
**GitHub:** (https://github.com/Limovsk?tab=repositories)

