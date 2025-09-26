from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Monza(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "^"]
        self.result = Label(
            text="0",
            font_size=48,
            size_hint=(1, 0.2),
            halign="right",
            valign="center"
        )
        self.result.bind(size=self.result.setter('text_size'))

        main_layout = BoxLayout(orientation="vertical", padding=12, spacing=12)
        main_layout.add_widget(self.result)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["(", ")", "=", "^"]
        ]

        button_grid = GridLayout(cols=4, spacing=10, size_hint=(1, 0.8))
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=28,
                    background_normal="",
                    background_color=(0.15, 0.15, 0.15, 1),
                    color=(1, 1, 1, 1),
                    bold=True
                )
                button.bind(on_press=self.on_button_press)
                button_grid.add_widget(button)

        main_layout.add_widget(button_grid)
        return main_layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = "0"
        elif button_text == "=":
            try:
                expression = current.replace("^", "**")
                self.result.text = str(eval(expression))
            except Exception:
                self.result.text = "Erreur"
        else:
            if current == "0":
                self.result.text = button_text
            else:
                self.result.text = current + button_text


if __name__ == "__main__":
    Monza().run()
