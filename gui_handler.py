from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from answer_handler import answer_evaluation
# from file_handler import log_it


class AiFace(Widget):
    label_text = StringProperty("Welcome!")

    def send_answer(self):
        text = answer_evaluation(self.ids["text_input_1"].text)
        self.label_text = text


class AiGuiApp(App):
    def build(self):
        self.title = "Santi AI v1"
        return AiFace()


def start_gui():
    AiGuiApp().run()


if __name__ == "__main__":
    start_gui()
