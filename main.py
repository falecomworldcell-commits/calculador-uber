from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CalculadorUberApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label_status = Label(
            text="🚦 SEMÁFORO UBER\nSistema Ativado e Monitorando", 
            font_size='24sp',
            halign='center'
        )
        
        btn_verificar = Button(
            text="VERIFICAR CORRIDA", 
            font_size='20sp',
            background_color=(0, 1, 0, 1)
        )
        
        layout.add_widget(self.label_status)
        layout.add_widget(btn_verificar)
        return layout

if __name__ == "__main__":
    CalculadorUberApp().run()
