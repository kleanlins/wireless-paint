import arcade

class MainCanvas(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
    
        arcade.set_background_color(arcade.color.WHITE)


    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        print("plotting")
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.draw_point(x, y, arcade.color.BLACK, 5)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()


def main():
    window = MainCanvas(800, 600)
    arcade.run()


if __name__ == "__main__":
    main()