from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class DiagnosticApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1) # အမည်းရောင် Background
        layout = BoxLayout(orientation='vertical', padding=30)
        
        # သင့် Tool ရဲ့ အချက်အလက်များကို ပြသမည့် Label
        result_text = (
            "[b][color=00ffff]Phone Hardware Diagnostic[/color][/b]\n\n"
            "Battery Health: [color=00ff00]GOOD[/color]\n"
            "Battery Level: 91%\n"
            "Internal Storage: 179G used\n"
            "Android Version: 15\n\n"
            "[color=00ff00]✓ Sensors are responding correctly.[/color]"
        )
        
        lbl = Label(text=result_text, markup=True, font_size='18sp', halign='center')
        layout.add_widget(lbl)
        return layout

if __name__ == '__main__':
    DiagnosticApp().run()
