from reactpy import component, html, use_state
from rich.console import Console

console = Console()

def increment(e):
    console.print(e + 1)
    return e + 1

def decrement(e):
    console.print(e - 1)
    return e - 1

@component
def App():
    count, set_count = use_state(0)

    return html.h1(f'Count: {count}',
                    html.button(
                        {
                            "class_name": "btn btn-primary",
                            'on_click': lambda e: set_count(increment)
                        },
                        'Increment'
                        ),
                    html.button(
                        {
                            "class_name": "btn btn-primary",
                            'on_click': lambda e: set_count(decrement)
                        },
                        'Decrement'
                        )
                )
