from tkinter import *


def setwindow(root_):
    root_.title('Конфигуратор дома')
    root_.resizable(False, False)
    w = 800
    h = 600
    ww = root_.winfo_screenwidth()
    wh = root_.winfo_screenheight()
    x = int(ww / 2 - w / 2)
    y = int(wh / 2 - h / 2)
    root_.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))


type_foundation = 0
material = 0
roof_type = 0
summa = 0
summa_foundation = 0
summa_material = 0
summa_roof = 0

root = Tk()
setwindow(root)

square_var = StringVar()
number_floors_var = StringVar()


def enter_entry(*args):
    entry_floors.focus()
    root.unbind('<Return>')
    root.bind('<Return>', enter_prv)
    if args:
        pass


def enter_prv(*args):
    label_prv.destroy()
    label_floors.destroy()
    label_square.destroy()
    entry_floors.destroy()
    entry_square.destroy()
    button_enter1.destroy()
    label_found.place(relx=0.5, rely=0.05, anchor='center')
    button_tape.place(relx=0.2, rely=0.5, anchor='center')
    button_pile.place(relx=0.5, rely=0.5, anchor='center')
    button_plate.place(relx=0.8, rely=0.5, anchor='center')
    root.unbind('<Return>')
    if args:
        pass


def enter_found(i):
    global type_foundation
    label_found.destroy()
    button_tape.destroy()
    button_pile.destroy()
    button_plate.destroy()
    type_foundation = i
    label_material.place(relx=0.5, rely=0.05, anchor='center')
    button_bar.place(relx=0.315, rely=0.43, anchor='center')
    button_brick.place(relx=0.45, rely=0.43, anchor='center')
    button_ceramic_block.place(relx=0.65, rely=0.43, anchor='center')
    button_carcass.place(relx=0.32, rely=0.55, anchor='center')
    button_aerated_concrete_block.place(relx=0.68, rely=0.55, anchor='center')


def enter_material(i):
    global material
    label_material.destroy()
    button_bar.destroy()
    button_aerated_concrete_block.destroy()
    button_ceramic_block.destroy()
    button_brick.destroy()
    button_carcass.destroy()
    material = i
    label_roof.place(relx=0.5, rely=0.05, anchor='center')
    button_sheet_material.place(relx=0.305, rely=0.43, anchor='center')
    button_ceramic_roof.place(relx=0.695, rely=0.43, anchor='center')
    button_flexible_roof.place(relx=0.5, rely=0.55, anchor='center')


def enter_roof(i):
    global roof_type
    roof_type = i
    root.destroy()


label_prv = Label(root, text='Конфигуратор дома', font='Tahoma 26')
label_prv.place(relx=0.5, rely=0.05, anchor='n')
label_square = Label(root, text='Площадь 1го этажа:', font='Tahoma 22')
label_floors = Label(root, text='Количество этажей:', font='Tahoma 22')
entry_square = Entry(root, font='Tahoma 22', width=10, textvariable=square_var)
entry_square.focus()
entry_floors = Entry(root, font='Tahoma 22', width=10, textvariable=number_floors_var)

button_enter1 = Button(root, text='Далее', font='Tahoma 22', command=enter_prv)
root.bind('<Return>', enter_entry)

label_square.place(relx=0.5, rely=0.5, anchor='se')
label_floors.place(relx=0.5, rely=0.5, anchor='ne')
entry_square.place(relx=0.5, rely=0.5, anchor='sw')
entry_floors.place(relx=0.5, rely=0.5, anchor='nw')
button_enter1.place(relx=0.95, rely=0.95, anchor='se')

label_found = Label(root, text='Фундамент', font='Tahoma 26')
button_tape = Button(root, text='Ленточный', width=11, font='Tahoma 22',
                     command=lambda: enter_found(1))
button_pile = Button(root, text='Свайный', width=11, font='Tahoma 22',
                     command=lambda: enter_found(2))
button_plate = Button(root, text='Плитный', width=11, font='Tahoma 22',
                      command=lambda: enter_found(3))

label_material = Label(root, text='Материал тела дома', font='Tahoma 26')
button_bar = Button(root, text='Брус', font='Tahoma 22',
                    command=lambda: enter_material(1))
button_aerated_concrete_block = Button(root, text='Газобетонный блок', font='Tahoma 22',
                                       command=lambda: enter_material(2))
button_ceramic_block = Button(root, text='Керамоблок', font='Tahoma 22',
                              command=lambda: enter_material(3))
