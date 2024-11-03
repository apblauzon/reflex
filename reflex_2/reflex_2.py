import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index():
    return rx.text("Root Page")


def about():
    return rx.text("About Page")


def custom():
    return rx.text("Custom Route")


app = rx.App()

app.add_page(index)
app.add_page(about)
app.add_page(custom, route="/custom-route")
