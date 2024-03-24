import reflex as rx

from qode66.components.navbar import navbar
from qode66.components.home_body import home_body
from qode66.components.footer import footer


def home() -> rx.Component:
    return rx.container(
        navbar(),
        home_body(),
        footer(),
    )