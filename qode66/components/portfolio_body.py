import reflex as rx

from qode66.views.curso_scratch import curso_scratch
from qode66.views.curso_arduino import curso_arduino
from qode66.views.refprogard import refprogard
from qode66.views.guia_markdown import guiamarkdown
from qode66.views.dht11tolcdi2c import dht11tolcdi2c
from qode66.styles.colors import Color as Color

def portfolio_body() -> rx.Component:
    return rx.container(

# Secció cursos

        rx.section(
            rx.center(
                rx.heading(
                    "Portfoli",
                    color=Color.ACCENT1.value,
                    font_size="40px",
                    margin_bottom="20px",
                    ),
            ),
            rx.section(
                rx.heading(
                    "Arduino",
                    color=Color.ACCENT1.value,
                    font_size="32px",
                    margin="20px",
                ),
                dht11tolcdi2c(),
            ),
            rx.section(
                rx.heading(
                    "Traduccions",
                    color=Color.ACCENT1.value,
                    font_size="32px",
                    margin="20px",
                ),
                curso_scratch(),
                curso_arduino(),
                refprogard(),
                guiamarkdown(),
            ),
        ),
    )