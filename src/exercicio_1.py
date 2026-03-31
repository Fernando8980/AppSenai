import asyncio

import flet
from flet import ThemeMode, View, control, AppBar, Colors, Button, Text, TextField


def main(page: flet.Page):
    # configuraçãoes
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # funções
    def exibir_msg():
        text_msg.value = f"Bom dia {input_nome.value}, Tudo bem?"
        input_nome.value = ""
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
                    AppBar(
                        title="Primeira pagina",
                        bgcolor=Colors.AMBER_200,
                    ),
                    Text("digite seu nome para receber uma mensagem"),
                    input_nome,
                    btn_salvar,
                ]

            )

        )
        if page.route == "/tela_msg":
            page.views.append(
                View(
                    route="/tela_msg",
                    controls=[
                        AppBar(
                            title="Segunda pagina",
                        ),
                        text_msg,
                    ]

                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componetes


    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    input_nome = TextField(label="Nome")
    text_msg = Text()
    btn_salvar = Button("Salvar", on_click=exibir_msg)

    route_change()


flet.run(main)
