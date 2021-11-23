import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# Clave: benchmark, isa, cpu, eje x, eje y
# Valor: dirección de la imagen
Images = {
    '11111': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '11112': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '11113': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '11114': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '11115': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '11116': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '11121': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '11122': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '11123': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '11124': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '11125': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '11126': 'imagenes/458.sjeng-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '11211': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '11212': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '11213': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '11214': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '11215': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '11216': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '11221': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '11222': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '11223': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '11224': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '11225': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '11226': 'imagenes/458.sjeng-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '12111': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '12112': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '12113': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '12114': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '12115': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '12116': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '12121': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '12122': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '12123': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '12124': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '12125': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '12126': 'imagenes/458.sjeng-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '12211': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '12212': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '12213': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '12214': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '12215': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '12216': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '12221': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '12222': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '12223': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '12224': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '12225': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '12226': 'imagenes/458.sjeng-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '21111': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '21112': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '21113': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '21114': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '21115': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '21116': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '21121': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '21122': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '21123': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '21124': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '21125': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '21126': 'imagenes/blackscholes-ARM-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '21211': 'imagenes/blackscholes-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '21212': 'imagenes/blackscholes-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '21213': 'imagenes/blackscholes-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '21214': 'imagenes/blackscholes-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '21215': 'imagenes/blackscholes-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '21216': 'imagenes/blackscholes-ARM-TimingSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '21221': 'imagenes/blackscholes-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '21222': 'imagenes/blackscholes-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '21223': 'imagenes/blackscholes-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '21224': 'imagenes/blackscholes-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '21225': 'imagenes/blackscholes-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '21226': 'imagenes/blackscholes-ARM-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '22111': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '22112': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '22113': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '22114': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '22115': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '22116': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '22121': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '22122': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '22123': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '22124': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '22125': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '22126': 'imagenes/blackscholes-RISCV-AtomicSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '22211': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1d.png',
    '22212': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Hits l1i.png',
    '22213': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1d.png',
    '22214': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Miss Rate l1i.png',
    '22215': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Misses l1d.png',
    '22216': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-cacheline_size/Tamano de linea - Numero de Ciclo.png',

    '22221': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1d.png',
    '22222': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Hits l1i.png',
    '22223': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1d.png',
    '22224': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Miss Rate l1i.png',
    '22225': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Misses l1d.png',
    '22226': 'imagenes/blackscholes-RISCV-TimingSimpleCPU-l1d_size/Tamano de la cache l1d - Numero de Ciclo.png',

    '11131': 'imagenes/branchpredictors-458.sjeng-ARM-AtomicSimpleCPU/Branch Predictor - Hits l1d.png',
    '11136': 'imagenes/branchpredictors-458.sjeng-ARM-AtomicSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '11137': 'imagenes/branchpredictors-458.sjeng-ARM-AtomicSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '11138': 'imagenes/branchpredictors-458.sjeng-ARM-AtomicSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png',

    '11231': 'imagenes/branchpredictors-458.sjeng-ARM-TimingSimpleCPU/Branch Predictor - Hits l1d.png',
    '11236': 'imagenes/branchpredictors-458.sjeng-ARM-TimingSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '11237': 'imagenes/branchpredictors-458.sjeng-ARM-TimingSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '11238': 'imagenes/branchpredictors-458.sjeng-ARM-TimingSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png',

    '12131': 'imagenes/branchpredictors-458.sjeng-RISCV-AtomicSimpleCPU/Branch Predictor - Hits l1d.png',
    '12136': 'imagenes/branchpredictors-458.sjeng-RISCV-AtomicSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '12137': 'imagenes/branchpredictors-458.sjeng-RISCV-AtomicSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '12138': 'imagenes/branchpredictors-458.sjeng-RISCV-AtomicSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png',

    '12231': 'imagenes/branchpredictors-458.sjeng-RISCV-TimingSimpleCPU/Branch Predictor - Hits l1d.png',
    '12236': 'imagenes/branchpredictors-458.sjeng-RISCV-TimingSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '12237': 'imagenes/branchpredictors-458.sjeng-RISCV-TimingSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '12238': 'imagenes/branchpredictors-458.sjeng-RISCV-TimingSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png',

    '21131': 'imagenes/branchpredictors-blackscholes-ARM-AtomicSimpleCPU/Branch Predictor - Hits l1d.png',
    '21136': 'imagenes/branchpredictors-blackscholes-ARM-AtomicSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '21137': 'imagenes/branchpredictors-blackscholes-ARM-AtomicSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '21138': 'imagenes/branchpredictors-blackscholes-ARM-AtomicSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png',

    '21231': 'imagenes/branchpredictors-blackscholes-ARM-TimingSimpleCPU/Branch Predictor - Hits l1d.png',
    '21236': 'imagenes/branchpredictors-blackscholes-ARM-TimingSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '21237': 'imagenes/branchpredictors-blackscholes-ARM-TimingSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '21238': 'imagenes/branchpredictors-blackscholes-ARM-TimingSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png',

    '22131': 'imagenes/branchpredictors-blackscholes-RISCV-AtomicSimpleCPU/Branch Predictor - Hits l1d.png',
    '22136': 'imagenes/branchpredictors-blackscholes-RISCV-AtomicSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '22137': 'imagenes/branchpredictors-blackscholes-RISCV-AtomicSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '22138': 'imagenes/branchpredictors-blackscholes-RISCV-AtomicSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png',

    '22231': 'imagenes/branchpredictors-blackscholes-RISCV-TimingSimpleCPU/Branch Predictor - Hits l1d.png',
    '22236': 'imagenes/branchpredictors-blackscholes-RISCV-TimingSimpleCPU/Branch Predictor - Numero de Ciclos.png',
    '22237': 'imagenes/branchpredictors-blackscholes-RISCV-TimingSimpleCPU/Branch Predictor - Porcentaje de Hits BTB.png',
    '22238': 'imagenes/branchpredictors-blackscholes-RISCV-TimingSimpleCPU/Branch Predictor - Porcentaje de Misses BTB.png'
    }

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Gráficas de rendimiento')
        self.geometry('640x400')
        self.resizable(width=False, height=False)

        # label
        self.label = Label(self, text='Gráficas de rendimiento:')
        self.label.place(x=20, y=10)

        # Benchmark
        self.label_benchmark = Label(self, text='Seleccione el Benchmark')
        self.label_benchmark.place(x=20, y=50)

        self.var_benchmark = IntVar()
        self.var_benchmark.set(1)
        
        self.benchmark_1 = Radiobutton(self, text="458.sjeng", variable=self.var_benchmark, value=1, state=NORMAL)
        self.benchmark_1.place(x=20, y=70)

        self.benchmark_2 = Radiobutton(self, text="Blackscholes", variable=self.var_benchmark, value=2)
        self.benchmark_2.place(x=20, y=100)

        # ISA
        self.label_isa = Label(self, text='Seleccione el ISA')
        self.label_isa.place(x=250, y=50)
        
        self.var_isa = IntVar()
        self.var_isa.set(1)
                
        self.isa_1 = Radiobutton(self, text="ARM", variable=self.var_isa, value=1)
        self.isa_1.place(x=250, y=70)

        self.isa_2 = Radiobutton(self, text="RISC-V", variable=self.var_isa, value=2)
        self.isa_2.place(x=250, y=100)

        # CPU
        self.label_cpu = Label(self, text='Seleccione el CPU')
        self.label_cpu.place(x=480, y=50)

        self.var_cpu = IntVar()
        self.var_cpu.set(1)
        
        self.cpu_1 = Radiobutton(self, text="AtomicSimpleCPU", variable=self.var_cpu, value=1)
        self.cpu_1.place(x=480, y=70)

        self.cpu_2 = Radiobutton(self, text="TimingSimpleCPU", variable=self.var_cpu, value=2)
        self.cpu_2.place(x=480, y=100)

        # Parametro a variar
        self.label_parametro_variar = Label(self, text='Seleccione el parámetro a variar')
        self.label_parametro_variar.place(x=20, y=140)

        self.var_parametro_variar = IntVar()
        self.var_parametro_variar.set(1)
        
        self.parametro_variar_1 = Radiobutton(self, text="Cache line", variable=self.var_parametro_variar, value=1,
                                              command=self.disabled_radiobutton)
        self.parametro_variar_1.place(x=20, y=160)

        self.parametro_variar_2 = Radiobutton(self, text="l1d size", variable=self.var_parametro_variar, value=2,
                                              command=self.disabled_radiobutton)
        self.parametro_variar_2.place(x=250, y=160)

        self.parametro_variar_3 = Radiobutton(self, text="Branch Predictor", variable=self.var_parametro_variar, value=3,
                                              command=self.disabled_radiobutton)
        self.parametro_variar_3.place(x=480, y=160)

        # Parametro de salida
        self.label_parametro_salida = Label(self, text='Seleccione el parámetro de salida')
        self.label_parametro_salida.place(x=20, y=200)

        self.var_parametro_salida = IntVar()
        self.var_parametro_salida.set(1)
                
        self.parametro_salida_1 = Radiobutton(self, text="Hits l1d", variable=self.var_parametro_salida, value=1)
        self.parametro_salida_1.place(x=20, y=220)

        self.parametro_salida_2 = Radiobutton(self, text="Hits l1i", variable=self.var_parametro_salida, value=2)
        self.parametro_salida_2.place(x=250, y=220)

        self.parametro_salida_3 = Radiobutton(self, text="Missrate l1d", variable=self.var_parametro_salida, value=3)
        self.parametro_salida_3.place(x=480, y=220)
        
        self.parametro_salida_4 = Radiobutton(self, text="Miss Rate l1i", variable=self.var_parametro_salida, value=4)
        self.parametro_salida_4.place(x=20, y=250)

        self.parametro_salida_5 = Radiobutton(self, text="Misses l1d", variable=self.var_parametro_salida, value=5)
        self.parametro_salida_5.place(x=250, y=250)

        self.parametro_salida_6 = Radiobutton(self, text="Numero de ciclos", variable=self.var_parametro_salida, value=6)
        self.parametro_salida_6.place(x=480, y=250)

        self.parametro_salida_7 = Radiobutton(self, text="% hits btb", variable=self.var_parametro_salida, value=7, state=DISABLED)
        self.parametro_salida_7.place(x=20, y=280)

        self.parametro_salida_8 = Radiobutton(self, text="% misses btb", variable=self.var_parametro_salida, value=8, state=DISABLED)
        self.parametro_salida_8.place(x=250, y=280)

        # button
        self.button = Button(self, text='Generar gráfica')
        self.button['command'] = self.generar_grafica
        self.button.place(x=250, y=340)

    def disabled_radiobutton(self):
       self.selection = self.var_parametro_variar.get()
       if (self.selection == 1 or self.selection == 2):
           self.parametro_salida_2.configure(state = NORMAL)
           self.parametro_salida_3.configure(state = NORMAL)
           self.parametro_salida_4.configure(state = NORMAL)
           self.parametro_salida_5.configure(state = NORMAL)
           self.parametro_salida_7.configure(state = DISABLED)
           self.parametro_salida_8.configure(state = DISABLED)
       else:
           self.parametro_salida_2.configure(state = DISABLED)
           self.parametro_salida_3.configure(state = DISABLED)
           self.parametro_salida_4.configure(state = DISABLED)
           self.parametro_salida_5.configure(state = DISABLED)
           self.parametro_salida_7.configure(state = NORMAL)
           self.parametro_salida_8.configure(state = NORMAL)

    def generar_grafica(self):

        self.seleccion = ( str(self.var_benchmark.get()) + str(self.var_isa.get()) + str(self.var_cpu.get()) 
                             + str(self.var_parametro_variar.get()) + str(self.var_parametro_salida.get()) )
        
        # Nueva ventana para mostrar imagen
        window = Window(self, self.seleccion)
        window.grab_set()
        
# Ventana para mostrar imagen
class Window(tk.Toplevel):
    def __init__(self, parent, seleccion):
        super().__init__(parent)

        self.geometry('640x480')
        self.title('Gráfica')

        # Open images
        self.img = Image.open(Images[seleccion])
        self.img = self.img.resize((640, 480), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.panel = Label(self, image=self.img)
        self.panel.image = self.img
        self.panel.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
