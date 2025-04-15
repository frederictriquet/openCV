import mido
# mido.get_output_names() -> 'nanoKONTROL2 CTRL'
with mido.open_input('nanoKONTROL2 SLIDER/KNOB') as port:
    is_running = True
    while is_running:
        for msg in port.iter_pending():
            print(msg, type(msg))
            print(msg.control)
            print(msg.value)
            if msg.control == 42 and msg.value == 127:
                is_running = False

