import arcade        

class Brush:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

        self.brush_color = {
            'r': arcade.color.RED,
            'g': arcade.color.GREEN,
            'b': arcade.color.BLUE
        }

    def draw(self):
        arcade.draw_point(self.x, self.y, self.brush_color[self.color], self.size)


class MainCanvas(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
    
        arcade.set_background_color(arcade.color.WHITE)

        # Dynamic data
        self.brush_size = 3

        # Drawing data
        self.drawing: Brush = []

        # Debug
        self.mouse_clicks = 0


    def on_draw(self):
        arcade.start_render()
        for point in self.drawing:
            point.draw()
            #arcade.draw_point(point[0], point[1], arcade.color.BLACK, self.brush_size)


    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
                self.mouse_clicks += 1
                print("reading mouse click", self.mouse_clicks) 
                #self.drawing.append((x, y))
                self.drawing.append(Brush(x, y, 'r', self.brush_size))


#    def on_mouse_press(self, x, y, button, modifiers):
#        if button == arcade.MOUSE_BUTTON_LEFT:
#            while(1):
#                #self.drawing.append(Brush(x, y, 'r', self.brush_size))
#                self.drawing.append((x, y))

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()

        if key == arcade.key.UP:
            self.brush_size += 2


def main():
    window = MainCanvas(800, 600)
    arcade.run()


if __name__ == "__main__":
    main()