from function import *
from tkinter import *
from turtle import *
from tkinter import messagebox


def uz():
    global dop
    r = float(radius.get())
    n = int(kolvo.get())
    x1n = 0
    y1n = 0
    x2n = int(dlina.get())
    y2n = int(shirina.get())
    m = [42, 51, 60, 41, 42]
    s = set()
    k = 0
    sl = {}
    dop = []
    for i in range(n):
        for j in range(n):
            sl[f'''i = {i + 1}, j = {j + 1}'''] = results(r, x1n + x2n * j, y1n + y2n * i, x2n + x2n * j, y2n + y2n * i)
    reset()
    hideturtle()
    pensize(1)
    tracer(0, 0)
    up()
    goto(-300, -100)
    down()
    setup(1000, 1000)
    bgcolor("light grey")
    title("Узлы связи")
    for elem in sl:
        fillcolor('light grey')
        begin_fill()
        for el in m:
            goto(sl[f'{elem}'][el - 1][1] * 70 - 300, sl[f'{elem}'][el - 1][2] * 70 - 150)
            down()
        end_fill()
        up()
        goto(sl[f'{elem}'][52][1] * 70 - 300, sl[f'{elem}'][52][2] * 70 - 150)
        down()
        color("black")
        for i in range(16):
            circle(r*70, 360 / 16)
            if i % 2 == 0:
                xy = (xcor(), ycor())
                dop.append(xy)
        up()
        goto(sl[f'{elem}'][46][1] * 70 - 300, sl[f'{elem}'][46][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][2][1] * 70 - 300, sl[f'{elem}'][2][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][4][1] * 70 - 300, sl[f'{elem}'][4][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][64][1] * 70 - 300, sl[f'{elem}'][64][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][50][1] * 70 - 300, sl[f'{elem}'][50][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][40][1] * 70 - 300, sl[f'{elem}'][40][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][55][1] * 70 - 300, sl[f'{elem}'][55][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][24][1] * 70 - 300, sl[f'{elem}'][24][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][6][1] * 70 - 300, sl[f'{elem}'][6][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][44][1] * 70 - 300, sl[f'{elem}'][44][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][59][1] * 70 - 300, sl[f'{elem}'][59][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][41][1] * 70 - 300, sl[f'{elem}'][41][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][1][1] * 70 - 300, sl[f'{elem}'][1][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][4][1] * 70 - 300, sl[f'{elem}'][4][2] * 70 - 150)
        goto(sl[f'{elem}'][3][1] * 70 - 300, sl[f'{elem}'][3][2] * 70 - 150)
        goto(sl[f'{elem}'][2][1] * 70 - 300, sl[f'{elem}'][2][2] * 70 - 150)
        goto(sl[f'{elem}'][1][1] * 70 - 300, sl[f'{elem}'][1][2] * 70 - 150)
        up()

    up()
    m1 = []
    for elem in sl:
        for i in range(len(sl[f'{elem}'])):
            if (sl[f'{elem}'][i][1] * 70 - 300, sl[f'{elem}'][i][2] * 70 - 150) not in s:
                goto(sl[f'{elem}'][i][1] * 70 - 300, sl[f'{elem}'][i][2] * 70 - 150)
                dot(5, "black")
                write(k)
                k += 1
                s.add((sl[f'{elem}'][i][1] * 70 - 300, sl[f'{elem}'][i][2] * 70 - 150))
                m1.append((sl[f'{elem}'][i][1], sl[f'{elem}'][i][2]))

    up()
    global dop_uzel
    dop_uzel = []

    for elem in dop:
        goto(elem[0], elem[1])
        dot(5, "red")
        dop_uzel.append(((elem[0] + 300) / 70, (elem[1] + 150) / 70))

    hideturtle()


