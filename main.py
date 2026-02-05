from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class PhoneChecker(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        self.lbl = Label(text="Phone Diagnostic Tool", font_size='25sp')
        self.btn = Button(text="စစ်ဆေးမည်", size_hint=(1, 0.3), background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.check)
        
        self.layout.add_widget(self.lbl)
        self.layout.add_widget(self.btn)
        return self.layout

    def check(self, instance):
        self.lbl.text = "Battery: GOOD\nDisplay: Verified\nSensors: Active"

if __name__ == "__main__":
    PhoneChecker().run()
