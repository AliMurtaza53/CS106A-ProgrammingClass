from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
time = 60
def tick():
    # You have to clear the canvas each time the clock updates
    # (otherwise it writes on top of the old time).  Since the
    # time is the only thing in the canvas, delete(ALL) works
    # perfectly (if it wasn't however, you can delete the id
    # that goes with the clock).
    canvas.delete(ALL)
    # I have to declare time as a global because I'm not using
    # a class (otherwise, I could do something like self.time -= 1)
    global time
    time -= 5
    # You can place the time wherever in the canvas
    # (I chose 10,10 for the example)
    canvas.create_text(10, 10, text=time)
    if time == 0:
        canvas.create_text(10, 10, text="ali is great")
    else:
        canvas.after(1000, tick)
canvas.after(1, tick)
root.mainloop()

if __name__ == "__main__":
    main()
