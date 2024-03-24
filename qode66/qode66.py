from rxconfig import config
from qode66.pages.home import home
from qode66.pages.about import about
from qode66.pages.portfolio import portfolio

import reflex as rx
import qode66.styles.styles as styles


class State(rx.State):
    """The app state."""

@rx.page(
    title="Qode66",
)

def index() -> rx.Component:
    return rx.container(
        home(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(index)
app.add_page(about)
app.add_page(portfolio)