import reflex as rx

from qode66.components.navbar import navbar
from qode66.components.about_body import about_body
from qode66.components.footer import footer

@rx.page(title="Quant a")
def about() -> rx.Component:
    return rx.container(
        navbar(),
        about_body(),
        footer(),
    )