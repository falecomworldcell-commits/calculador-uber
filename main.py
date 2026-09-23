from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class CalculadorUberApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label_status = Label(
            text="🚦 SEMÁFORO UBER\n\nAbra o aplicativo da Uber\ne clique no botão abaixo para testar.", 
            font_size='22sp',
            halign='center',
            markup=True
        )
        
        self.btn_verificar = Button(
            text="VERIFICAR CORRIDA", 
            font_size='20sp',
            background_color=get_color_from_hex('#00FF00'),
            size_hint=(1, 0.3)
        )
        self.btn_verificar.bind(on_press=self.simular_leitura)
        
        self.layout.add_widget(self.label_status)
        self.layout.add_widget(self.btn_verificar)
        return self.layout

    def simular_leitura(self, instance):
        self.layout.clear_widgets()
        resultado_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        lbl_resultado = Label(
            text="🟢 CORRIDA APROVADA!\n\n[b]Valor:[/b] R$ 8,08\n[b]Nota do Passageiro:[/b] 4.98\n\n[b]Lucro Líquido Real:[/b] R$ 6,20\n🔥 Ganhando R$ 2,10 por KM!",
            font_size='24sp',
            halign='center',
            markup=True
        )
        
        btn_voltar = Button(
            text="VOLTAR AO MONITOR",
            font_size='18sp',
            size_hint=(1, 0.2)
        )
        btn_voltar.bind(on_press=self.voltar_tela)
        
        resultado_layout.add_widget(lbl_resultado)
        resultado_layout.add_widget(btn_voltar)
        self.layout.add_widget(resultado_layout)

    def voltar_tela(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.label_status)
        self.layout.add_widget(self.btn_verificar)

if __name__ == "__main__":
    CalculadorUberApp().run()
