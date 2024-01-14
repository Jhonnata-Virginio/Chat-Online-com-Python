# Modelo do Projeto:
    # Titulo - Chat Online
    # Botão de Iniciar o Chat
        # Popup
            # Mensagem de Bem Vindo
            # Caixa para escrever o nome
            # Entrar no Chat
    # Chat
        # Usuario entrou no Chat
        # Mensagem do Usuario
    # Caixa de enviar mensagem
    # Botão de enviar

import flet as ft

def main(pagina):
    def iniciarChat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    def entrarChat(evento):
        popup.open = False
        pagina.remove(botaoIniciar)
        pagina.add(chat)
        linhaMensagem = ft.Row([campoMensagem, botaoEnviar])
        pagina.add(linhaMensagem)
        textoEntrou = f'{nomeUsuario.value} entrou no chat!'
        pagina.pubsub.send_all(textoEntrou)
        pagina.update()

    def enviarMensagem(evento):
        texto_campoMensagem = f'{nomeUsuario.value}: {campoMensagem.value}'
        pagina.pubsub.send_all(texto_campoMensagem)
        campoMensagem.value = ''
        pagina.update()
    
    def enviarMensagemTunel(info):
        chat.controls.append(ft.Text(info))
        pagina.update()
        

    titulo = ft.Text('Chat Online - Desenvolvido por Jhonnata Virginio')
    nomeUsuario = ft.TextField(label='Escreva seu nome', on_submit=entrarChat)
    botaoIniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciarChat)


    chat = ft.Column()
    campoMensagem = ft.TextField(label='Escreva sua mensagem aqui', on_submit=enviarMensagem)
    botaoEnviar = ft.ElevatedButton('Enviar', on_click=enviarMensagem)

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text('Bem Vindo ao Chat'),
        content=nomeUsuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrarChat)]
    )

    pagina.pubsub.subscribe(enviarMensagemTunel)


    pagina.add(titulo)
    pagina.add(botaoIniciar)



ft.app(main, view=ft.WEB_BROWSER)