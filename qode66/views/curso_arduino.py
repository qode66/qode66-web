import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color as Color

def curso_arduino() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.flex(
                rx.heading(
                    "Tutorial de Arduino",
                    style=styles.portfolio_heading,
                    ),
                rx.text(
                    "Descobreix la potència d’Arduino mentre explorem el seu hardware senzill, el seu programari fàcil d’utilitzar i les inacabables possibilitats de projectes. Des de circuits bàsics fins a robòtica avançada, aquest tutorial et dotarà del coneixement i les habilitats per fer realitat les teves idees.",
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
                        href="https://github.com/qode66/arduino-scratch",
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
                    src="/images/arduino-sensors.png",
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