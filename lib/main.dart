import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: SemaforoUberApp()));

class SemaforoUberApp extends StatefulWidget {
  @override
  _SemaforoUberAppState createState() => _SemaforoUberAppState();
}

class _SemaforoUberAppState extends State<SemaforoUberApp> {
  String textoSemaforo = "🚦 MONITORANDO UBER\n\nAguardando nova corrida...";
  Color corFundo = Colors.black87;

  void calcularLucroReal() {
    setState(() {
      textoSemaforo = "🟢 CORRIDA APROVADA!\n\nLucro Líquido: R\$ 6,20 limpo!\nGanho por KM: R\$ 2,10 por KM!\nNota: 4.98";
      corFundo = Color(0xFF1E5631); // Verde padrão Gigu
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: corFundo,
      appBar: AppBar(title: Text("Semaforo Uber Oficial"), backgroundColor: Colors.transparent),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(textoSemaforo, style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Colors.white), textAlign: TextAlign.center),
              SizedBox(height: 40),
              ElevatedButton(
                onPressed: calcularLucroReal,
                child: Text("CALCULAR MEU LUCRO", style: TextStyle(fontSize: 18)),
                style: ElevatedButton.styleFrom(backgroundColor: Colors.green, padding: EdgeInsets.all(16)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