def rebro():
    r = float(radius.get())
    n = int(kolvo.get())
    x1n = 0
    y1n = 0
    x2n = int(dlina.get())
    y2n = int(shirina.get())
    m = [42, 51, 60, 41, 42]
    sl = {}
    rb = {}
    dop = []
    reset()
    hideturtle()
    tracer(0, 0)
    pensize(2)
    up()
    goto(-300, -100)
    down()
    setup(1000, 1000)
    bgcolor("light grey")
    title("Нумерация ребер")
    for i in range(n):
        for j in range(n):
            sl[f'''i = {i + 1}, j = {j + 1}'''] = results(r, x1n + x2n * j, y1n + y2n * i, x2n + x2n * j, y2n + y2n * i)
            rb[f'''i = {i + 1}, j = {j + 1}'''] = edge_index(sl[f'''i = {i + 1}, j = {j + 1}'''])
    for elem in sl:
        fillcolor('light grey')
        begin_fill()
        for el in m:
            goto(sl[f'{elem}'][el - 1][1] * 70 - 300, sl[f'{elem}'][el - 1][2] * 70 - 150)
            down()
        end_fill()
        up()
        goto(sl[f'{elem}'][52][1] * 70 - 300, sl[f'{elem}'][52][2] * 70 - 150)
        down()
        for i in range(16):
            circle(r * 70, 360 / 16)
            if i % 2 == 0:
                xy = (xcor(), ycor())
                dop.append(xy)
        up()
        goto(sl[f'{elem}'][46][1] * 70 - 300, sl[f'{elem}'][46][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][2][1] * 70 - 300, sl[f'{elem}'][2][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][4][1] * 70 - 300, sl[f'{elem}'][4][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][64][1] * 70 - 300, sl[f'{elem}'][64][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][50][1] * 70 - 300, sl[f'{elem}'][50][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][40][1] * 70 - 300, sl[f'{elem}'][40][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][55][1] * 70 - 300, sl[f'{elem}'][55][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][24][1] * 70 - 300, sl[f'{elem}'][24][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][6][1] * 70 - 300, sl[f'{elem}'][6][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][44][1] * 70 - 300, sl[f'{elem}'][44][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][59][1] * 70 - 300, sl[f'{elem}'][59][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][41][1] * 70 - 300, sl[f'{elem}'][41][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][1][1] * 70 - 300, sl[f'{elem}'][1][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][4][1] * 70 - 300, sl[f'{elem}'][4][2] * 70 - 150)
        goto(sl[f'{elem}'][3][1] * 70 - 300, sl[f'{elem}'][3][2] * 70 - 150)
        goto(sl[f'{elem}'][2][1] * 70 - 300, sl[f'{elem}'][2][2] * 70 - 150)
        goto(sl[f'{elem}'][1][1] * 70 - 300, sl[f'{elem}'][1][2] * 70 - 150)
        up()
    up()

    global dop_uzel
    dop_uzel = []

    for elem in dop:
        goto(elem[0], elem[1])
        dot(5, "red")
        dop_uzel.append(((elem[0]+300)/70, (elem[1]+150)/70))

    up()
    s = set()
    reb = -1
    flag = {}
    for elem in rb:
        for i in range(len(rb[f'{elem}'])):
            for j in range(len(rb[f'{elem}'][i])):
                if ((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1])/2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2])/2) not in s:
                    reb += 1
                    rb[f'{elem}'][i][j].append(f'{reb} ребро')
                    s.add(((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1])/2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2])/2))
                    goto(((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1])/2) * 70 - 300, ((rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2])/2) * 70 - 150)
                    color('black')
                    write(reb, font=("Arial", 7, "bold"))
                    flag[((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1])/2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2])/2)] = reb
                else:
                    v = flag[((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1])/2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2])/2)]
                    rb[f'{elem}'][i][j].append(f'{v} ребро')

    hideturtle()
    exitonclick()


