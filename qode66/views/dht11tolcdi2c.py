import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color as Color

def dht11tolcdi2c() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.flex(
                rx.heading(
                    "Monitoratge ambiental amb DHT11 i LCD 16x2",
                    style=styles.portfolio_heading,
                    ),
                rx.text(
                    "El projecte que presentem consisteix en la implementació d'un sistema de monitoratge ambiental utilitzant un sensor DHT11 i una pantalla LCD 16x2. El sensor DHT11 és capaç de mesurar la temperatura i la humitat de l'ambient en el qual està instal·lat, mentre que la pantalla LCD 16x2 s'utilitza per a visualitzar les dades obtingudes pel sensor.",
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
                        href="https://github.com/cartrotech/DHT11-to-LCD16x02",
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
                    src="/images/DHT11toLCDI2C.png",
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
            padding_bottom="10px",

        ),
        margin_top="10px",
        margin_bottom="10px",
    )