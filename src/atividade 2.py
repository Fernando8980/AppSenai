import asyncio
from asyncio import create_task
from datetime import datetime
import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight, View, AppBar, FloatingActionButton, Icons, ListView, Card, Row, Icon, ListTile, PopupMenuButton, \
    PopupMenuItem

class Cartao():
    def __init__(self, nome, limite, bandeira):
        self.limite = limite
        self.nome = nome
        self.bandeira = bandeira


def main(page: flet.Page):
    # configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    def montar_lista_padrao():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.CREDIT_CARD_OUTLINED),
                    title=item.nome,
                    subtitle=item.bandeira,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhe", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, pessoa=item: ver_detalhes (pessoa)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE),
                        ]
                    ),

                )
            )

    def ver_detalhes(Cartao):
        text_nome.value = Cartao.nome
        text_limite.value = Cartao.limite
        text_bandeira.value = Cartao.bandeira

        navegar("/detalhes")



    def salvar_dados():
        nome = input_nome.value.strip()
        limite = input_limite.value.strip()
        bandeira = input_bandeira.value.strip()

        tem_erro = False
        if nome:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatório"

        if limite:
            input_limite.error = None
        else:
            tem_erro = True
            input_limite.error = "Campo obrigatório"

        if bandeira:
            input_bandeira.error = None
        else:
            tem_erro = True
            input_bandeira.error = "Campo obrigatório"

        if not tem_erro:
            cartao = Cartao(
                nome=nome,
                limite=limite,
                bandeira=bandeira,
            )

            lista_dados.append(cartao)
            input_nome.value = ""
            input_limite.value = ""
            input_bandeira.value = ""

        montar_lista_padrao()

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        montar_lista_padrao()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Lista de Cartoes",
                    ),
                    list_view
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro")
                )

            )
        )
        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro de cartoes",
                        ),
                        input_nome,
                        input_limite,
                        input_bandeira,
                        btn_salvar,
                    ]
                )
            )

        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                        ),
                        Icon(Icons.AD_UNITS_ROUNDED),
                        text_nome,
                        text_limite,
                        text_bandeira,
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro")
                    )

                )
            )


    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_nome = TextField(label="Nome", hint_text="Digite o nome do cartao", on_submit=salvar_dados)
    input_limite = TextField(label="Limite", hint_text="Digite a limite do cartao", on_submit=salvar_dados)
    input_bandeira = TextField(label="bandeira", hint_text="Digite a bandeira do cartao", on_submit=salvar_dados)

    text_nome = Text(weight=FontWeight.BOLD, size=24)
    text_limite = Text()
    text_bandeira = Text()

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)