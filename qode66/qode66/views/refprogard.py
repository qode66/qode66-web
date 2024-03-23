import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color as Color

def refprogard() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.flex(
                rx.heading(
                    "Referència de programació d'arduino",
                    style=styles.portfolio_heading,
                    ),
                rx.text(
                    "Traducció al català/valencià de arduino/reference-en, la documentació de referència del llenguatge de la sintaxi d’Arduino.",
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
                    src="/images/arduino-refprog.png",
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