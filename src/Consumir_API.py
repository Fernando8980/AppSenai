import asyncio
from cProfile import label

import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, \
    FontWeight, View, FloatingActionButton, Icons, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, DropdownOption
from flet.controls import page, colors
from flet.controls.border_radius import horizontal
from datetime import datetime

from flet.controls.core.canvas import Color
from flet.controls.material import icons
from markdown_it.rules_block import lheading

from src.api_endpoints_viacep import get_ceps


# Configurações
def main(page: flet.Page):
    # Configuraçoes
    page.title = "Exemplo de Listas"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode.light
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def ceps():
            cep = input_cep.value
            numero_casa = input_numero_casa.value

            tem_error = False
            if cep:
                input_cep.error = None
            else:
                tem_error = True
                input_cep.error = "campo obrigatorio"

            if numero_casa:
                input_numero_casa.error = None
            else:
                tem_error = True
                input_numero_casa.error = "campo obrigatorio"

            if not tem_error:


                endereco = get_ceps(cep)
                text_cidade.value = endereco["localidade"]
                text_uf.value = endereco["uf"]
                text_logradouro.value = endereco["logradouro"]
                text_bairro.value = endereco["bairro"]





    # Gerenciar as Telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/Tela Inicial",
                controls=[
                    flet.AppBar(
                        title="Cadastro de Localização",
                    ),
                    input_cep,
                    input_numero_casa,
                    text_cidade,
                    text_uf,
                    text_logradouro,
                    text_bairro,
                    btn_salvar,
                    list_view

                ],

                )
            )




            # Voltar

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_cep = TextField(label="CEP", hint_text="Digite o CEP", on_submit=ceps)
    input_numero_casa = TextField(label="Digite o Numero da Casa", hint_text="Digite o Numero da Casa", on_submit=ceps)
    text_cidade = TextField(label="Cidade:")
    text_uf = TextField(label="UF:")
    text_logradouro = TextField(label="logradouro:")
    text_bairro = TextField(label="bairro:")


    btn_salvar = Button("salvar", width=400, on_click=lambda: ceps())

    list_view = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)