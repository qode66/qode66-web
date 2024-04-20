import reflex as rx

from enum import Enum
from qode66.styles.colors import Color
from qode66.styles.fonts import Font, Weight

STYLESHEETS = [

    "https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700;900&display=swap",
    "https://fonts.googleapis.com/css2?family=Raleway:wght@100..900&display=swap",
    # "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
]

BASE_STYLE = {
    "font_family": Font.TEXT.value,
    "font_weight": Weight.LIGHT.value,
    "background_color": Color.BACKGROUND1.value,

    rx.heading: {
        "color": Color.TEXTCOLOR.value,
        "font_family": Font.TITLE.value,
        "font_weight": Weight.BOLD.value,
    },

    rx.link: {
        "color": Color.TEXTCOLOR.value,
        "text_decoration": "none",
        "_hover": {
            "color": Color.ACCENT1.value,
        }
    }
}

navbar_link_style = dict(
    font_family=Font.TITLE.value,
    font_weight=Weight.BOLD.value,
    font_size="14px",
    color=Color.TEXTCOLOR.value,
    )

footer_heading_style = dict(
    font_family=Font.TITLE.value,
    font_weight=Weight.BOLD.value,
    font_size="14px",
    color=Color.TEXTCOLOR.value,
)

footer_link_style = dict(
    font_family=Font.TEXT.value,
    font_weight=Weight.LIGHT.value,
    )

about_section1_text = dict(
    font_family=Font.TEXT.value,
    font_weight=Weight.LIGHT.value,
    font_size="16px",
    padding_top="5px",
    paddig_bottom="5px",
)

about_even_section = dict(
    padding_left="30px",
    padding_right="30px",
    color=Color.BACKGROUND1.value,
    background_color=Color.ACCENT1.value,
    size="1",
)

about_odd_section = dict(
    padding_left="30px",
    padding_right="30px",
    color=Color.TEXTCOLOR.value,
    background_color=Color.BACKGROUND1.value,
    size="1",
)

portfolio_text = dict(
    font_family=Font.TEXT.value,
    font_weight=Weight.LIGHT.value,
    font_size="16px",
    color=Color.TEXTCOLOR.value,
    padding="20px",
)

portfolio_heading = dict(
    font_family=Font.TITLE.value,
    font_weight=Weight.BOLD.value,
    font_size="32px",
    color=Color.ACCENT2.value,
    padding="20px",
)