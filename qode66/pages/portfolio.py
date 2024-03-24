import reflex as rx

from qode66.components.navbar import navbar
from qode66.components.portfolio_body import portfolio_body
from qode66.components.footer import footer

@rx.page(title="Portfolio")
def portfolio() -> rx.Component:
    return rx.container(
        navbar(),
        portfolio_body(),
        footer(),
    )