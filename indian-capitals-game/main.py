import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Guess capitals game")
image = "ezgif-3-587b0dcd23.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("capital_names.csv")
all_capitals = data.capital.to_list()
guessed_capital = []

while len(guessed_capital) < 30:

    answer_capital = screen.textinput(title= f"{len(guessed_capital)}/30 capitals correct", prompt="What's the capital name??").title()
    if answer_capital == "Exit":
        missing_capitals = []
        for capital in all_capitals:
            if capital not in guessed_capital:
                missing_capitals.append(capital)
        new_data = pd.DataFrame(missing_capitals)
        new_data.to_csv("capitals_to_learn.csv")

        break
    if answer_capital in all_capitals:
        guessed_capital.append(answer_capital)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        capital_data = data[data.capital == answer_capital]
        t.goto(int(capital_data.x), int(capital_data.y))
        t.write(answer_capital)

# #getting coordinates to create csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)




#turtle.mainloop()
