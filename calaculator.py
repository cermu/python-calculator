from tkinter import *
import parser


# global variable i
i = 0


class Calculator:

    def __init__(self, main_screen):
        # The Display Area
        self.display = Entry(main_screen, state="normal", readonlybackground="white")
        self.display.grid(row=1, columnspan=6, sticky=W + E)

        # The Buttons
        Button(main_screen, text="1", bg="#a4c2f2", fg="black", command=lambda: self.get_input(1)).grid(row=2, column=0, sticky=N + S + E + W)
        Button(main_screen, text="2", bg="#a4c2f2", fg="black", command=lambda: self.get_input(2)).grid(row=2, column=1, sticky=N + S + E + W)
        Button(main_screen, text="3", bg="#a4c2f2", fg="black", command=lambda: self.get_input(3)).grid(row=2, column=2, sticky=N + S + E + W)

        Button(main_screen, text="4", bg="#a4c2f2", fg="black", command=lambda: self.get_input(4)).grid(row=3, column=0, sticky=N + S + E + W)
        Button(main_screen, text="5", bg="#a4c2f2", fg="black", command=lambda: self.get_input(5)).grid(row=3, column=1, sticky=N + S + E + W)
        Button(main_screen, text="6", bg="#a4c2f2", fg="black", command=lambda: self.get_input(6)).grid(row=3, column=2, sticky=N + S + E + W)

        Button(main_screen, text="7", bg="#a4c2f2", fg="black", command=lambda: self.get_input(7)).grid(row=4, column=0, sticky=N + S + E + W)
        Button(main_screen, text="8", bg="#a4c2f2", fg="black", command=lambda: self.get_input(8)).grid(row=4, column=1, sticky=N + S + E + W)
        Button(main_screen, text="9", bg="#a4c2f2", fg="black", command=lambda: self.get_input(9)).grid(row=4, column=2, sticky=N + S + E + W)

        Button(main_screen, text="AC", bg="orange", fg="white", command=lambda: self.clear_all()).grid(row=5, column=0, sticky=N + S + E + W)
        Button(main_screen, text="0", bg="#a4c2f2", fg="black", command=lambda: self.get_input(0)).grid(row=5, column=1, sticky=N + S + E + W)
        Button(main_screen, text="Del", bg="red", fg="white", command=lambda: self.undo()).grid(row=5, column=2,  sticky=N + S + E + W)

        Button(main_screen, text="+", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("+")).grid(row=2, column=3, sticky=N + S + E + W)
        Button(main_screen, text="-", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("-")).grid(row=3, column=3, sticky=N + S + E + W)
        Button(main_screen, text="*", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("*")).grid(row=4, column=3, sticky=N + S + E + W)
        Button(main_screen, text="/", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("/")).grid(row=5, column=3, sticky=N + S + E + W)

        # Button(main_screen, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4, sticky=N + S + E + W)
        Button(main_screen, text="exp", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("**")).grid(row=2, column=4, sticky=N + S + E + W)
        Button(main_screen, text="%", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("%")).grid(row=3, column=4, sticky=N + S + E + W)
        Button(main_screen, text="(", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("(")).grid(row=4, column=4, sticky=N + S + E + W)
        Button(main_screen, text=".", bg="#a4c2f2", fg="black", command=lambda: self.get_operation(".")).grid(row=5, column=4, sticky=N + S + E + W)

        Button(main_screen, text="^2", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("**2")).grid(row=2, column=5, sticky=N + S + E + W)
        Button(main_screen, text="^3", bg="#a4c2f2", fg="black", command=lambda: self.get_operation("**3")).grid(row=3, column=5, sticky=N + S + E + W)
        Button(main_screen, text=")", bg="#a4c2f2", fg="black", command=lambda: self.get_operation(")")).grid(row=4, column=5, sticky=N + S + E + W)
        Button(main_screen, text="=", bg="green", fg="white", command=lambda: self.calculate()).grid(row=5, column=5, sticky=N + S + E + W)

    # Display user input
    def get_input(self, num):
        global i
        self.display.insert(i, num)
        # increment the value of i which is the index so as to allow appending of another value
        i += 1

    # Clear the input
    def clear_all(self):
        self.display.delete(0, END)

    # Delete input one at a time
    def undo(self):
        entire_string = self.display.get()
        string_length = len(entire_string)

        # confirm the string_length is not 0
        if string_length:
            new_string = entire_string[:-1]
            self.clear_all()
            self.display.insert(0, new_string)
        else:
            self.display.insert(0, "Empty")

    # Get operator
    def get_operation(self, operator):
        global i

        # get the length of the operator
        operator_len = len(operator)
        self.display.insert(i, operator)

        # increment i by the operator_len because some are 2
        i += operator_len

    # Perform calculations
    def calculate(self):
        entire_string = self.display.get()

        try:
            input_expression = parser.expr(entire_string).compile()
            results = eval(input_expression)
            self.clear_all()
            self.display.insert(0, results)
        except Exception:
            self.clear_all()
            self.display.insert(0, "Mathematical Error")


calculator_screen = Tk()
calculator_screen.title("Simple Calculator")

# Don't allow resizing in the x or y direction
calculator_screen.resizable(0, 0)

calculator_object = Calculator(calculator_screen)

calculator_screen.mainloop()
