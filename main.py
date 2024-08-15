import io
from parseics import parseics
from parseagendas import parseagendas
from getcurrentclass import getcurrentclass
from getcurrentagenda import getcurrentagenda
from testics import test_ics
import tkinter

with io.open("./CalExport.ics", "r", encoding="utf8") as ics_text:
    ics = ics_text.read()

with io.open("./DailyAgendas.txt", "r", encoding="utf8") as agendas_text:
    agendas = agendas_text.read()

    parsed_ics = parseics(test_ics)
    parsed_agendas = parseagendas(agendas)


def main(canvas):
    current_class = getcurrentclass(parsed_ics)

    canvas.delete("display_text")

    if current_class:
        current_agenda = getcurrentagenda(current_class, parsed_agendas)[0]

        canvas.create_text(
            870,
            100,
            font="Georgia 60 bold",
            text=f"{current_agenda["Date"]}",
            fill="white",
            tag="display_text",
        )

        canvas.create_text(
            870,
            250,
            font="Georgia 100 bold",
            text=f"{current_agenda["Class"]} {current_agenda["Period"]}",
            fill="white",
            tag="display_text",
        )

        counter = 400

        for x in current_agenda["Body"]:
            canvas.create_text(
                870,
                counter,
                font="Georgia 60",
                text=x,
                fill="white",
                justify="center",
                tag="display_text",
            )
            counter = counter + 90
    else:
        canvas.create_text(
            870,
            540,
            font="Georgia 150 bold",
            text="Crespi Media Arts",
            fill="white",
            tag="display_text",
        )


root = tkinter.Tk()
bg = tkinter.PhotoImage(file="./BTSNightBackground.png")
canvas = tkinter.Canvas(width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")


def schedule_function():
    main(canvas)
    root.after(60000, schedule_function)


schedule_function()
root.mainloop()
