import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, TextField, Text, OutlinedButton, Column, Container, \
    CrossAxisAlignment


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.LIGHT # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # funções
    def exibir_msg():
        text_banco.value = f"Banco: {input_banco.value}"
        text_limite.value = f"Limite: {input_limite.value}"
        text_bandeira.value = f"Bandeira: {input_bandeira.value}"

        tem_erro = False
        if input_banco.value:
            input_banco.error = None
        else:
            tem_erro = True
            input_banco.error = "Campo obrigatorio"

        tem_erro = False
        if input_limite.value:
            input_limite.error = None
        else:
            tem_erro = True
            input_limite.error = "Campo obrigatorio"

        if input_bandeira.value:
            input_bandeira.error = None
        else:
            tem_erro = True
            input_bandeira.error = "Campo obrigatorio"

        if not tem_erro:
            input_banco.value = ""
            input_limite.value = ""
            input_bandeira.value = ""
            navegar("/tela_msg")

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Preencha os dados sobre o cartão",
                        bgcolor=Colors.AMBER_200,
                    ),
                    Text("Preencha os campos"),
                    input_banco,
                    input_limite,
                    input_bandeira,
                    btn_salvar
                ]
            )
        )
        if page.route == "/tela_msg":
            page.views.append(
                View(
                    route="/tela_msg",
                    controls=[
                        flet.AppBar(
                            title="Informações sobre o cartão",
                        ),
                        Container(
                            Column([
                                text_banco,
                                text_limite,
                                text_bandeira,
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.AMBER_500,
                            width= 500,
                            padding=15,
                            border_radius=10
                        )

                    ]
                ),

            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    # Componentes

    text_banco = Text()
    text_limite = Text()
    text_bandeira = Text()
    btn_salvar = Button("Salvar", on_click=exibir_msg)
    input_banco = TextField(label="Digite o nome do seu Banco")
    input_limite = TextField(label="Digite o Limite que você tem")
    input_bandeira = TextField(label="Digite a Bandeira que você tem")



    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)