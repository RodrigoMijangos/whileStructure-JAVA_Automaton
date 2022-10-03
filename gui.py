import PySimpleGUI as gui
import automaton as aut


def init_gui():
    file = open("instructions.txt")

    content = ""

    for line in file:
        content += line

    container_code = gui.Multiline(content, size=(50, 10))
    file.close()
    main_label = gui.Text("Analizador de estructuras WHILE")
    btn_initializer = gui.OK()
    btn_evaluator = gui.Button("Analizar")
    btn_appOut = gui.Button("Salir")

    layout = [
        [main_label],
        [container_code],
        [btn_initializer, btn_evaluator, btn_appOut]
    ]

    app = gui.Window("App", layout, size=(400, 300))

    while True:

        event, values = app.read()

        if event == "OK":
            file = open("instructions.txt", "w")
            file.write(container_code.get())
            file.close()

        if event == "Analizar":
            chain_t_eval = container_code.get()
            if aut.automaton(chain=chain_t_eval):
                gui.popup("Correcto")
            else:
                gui.popup("Incorrecto")

            # if while_automaton("INI", chain_t_eval, 0, chain_t_eval[0]):
            #     gui.popup('Correcto')
            # else:
            #     gui.popup("Incorrecto")
        if event == gui.WIN_CLOSED or event == "Salir":
            app.close()
            break

