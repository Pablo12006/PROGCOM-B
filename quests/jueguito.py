import tkinter as tk
import random
import time
from tkinter import Canvas

class JuegoMatematico:
    def __init__(self, root):
        self.root = root
        self.root.title("🌈 Sumo y Resto: Aventura Matemática 🎨")
        self.root.geometry("420x550")
        self.root.configure(bg="#FFD700")
        self.vidas = 3
        self.nivel = 1
        self.puntos = 0
        self.inicio_tiempo = None
        self.operador = None
        
        self.label_info = tk.Label(root, text="🌟 ¡Elige una aventura matemática! 🌟", font=("Comic Sans MS", 16, "bold"), bg="#FFD700", fg="#00008B")
        self.label_info.pack(pady=10)
        
        self.boton_suma = tk.Button(root, text="🎈 Sumas", command=lambda: self.iniciar_juego('+'), font=("Comic Sans MS", 16, "bold"), bg="#FF4500", fg="white", width=10, height=2)
        self.boton_suma.pack(pady=5)
        
        self.boton_resta = tk.Button(root, text="🎈 Restas", command=lambda: self.iniciar_juego('-'), font=("Comic Sans MS", 16, "bold"), bg="#32CD32", fg="white", width=10, height=2)
        self.boton_resta.pack(pady=5)
        
        self.label_muñeco = tk.Label(root, text="😀😀😀", font=("Comic Sans MS", 30), bg="#FFD700")
        self.label_muñeco.pack(pady=10)
    
    def actualizar_muñeco(self):
        muñeco_estado = ["💀", "😟", "😊", "😀😀😀"]
        self.label_muñeco.config(text=muñeco_estado[self.vidas])
    
    def iniciar_juego(self, operador):
        self.operador = operador
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.label_info = tk.Label(self.root, text=f"🌟 ¡Resuelve las {self.operador} preguntas! 🌟", font=("Comic Sans MS", 16, "bold"), bg="#FFD700", fg="#00008B")
        self.label_info.pack(pady=10)
        
        self.label_estado = tk.Label(self.root, text="", font=("Comic Sans MS", 14), bg="#FFD700", fg="#444")
        self.label_estado.pack()
        
        self.label_muñeco = tk.Label(self.root, text="😀😀😀", font=("Comic Sans MS", 30), bg="#FFD700")
        self.label_muñeco.pack(pady=10)
        
        self.label_pregunta = tk.Label(self.root, text="", font=("Comic Sans MS", 20, "bold"), bg="#FFD700", fg="#0000CD")
        self.label_pregunta.pack(pady=10)
        
        self.entry_respuesta = tk.Entry(self.root, font=("Comic Sans MS", 18), justify="center", width=5)
        self.entry_respuesta.pack()
        
        self.boton_enviar = tk.Button(self.root, text="✅ Responder", command=self.verificar_respuesta, font=("Comic Sans MS", 16, "bold"), bg="#4CAF50", fg="white", width=12, height=2)
        self.boton_enviar.pack(pady=10)
        
        self.canvas = Canvas(self.root, width=420, height=100, bg="#FFD700", highlightthickness=0)
        self.canvas.pack()
        
        self.nueva_pregunta()
    
    def generar_pregunta(self):
        a = random.randint(1, 10 * self.nivel)
        b = random.randint(1, 10 * self.nivel)
        if self.operador == '-':
            a, b = max(a, b), min(a, b)
        resultado = eval(f"{a} {self.operador} {b}")
        return f"{a} {self.operador} {b} = ?", resultado
    
    def nueva_pregunta(self):
        self.pregunta_actual, self.respuesta_correcta = self.generar_pregunta()
        self.label_pregunta.config(text=self.pregunta_actual)
        self.label_estado.config(text=f"🎯 Nivel {self.nivel} | ⭐ Puntos: {self.puntos} | ❤️ Vidas: {self.vidas}")
        self.entry_respuesta.delete(0, tk.END)
        self.inicio_tiempo = time.time()
    
    def mostrar_confeti(self):
        self.canvas.delete("all")
        for _ in range(30):
            x = random.randint(10, 400)
            y = random.randint(10, 100)
            color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
            self.canvas.create_oval(x, y, x+10, y+10, fill=color, outline=color)
        self.root.after(1000, self.canvas.delete, "all")
    
    def verificar_respuesta(self):
        try:
            respuesta_usuario = int(self.entry_respuesta.get())
        except ValueError:
            self.vidas -= 1
            self.actualizar_muñeco()
            self.label_estado.config(text=f"⚠️ Respuesta inválida. ❤️ Vidas restantes: {self.vidas}")
            if self.vidas == 0:
                self.fin_del_juego()
            return
        
        if respuesta_usuario == self.respuesta_correcta:
            self.puntos += 2
            self.mostrar_confeti()
            if self.puntos % 5 == 0:
                self.nivel += 1
                self.label_estado.config(text=f"🎉 ¡Subiste al nivel {self.nivel}! Ahora es más difícil.")
            else:
                self.label_estado.config(text=f"✅ Correcto. ⭐ Puntos: {self.puntos}")
            self.nueva_pregunta()
        else:
            self.vidas -= 1
            self.actualizar_muñeco()
            self.label_estado.config(text=f"❌ Incorrecto. La respuesta era {self.respuesta_correcta}. ❤️ Vidas restantes: {self.vidas}")
            if self.vidas == 0:
                self.fin_del_juego()
                return
            self.nueva_pregunta()
    
    def fin_del_juego(self):
        self.label_pregunta.config(text="💀 Fin del juego")
        self.boton_enviar.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = JuegoMatematico(root)
    root.mainloop()

if __name__ == "__main__":
    main()











