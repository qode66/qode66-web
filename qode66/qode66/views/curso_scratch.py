import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color as Color

def curso_scratch() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.flex(
                rx.heading(
                    "Tutorial Scratch for Arduino S4A",
                    style=styles.portfolio_heading,
                    ),
                rx.text(
                    "Scratch for Arduino S4A és un entorn senzill i divertit per als alumnes mes joves, que els inicia en aqueix camí i els introdueix a els conceptes inherents a la programació estructurada d'una manera que sembla un joc, però amb moltes mes profunditat del que a primera vista es percep.",
                    style=styles.portfolio_text,
                ),
                rx.card(
                    rx.link(
                        rx.flex(
                            rx.avatar(src="/icons/github.png"),
                            rx.text("Veure a GitHub", color="black"),
                            spacing="2",
                            align="center",
                            
                        ),
                        href="https://github.com/qode66/arduino-tutorial",
                        is_external=True,
                    ),
                    background=Color.TEXTCOLOR.value,
                    _hover={"opacity": "0.5"},
                ),
                width="50%",
                direction="column",
                justify="center",
                align="center",
            ),
            rx.flex(
                rx.image(
                    src="/images/arduino-scratch.png",
                    width="300px",
                    height="auto",
                    ),
                width="50%",
                justify="center",
                align="center",
                padding="10px",
            ),
            direction="row",
            background=Color.BACKGROUND2.value,

        ),
        margin_top="10px",
        margin_bottom="10px",
    )