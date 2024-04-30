import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color as Color

def cartrobot() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.flex(
                rx.heading(
                    "Cartrobot",
                    style=styles.portfolio_heading,
                    ),
                rx.text(
                    "El projecte «Cartrobot» és la construcció amb cartró i l'electrònica necessària d'un robot capaç de caminar i que estiga controlat per bluetooth. Està basat en models publicats en internet i de codi lliure.",
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
                        href="https://github.com/cartrotech/Cartrobot",
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
                    src="/images/cartrobot.png",
                    width="300px",
                    height="auto",
                    ),
                width="50%",
                justify="center",
                align="center",
                padding="10px",
            ),
            direction="row",
            background=Color.BACKGROUND1.value,

        ),
        margin_top="10px",
        margin_bottom="10px",
    )