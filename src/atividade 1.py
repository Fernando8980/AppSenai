import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, \
    Column, control, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, FontWeight


class Perfil:
    def __init__(self, nome, profissao, sexo):
        self.nome = nome
        self.profissao = profissao
        self.sexo = sexo


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de Listas "
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # funções
    # navegar

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )

    def montar_lista_card():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row([
                        Icon(Icons.PERSON, color=Colors.BLUE),
                        Text(item)
                    ],
                        margin=8
                    ),
                )
            )

    def icone_genero(p1):
        if p1 == "Masculino":
            return Icon(Icons.BOY)
        elif p1 == "Feminino":
            return Icon(Icons.GIRL)

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=icone_genero(item.sexo),
                    title=item.nome,
                    subtitle=item.profissao,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, pessoa=item: ver_detalhes(pessoa)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )
    def ver_detalhes(pessoa):
        text_nome.value = pessoa.nome
        text_profissao.value = pessoa.profissao
        text_sexo.value = pessoa.sexo

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value
        profissao = input_profissao.value
        sexo = input_sexo.value

        tem_erro = False

        if nome:
            input_nome.error = None
        else:
            input_nome.error = "Campo obrigatório!"
            tem_erro = True

        if profissao:
            input_profissao.error = None
        else:
            input_profissao.error = "Campo obrigatório!"
            tem_erro = True

        if sexo:
            input_sexo.error = None
        else:
            input_sexo.error = "Campo obrigatório!"
            tem_erro = True

        if not tem_erro:
            p1 = Perfil(nome=nome.strip(), profissao=profissao.strip(), sexo=sexo.strip())
            lista_dados.append(p1)

        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Exemplos de Listas",
                        bgcolor=Colors.BLUE
                    ),
                    Button("Lista de texto", on_click=lambda: navegar("/lista_texto"), color=Colors.BLUE),
                    Button("Lista de Card", on_click=lambda: navegar("/lista_card"), color=Colors.BLUE),
                    Button("Lista padrão Android", on_click=lambda: navegar("/lista_padrao"), color=Colors.BLUE)

                ]
            )
        )

        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        AppBar(
                            title="Lista de texto",
                            bgcolor=Colors.BLUE

                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        AppBar(
                            title="Detalhes",
                            bgcolor=Colors.BLUE

                        ),
                        text_nome,
                        text_profissao,
                        text_sexo,

                    ]
                )
            )

        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        AppBar(
                            title="Lista de card",
                            bgcolor=Colors.BLUE

                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )

        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        AppBar(
                            title="Lista padrão de Android",
                            bgcolor=Colors.BLUE

                        ),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda: navegar("/form_cadastro"),
                    )
                )
            )

        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        AppBar(
                            title="Cadastro",
                            bgcolor=Colors.BLUE

                        ),
                        input_nome,
                        input_profissao,
                        input_sexo,
                        btn_salvar,

                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_nome = TextField(label="Nome", hint_text="Digite o seu nome: ", on_submit=salvar_dados)

    input_profissao = TextField(label="Profissao", hint_text="Digite sua Profissao: ", on_submit=salvar_dados)

    input_sexo = Dropdown(
        label="Genero",
        editable=True,
        options=[
            DropdownOption("Feminino"),
            DropdownOption("Masculino"),
        ],
    )

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    text_nome = Text(weight=FontWeight.BOLD, size=24)
    text_profissao = Text()
    text_sexo = Text()

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
