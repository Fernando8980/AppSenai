import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, TextButton, Container, Colors, \
    FontWeight
from datetime import datetime


def main(page: flet.Page):
    # configuraçãoes
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        text.value = f"bom dia {input_nome.value} {input_sobrenome.value} "
        page.update()

    def numero_par_impar():
        if int(input_numero.value) % 2 == 0:
            text_idade.value = f"o numero {input_numero.value} é par"
            page.update()
        else:
            text_idade.value = f"o numero {input_numero.value} é impar"
        page.update()

    def calcular_idade():
        ano_nascimento = int(input_data.value)
        idade = datetime.now().year - ano_nascimento

        if idade >= 18:
            text_data.value = f"Voce tem {idade} anos e é maior de idade"

        else:
            text_data.value = f"Voce tem {idade} anos e é menor de idade"

    # Componentes
    text = Text()
    text_idade = Text()
    text_data = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    input_numero = TextField(label="Numero")
    btn_verificar = OutlinedButton("Verificar", on_click=numero_par_impar)

    input_data = TextField(label="Digite o Ano de Nascimento", hint_text="Ex:1999")
    btn_calcular = TextButton("Calcular idade", on_click=calcular_idade)

    # Construção da tela

    page.add(
        Column(
            [
                Container(
                    Column([
                        Text("Atividade 1", weight=FontWeight.BOLD, size=24),
                        input_nome,
                        input_sobrenome,
                        btn_salvar,
                        text,
                    ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=Colors.BLUE_500,
                    padding=15,
                    border_radius=10,
                    width=400,

                ),
                Container(
                    Column([
                        Text("Atividade 2", weight=FontWeight.BOLD, size=24),
                        text_idade,
                        input_numero,
                        btn_verificar,
                    ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ), bgcolor=Colors.BLUE_500,
                    padding=15,
                    border_radius=10,
                    width=400,
                ),
                Container(
                    Column([
                        Text("Atividade 3", weight=FontWeight.BOLD, size=24),
                        text_data,
                        input_data,
                        btn_calcular,
                    ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ), bgcolor=Colors.BLUE_500,
                    padding=15,
                    border_radius=10,
                    width=400,
                ),

            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    )


flet.app(main)
