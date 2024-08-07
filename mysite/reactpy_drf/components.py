from reactpy import component, html, use_state

@component
def App():
    count, set_count = use_state(0)

    def increment():
        set_count(count + 1)

    def decrement():
        set_count(count - 1)

    return html.h1(f'Count: {count} {nombre}',
                   html.button('Increment', onclick=increment),
                   html.button('Decrement', onclick=decrement))