def elem():
    index = 1
    r = float(radius.get())
    n = int(kolvo.get())
    x1n = 0
    y1n = 0
    x2n = int(dlina.get())
    y2n = int(shirina.get())
    m = [42, 51, 60, 41, 42]
    sl = {}
    rb = {}
    dop = []
    reset()
    hideturtle()
    tracer(0, 0)
    pensize(2)
    up()
    goto(-300, -100)
    down()
    setup(1000, 1000)
    bgcolor("light grey")
    title("Нумерация конечных элементов")
    for i in range(n):
        for j in range(n):
            sl[f'''i = {i + 1}, j = {j + 1}'''] = results(r, x1n + x2n * j, y1n + y2n * i, x2n + x2n * j, y2n + y2n * i)
            rb[f'''i = {i + 1}, j = {j + 1}'''] = edge_index(sl[f'''i = {i + 1}, j = {j + 1}'''])
    for elem in sl:
        fillcolor('light grey')
        begin_fill()
        for el in m:
            goto(sl[f'{elem}'][el - 1][1] * 70 - 300, sl[f'{elem}'][el - 1][2] * 70 - 150)
            down()
        end_fill()
        up()
        goto(sl[f'{elem}'][52][1] * 70 - 300, sl[f'{elem}'][52][2] * 70 - 150)
        down()
        for i in range(16):
            circle(r * 70, 360 / 16)
            if i % 2 == 0:
                xy = (xcor(), ycor())
                dop.append(xy)
        up()
        goto(sl[f'{elem}'][46][1] * 70 - 300, sl[f'{elem}'][46][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][2][1] * 70 - 300, sl[f'{elem}'][2][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][4][1] * 70 - 300, sl[f'{elem}'][4][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][64][1] * 70 - 300, sl[f'{elem}'][64][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][50][1] * 70 - 300, sl[f'{elem}'][50][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][40][1] * 70 - 300, sl[f'{elem}'][40][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][55][1] * 70 - 300, sl[f'{elem}'][55][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][24][1] * 70 - 300, sl[f'{elem}'][24][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][6][1] * 70 - 300, sl[f'{elem}'][6][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][44][1] * 70 - 300, sl[f'{elem}'][44][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][59][1] * 70 - 300, sl[f'{elem}'][59][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][41][1] * 70 - 300, sl[f'{elem}'][41][2] * 70 - 150)
        up()
        goto(sl[f'{elem}'][1][1] * 70 - 300, sl[f'{elem}'][1][2] * 70 - 150)
        down()
        goto(sl[f'{elem}'][4][1] * 70 - 300, sl[f'{elem}'][4][2] * 70 - 150)
        goto(sl[f'{elem}'][3][1] * 70 - 300, sl[f'{elem}'][3][2] * 70 - 150)
        goto(sl[f'{elem}'][2][1] * 70 - 300, sl[f'{elem}'][2][2] * 70 - 150)
        goto(sl[f'{elem}'][1][1] * 70 - 300, sl[f'{elem}'][1][2] * 70 - 150)

        up()

        elem_index = [[0, 4], [0, 3], [0, 2], [0, 1],
                      [7, 5], [12, 10], [13, 15],
                      [17, 19], [22, 25], [26, 28],
                      [32, 30], [34, 36], [40, 38], [43, 41],
                      [45, 47], [52, 50], [54, 56],
                      [57, 59], [61, 63], [66, 68]]


        color('black')
        for el in elem_index:
            x = ((sl[f'{elem}'][el[0]][1] + sl[f'{elem}'][el[1]][1])/2) * 70 - 300
            y = ((sl[f'{elem}'][el[0]][2] + sl[f'{elem}'][el[1]][2])/2) * 70 - 150
            goto(x, y)
            write(index, align='center', font=("Arial", 7, "bold"))
            index += 1
    up()

    global dop_uzel
    dop_uzel = []

    for elem in dop:
        goto(elem[0], elem[1])
        dot(5, "red")
        dop_uzel.append(((elem[0] + 300) / 70, (elem[1] + 150) / 70))


    hideturtle()
    exitonclick()
    bye()


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        root.destroy()


def data_for_stifness_matrix():
    r = float(radius.get())
    n = int(kolvo.get())
    x1n = 0
    y1n = 0
    x2n = int(dlina.get())
    y2n = int(shirina.get())
    numb = int(number.get())
    sl = {}
    rb = {}
    for i in range(n):
        for j in range(n):
            sl[f'''i = {i + 1}, j = {j + 1}'''] = results(r, x1n + x2n * j, y1n + y2n * i, x2n + x2n * j, y2n + y2n * i)
            rb[f'''i = {i + 1}, j = {j + 1}'''] = edge_index(sl[f'''i = {i + 1}, j = {j + 1}'''])

    s = set()
    reb = -1
    flag = {}
    for elem in rb:
        for i in range(len(rb[f'{elem}'])):
            for j in range(len(rb[f'{elem}'][i])):
                if ((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1]) / 2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2]) / 2) not in s:
                    reb += 1
                    rb[f'{elem}'][i][j].append(f'{reb} ребро')
                    s.add(((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1]) / 2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2]) / 2))
                    flag[((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1]) / 2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2]) / 2)] = reb
                else:
                    v = flag[((rb[f'{elem}'][i][j][0][1] + rb[f'{elem}'][i][j][1][1]) / 2, (rb[f'{elem}'][i][j][0][2] + rb[f'{elem}'][i][j][1][2]) / 2)]
                    rb[f'{elem}'][i][j].append(f'{v} ребро')
            rb[f'{elem}'][i].append((rb[f'{elem}'][0][0][0][1], rb[f'{elem}'][0][0][0][2]))

    res = []

    finit_elem = []

    for element in rb:
        for i in range(len(rb[f'{element}'])):
            finit_elem.append(rb[f'{element}'][i])

    data = finit_elem[numb-1]

    edges = ''
    uzel = []
    flag = False
    du = 0
    for i in range(4):
        if data[i][2] != 0:
            flag = True
            du = minlen(data[i][2], dop_uzel)
        edges += ' ' + data[i][3]
        x = data[i][0][1]
        y = data[i][0][2]
        uzel.append((x, y))

    flag2 = False
    for elem in uzel:
        l = sqrt((data[-1][0] - elem[0]) * (data[-1][0] - elem[0]) + (data[-1][1] - elem[1]) * (data[-1][1] - elem[1]))
        if l > r:
            flag2 = True

    res.append(flag)
    res.append(edges)
    res.append(uzel)
    res.append(numb)
    res.append(du)
    res.append(flag2)
    return res


