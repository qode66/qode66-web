import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color

def footer() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.center(
                rx.heading(
                    "© 2024-2030",
                    style=styles.footer_heading_style,
                ),
                rx.link(
                    "Qode66", 
                    href="mailto:qode66@gmail.com",
                    style=styles.footer_link_style,
                ),
                direction="column",
                width="10%",
            ),
            rx.center(
                rx.heading(
                    "Social",
                    style=styles.footer_heading_style,
                ),
                rx.link(
                    "Mastodon", 
                    href="https://mastodon.social/@qode66",
                    is_external=True,
                    style=styles.footer_link_style,
                ),
                rx.link(
                    "Github", 
                    href="https://github.com/qode66",
                    is_external=True,
                    style=styles.footer_link_style,
                ),
                rx.link(
                    "LinkedIn", 
                    href="https://www.linkedin.com/in/qserrano/",
                    is_external=True,
                    style=styles.footer_link_style,
                ),
                direction="column",
                width="10%",
            ),
            rx.center(
                rx.heading(
                    "Legal",
                    style=styles.footer_heading_style,
                ),
                rx.link(
                    "Privacitat", 
                    href="#",
                    style=styles.footer_link_style,
                ),
                rx.link(
                    "Galetes", 
                    href="#",
                    style=styles.footer_link_style,
                ),
                direction="column",
                width="10%",
            ),
        ),
        background_color=Color.BACKGROUND1.value,
        color=Color.TEXTCOLOR.value,
        style=styles.footer_heading_style,
        width="100%",
        height="20vh",
    )