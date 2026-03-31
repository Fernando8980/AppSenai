import asyncio

import flet
from flet import ThemeMode, View, control, AppBar, Colors, Button, Text, TextField, FontWeight
from flet.controls import buttons


def main(page: flet.Page):
    # configuraçãoes
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # funções
    def exibir_msg():
        text_nome.value = f"nome: {input_nome.value}"
        text_cpf.value = f"cpf: {input_cpf.value}"
        text_email.value = f"email: {input_email.value}"
        text_salario.value = f"salario: {input_salario.value}"

        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = f"campo obrigatorio"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = f"campo obrigatorio"

        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = f"campo obrigatorio"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = f"campo obrigatorio"
        if not tem_erro:
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                        title="Cadastro Funcionário",
                        bgcolor=Colors.AMBER_500,
                    ),
                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,
                    btn_salvar
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
                        text_nome,
                        text_cpf,
                        text_email,
                        text_salario,

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
    text_nome = Text("")
    text_cpf = Text("")
    text_email = Text("")
    text_salario = Text("")

    input_nome = TextField(label="Nome")
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="E-mail")
    input_salario = TextField(label="salario")

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    input_nome = TextField(label="Nome")
    text_msg = Text()
    btn_salvar = Button("Salvar", on_click=exibir_msg)

    route_change()


flet.run(main)
