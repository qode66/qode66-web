import reflex as rx

from qode66.styles.colors import Color as Color
from qode66.styles.fonts import Font, Weight

def home_body() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.vstack(
                rx.text(
                    "Un disseny per ",
                    rx.text.strong("captivar,", color="#3ece56"),
                    " un lloc per ",
                    rx.text.strong("connectar.", color="#3ece56"),
                    class_name="animate__animated animate__bounceInLeft",
                    font_family=Font.TITLE.value,
                    font_weight=Weight.BOLD.value,
                    align="center",
                    size="9",
                    color=Color.TEXTCOLOR.value,
                    width="80%",
                    margin="2px",
                    padding="10px",
                ),
                rx.text(
                    "Soc desenvolupador web en constant creixement i CEO fundador de CartroTech, la fusió entre artesania i tecnologia",
                    font_family=Font.TEXT.value,
                    font_weight=Weight.LIGHT.value,
                    align="center",
                    size="4",
                    color=Color.TEXTCOLOR.value,
                    width="80%",
                    margin="2px",
                    padding="10px",
                ),
            ),
            rx.image(
                src="/images/ilustracio-1.png",
                width="300px",
                height="auto",
                margin="10px",
            ),
            background_color=Color.BACKGROUND1.value,
            color=Color.TEXTCOLOR.value,
            align="center",
            width="100%",
            height="70vh",
        )
    )


