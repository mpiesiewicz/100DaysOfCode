import tkinter


def button1_command():
    input_value = entry1.get()
    output_value = f'{float(input_value) * 1.609344:.2f}'
    my_label3.config(text=output_value)


window = tkinter.Tk()
window.title('Mile to Km μConverter')
window.minsize(width=300, height=200)
window.config(padx=2, pady=2)

font = ('Arial', 10, 'normal')

entry1 = tkinter.Entry(width=5)
entry1.insert(index=0, string='0')
entry1.grid(column=1, row=0)

my_label = tkinter.Label(text='miles', font=font)
my_label.grid(column=2, row=0)

my_label2 = tkinter.Label(text='is equal to: ', font=font)
my_label2.grid(column=0, row=1)

my_label3 = tkinter.Label(text=0, font=font)
my_label3.grid(column=1, row=1)

my_label4 = tkinter.Label(text='km', font=font)
my_label4.grid(column=2, row=1)

button1 = tkinter.Button(text='Calculate', command=button1_command)
button1.grid(column=1, row=2)














window.mainloop()