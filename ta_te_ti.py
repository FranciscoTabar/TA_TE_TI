import tkinter as tk
from tkinter import messagebox
import random

class JuegoTaTeTi:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ta Te Ti")
        self.ventana.configure(bg="lightblue")
        
        self.turno = 'X'
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]

        self.botones = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.botones[i][j] = tk.Button(self.ventana, text='', font=('normal', 20), width=5, height=2,
                                              command=lambda fila=i, columna=j: self.realizar_movimiento(fila, columna))
                self.botones[i][j].grid(row=i, column=j)

    def realizar_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = self.turno
            color = "red" if self.turno =="X" else "blue"
            self.botones[fila][columna].config(text=self.turno, state='disabled', fg=color)

            if self.verificar_ganador('X'):
                messagebox.showinfo("Fin del juego", "¡Has ganado!")
                self.ventana.quit()
            elif ' ' not in [casilla for fila in self.tablero for casilla in fila]:
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.ventana.quit()
            else:
                self.turno = 'O' if self.turno =="X" else "X"
                if self.turno =="O":
                    self.jugar_computadora()

    def verificar_ganador(self, jugador):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == jugador:
                return True
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] == jugador:
                return True

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador:
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador:
            return True

        return False

    def jugar_computadora(self):
        disponibles = [(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == ' ']
        if disponibles:
            fila, columna = random.choice(disponibles)
            self.tablero[fila][columna] = 'O'
            self.botones[fila][columna].config(text='O', state='disabled',fg="blue")

            if self.verificar_ganador('O'):
                messagebox.showinfo("Fin del juego", "¡Gano la COMPUTADORA!")
                self.ventana.quit()
            elif ' ' not in [casilla for fila in self.tablero for casilla in fila]:
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.ventana.quit()
            else:
                self.turno = 'X'

    def iniciar_juego(self):
        if random.choice([True, False]):
            self.jugar_computadora()   
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = JuegoTaTeTi()
    juego.iniciar_juego()