button_brick = Button(root, text='Кирпич', font='Tahoma 22',
                      command=lambda: enter_material(4))
button_carcass = Button(root, text='Деревянный каркас', font='Tahoma 22',
                        command=lambda: enter_material(5))

label_roof = Label(root, text='Кровля', font='Tahoma 26')
button_sheet_material = Button(root, text='Листовые материалы', font='Tahoma 22',
                               command=lambda: enter_roof(1))
button_flexible_roof = Button(root, text='Гибкая кровля', font='Tahoma 22',
                              command=lambda: enter_roof(2))
button_ceramic_roof = Button(root, text='Штучные материалы', font='Tahoma 22',
                             command=lambda: enter_roof(3))

root.mainloop()

if number_floors_var.get() == '':
    number_floors = 0
else:
    number_floors = int(number_floors_var.get())
if square_var.get() == '':
    square = 0
else:
    square = int(square_var.get())


elements = square / 25

if type_foundation == 1:
    concrete_volume = elements * 5.2
    fittings = elements * 80
    summa_foundation = int(concrete_volume * 3000 + fittings * 50)
    summa += summa_foundation
elif type_foundation == 2:
    concrete_volume = elements * 5.2
    fittings = elements * 80
    number_piles = int(elements * 12)
    summa_foundation = int(concrete_volume * 3000 + number_piles * 2000 + fittings * 50)
    summa += summa_foundation
elif type_foundation == 3:
    concrete_volume = square * 0.3
    fittings = concrete_volume / 6.3 * 523
    summa_foundation = int(concrete_volume * 3000 + fittings * 50)
    summa += summa_foundation

if material == 1:
    bar = elements * 15 * number_floors
    summa_material = int(bar * 25000)
    summa += summa_material
elif material == 2:
    aerated_concrete_block = elements * 400 * number_floors
    summa_material = int(aerated_concrete_block * 3000)
    summa += summa_material
elif material == 3:
    ceramic_block = elements * 900 * number_floors
    summa_material = int(ceramic_block * 120)
    summa += summa_material
elif material == 4:
    brick = elements * 6000 * number_floors
    summa_material = int(brick * 19)
    summa += summa_material
elif material == 5:
    racks = elements * 53 * number_floors
    summa_racks = int(racks * 110)
    overlap = elements * 20 * number_floors
    summa_overlap = int(overlap * 1000)
    summa_material = summa_racks + summa_overlap
    summa += summa_material

if roof_type == 1:
    sheet_material = elements * 37
    summa_roof = int(sheet_material * 500)
    summa += summa_roof
elif roof_type == 2:
    flexible_roof = elements * 13
    summa_roof = int(flexible_roof * 500)
    summa += summa_roof
elif roof_type == 3:
    ceramic_roof = elements * 37
    summa_roof = int(ceramic_roof * 4000)
    summa += summa_roof

root = Tk()
setwindow(root)

label_sum_found = Label(root, text='Стоимость фундамента:', font='Tahoma 22')
label_sum_material = Label(root, text='Стоимость основного материала:', font='Tahoma 22')
label_sum_roof = Label(root, text='Стоимость кровли:', font='Tahoma 22')
label_sum = Label(root, text='Итоговая сумма:', font='Tahoma 22')
summa_foundation = str(summa_foundation)
summa_material = str(summa_material)
summa_roof = str(summa_roof)
summa = str(summa)
label_summa_foundation = Label(root, text=summa_foundation+' руб', font='Tahoma 22')
label_summa_material = Label(root, text=summa_material+' руб', font='Tahoma 22')
label_summa_roof = Label(root, text=summa_roof+' руб', font='Tahoma 22')
label_summa = Label(root, text=summa+' руб', font='Tahoma 22')
label_sum_found.place(relx=0.65, rely=0.25, anchor='ne')
label_sum_material.place(relx=0.65, rely=0.35, anchor='ne')
label_sum_roof.place(relx=0.65, rely=0.45, anchor='ne')
label_sum.place(relx=0.65, rely=0.55, anchor='ne')
label_summa_foundation.place(relx=0.65, rely=0.25, anchor='nw')
label_summa_material.place(relx=0.65, rely=0.35, anchor='nw')
label_summa_roof.place(relx=0.65, rely=0.45, anchor='nw')
label_summa.place(relx=0.65, rely=0.55, anchor='nw')

root.mainloop()