def minlen(el, dop):
    res = 0
    min = 10000
    for elem in dop:
        l = sqrt((el[0]-elem[0])*(el[0]-elem[0]) + (el[1]-elem[1])*(el[1]-elem[1]))
        if l < min:
            min = l
            res = elem

    return res


def new_window():
    res = data_for_stifness_matrix()
    flag = res[0]
    edges = res[1]
    du = res[4]
    new_window = Toplevel(root)
    new_window.geometry('600x500')
    new_window.title("Данные конечного элемента")
    frame = Frame(new_window, padx=10, pady=10)
    frame.pack(expand=True)

    num = Label(frame, text=f"Номер элемента: {res[3]}")
    num.grid(row=0, column=1)

    edges = Label(frame, text=f"Ребра в составе элемента - {edges} ")
    edges.grid(row=1, column=1)

    krivrebro = Label(frame, text=f"Наличие криволинейного ребра - {flag} ")
    krivrebro.grid(row=2, column=1)

    uzel1 = Label(frame, text=f"Узел 1 : {res[2][0]}")
    uzel1.grid(row=3, column=1)

    uzel2 = Label(frame, text=f"Узел 2: {res[2][1]}")
    uzel2.grid(row=4, column=1)

    uzel3 = Label(frame, text=f"Узел 3: {res[2][2]}")
    uzel3.grid(row=5, column=1)

    uzel4 = Label(frame, text=f"Узел 4: {res[2][3]}")
    uzel4.grid(row=6, column=1)

    if flag:
        uzel5 = Label(frame, text=f"Дополнительный узел 5 {du}")
        uzel5.grid(row=7, column=1)


def new_window2():
    res = data_for_stifness_matrix()
    du = res[4]
    flag = res[5]
    x = [res[2][0][0], res[2][1][0], res[2][2][0], res[2][3][0], du[0]]
    y = [res[2][0][1], res[2][1][1], res[2][2][1], res[2][3][1], du[1]]
    new_window2 = Toplevel(root)
    new_window2.geometry('600x500')
    new_window2.title("Локальная матрица элемента")
    frame = Frame(new_window2, padx=5, pady=5)
    frame.pack(expand=True)
    local = local_stiffness_matrix(x, y, flag)

    for i in range(len(local)):
        for j in range(len(local[i])):
            element = Label(frame, text=f"{local[i][j]}")
            element.grid(row=i, column=j)





root = Tk()
root.title('Формирование матриц жесткости')
root.protocol("WM_DELETE_WINDOW", on_closing)

mainmenu = Menu(root)
root.config(menu=mainmenu)
root.geometry('600x500')

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

kolvo = Label(frame, text="Размерность")
kolvo.grid(row=1, column=1)
kolvo = Entry(frame)
kolvo.grid(row=1, column=2)

radius = Label(frame, text="Радиус")
radius.grid(row=2, column=1)
radius = Entry(frame)
radius.grid(row=2, column=2)

dlina = Label(frame, text="Длина")
dlina.grid(row=3, column=1)
dlina = Entry(frame)
dlina.grid(row=3, column=2)

shirina = Label(frame, text="Ширина")
shirina.grid(row=4, column=1)
shirina = Entry(frame)
shirina.grid(row=4, column=2)

cal_btn = Button(frame, text='Вывести координаты узлов связи', command=uz)
cal_btn.grid(row=7, column=2)
cal_btn2 = Button(frame, text='Вывести нумерацию рёбер', command=rebro)
cal_btn2.grid(row=8, column=2)
cal_btn2 = Button(frame, text='Вывести нумерацию конечных элементов', command=elem)
cal_btn2.grid(row=9, column=2)

number = Label(frame, text="Введите номер конечного элемента")
number.grid(row=12, column=1)
number = Entry(frame)
number.grid(row=12, column=2)
cal_btn = Button(frame, text='Вывести данные этого конечного элемента', command=new_window)
cal_btn.grid(row=13, column=2)
cal_btn = Button(frame, text='Рассчитать локальную матрицу этого конечного элемента', command=new_window2)
cal_btn.grid(row=14, column=2)


root.mainloop()
