import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color as Color

def guiamarkdown() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.flex(
                rx.heading(
                    "Guia Markdown",
                    style=styles.portfolio_heading,
                    ),
                rx.text(
                    "Traducció al català/valencià de Markdown Guide. La Guia Markdown és una guia de referència lliure i de codi obert que explica com utilitzar Markdown, el llenguatge de marcatge senzill i fàcil d'utilitzar que podeu utilitzar per formatar pràcticament qualsevol document.",
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
                        href="https://github.com/qode66/guia-markdown-ca",
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
                    src="/images/markdown.png",
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