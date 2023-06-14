from tkinter import *
from random import randint
def print_cords(rec):
    x1, y1, = canvas.coords(rec)
    print("Rect coordinates: ", {x1}, {y1}, )
def move_up(event):
    global x2, y2,score
    if y2 > 70:
        canvas.move(rec, 0, -25)
        print_cords(rec)
        y2 -= 25
        score +=2
def move_down(event):
    global x2, y2,score
    if y2 < canvas_height - 70:
        canvas.move(rec, 0, +25)
        print_cords(rec)
        y2 += 25
        score +=2
def move_left(event):
    global x2, y2,score
    if x2 > 70:
        canvas.move(rec, -35, 0)
        print_cords(rec)
        x2 -= 35
        score +=2
def move_right(event):
    global x2, y2,score
    if x2 < canvas_width - 70:
        canvas.move(rec, 35, 0)
        print_cords(rec)
        x2 += 35
        score +=2
def attack():
    global enemy,begin,size
    for enemy in enemies:
        canvas.move(enemy, -5, 0)
        x1, y1, x2, y2 = canvas.coords(enemy)
        if (x1 <= 0 ):
            canvas.create_text(canvas_width / 2, 15, text="Shield Off GO! GO! GO!", fill="black", font=("Arial", 25))
            canvas.delete(begin)
            canvas.delete(enemy)
            enemies.remove(enemy)
            y = randint(0, 900)
            x = randint(1600,2000)
            size=randint(10,50)
            new_enemy = canvas.create_oval(x, y, x+size, y + size, fill='brown')
            enemies.append(new_enemy)
        elif canvas.find_overlapping(*canvas.bbox(rec)) == (rec,enemy):
            for enemy in enemies:
                canvas.delete(enemy)
            canvas.delete(rec)
            canvas.create_text(canvas_width / 2, canvas_height / 2, text="Game Over", fill="black", font=("Arial", 50))
            canvas.create_text(70, 15, text="Score: " + str(score), font=("Arial", 15), fill="black")
            return
    main.after(50, attack)

"""def get_mouse_click(event):
    print(event.x, event.y)"""

if __name__ == '__main__':
    main = Tk()
    canvas_width = main.winfo_screenwidth()
    # 1536
    canvas_height = main.winfo_screenheight()
    # 864
    canvas = Canvas(main, width=canvas_width, height=canvas_height)
    """canvas.bind("<Button-1>", get_mouse_click)"""
    canvas.pack()
    begin =canvas.create_text(canvas_width / 2, 30, text="Initiating test run with asteroid shield no damage will be taken until next run, Have it easy on your first go", fill="Cyan", font=("Arial", 25))
    enemies = []
    size = randint(10,50)
    for i in range(15):
        y = randint(0, 900)
        x = randint(1600, 2000)
        new_enemy = canvas.create_oval(x, y, x + size, y + size, fill='brown')
        enemies.append(new_enemy)
    x2 = 70
    count=1
    score=0
    y2 = canvas_height / 2
    retro = PhotoImage(file="retro.png")
    rec = canvas.create_image(70, canvas_height / 2, image=retro)
    main.bind("<w>", move_up)
    main.bind("<s>", move_down)
    main.bind("<a>", move_left)
    main.bind("<d>", move_right)
    attack()
    main.mainloop()