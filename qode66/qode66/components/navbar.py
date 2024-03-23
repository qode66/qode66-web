import reflex as rx
import qode66.styles.styles as styles
from qode66.styles.fonts import Font, Weight

from qode66.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/images/quique-rounded.png",
                    height="30px",
                    width="auto",
                ),
                rx.text(
                    "Quique Serrano",
                    size="5",
                    weight="regular",
                    color=Color.ACCENT1.value,
                    font_family=Font.TITLE.value,
                    font_weight=Weight.MEDIUM.value,
                    font_style="italic",
                ),
            ),
            rx.spacer(),
            rx.hstack(
                rx.link(
                    "Inici",
                    href="/",
                    color=Color.TEXTCOLOR.value,
                ),
                rx.link(
                    "Portfoli",
                    href="/portfolio",
                    color=Color.TEXTCOLOR.value,
                ),
                rx.link(
                    "Quant a",
                    href="/about",
                    color=Color.TEXTCOLOR.value,
                ),
                style=styles.navbar_link_style,
            ),
        ),
        position="sticky",
        justify="center",
        align="center",
        width="100%",
        height="60px",
        background=Color.BACKGROUND1.value,
        margin_top="20px",
    )
