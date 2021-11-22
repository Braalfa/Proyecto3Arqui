import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

localDirectory = '/home/brayan/Documents'
rutaLocal = localDirectory+"/GEM5/gem5/parsec-2.1/pkgs/apps/blackscholes"

def grepToNumber(grep):
    i = grep.find('                       #')-1
    j = 0
    number = ""
    while grep[i] != " ":
        number =  grep[i] + number
        i -= 1
        j += 1
    return float(number)

def obtain(what):
    out = subprocess.run("grep '"+ what +"' "+ rutaLocal+"/m5out/stats.txt", capture_output=True, shell=True)
    grep = str(out.stdout)
    return grepToNumber(grep)

def generateDiscrete(df, xcolumns, xlabes, ycolumns, ylabes, folder): 
    for i in range(0,len(xcolumns)):
        for j in range(0,len(ycolumns)):
            plt.clf()
            sns.catplot(x=xcolumns[i], y= ycolumns[j],
                        markers="^", linestyles="--",
                        kind="point", data=df[[xcolumns[i], ycolumns[j]]])
            plt.xlabel(xlabes[i])
            plt.ylabel(ylabes[j])

            plt.savefig(folder + '/' + xlabes[i] + " - " + ylabes[j] +'.png')


def generateImages(df, xcolumns, xlabes, ycolumns, ylabes, folder): 
    for i in range(0,len(xcolumns)):
        for j in range(0,len(ycolumns)):
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(df[xcolumns[i]],df[ycolumns[j]], '-o',color="red")

            ax.set_xlabel(xlabes[i])
            ax.set_ylabel(ylabes[j])

            #removing top and right borders
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)

            plt.savefig(folder + '/' + xlabes[i] + " - " + ylabes[j] +'.png')

def runSimulation(cacheline_size, l2_assoc,l1i_assoc, l1d_assoc, l2_size, l1i_size, l1d_size, cpu, isa, branchpredictor, benchmark, flops):
    global rutaLocal
    rutaLocal = localDirectory+"/Proyecto3/blackscholes"
    ruta = " " + rutaLocal+"/src/blackscholes -o "+rutaLocal+"/inputs/input_test/in_4.txt "
    lineaMakeFile = 60
    command = "CXX"
    compiler = "++"
    if benchmark != "blackscholes":
        rutaLocal = localDirectory+"/Proyecto3/458.sjeng"
        ruta = " " + rutaLocal+"/src/benchmark -o " + rutaLocal+"/data/test.txt"
        lineaMakeFile = 5
        command = "CC"
        compiler = "cc"

    with open(rutaLocal+'/src/Makefile', 'r') as file:
        data = file.readlines()
    if isa == "ARM":
        data[lineaMakeFile] = command + " = arm-linux-gnueabi-g" +compiler + " -static\n"
    else:
        data[lineaMakeFile] = command + " = riscv32-unknown-elf-g"+compiler+"\n"    
    with open(rutaLocal+'/src/Makefile', 'w') as file:
        file.writelines( data )

    command  = "cd " + rutaLocal + "/src && export RISCV="+localDirectory+"/isa/riscv && export PATH=$PATH:$RISCV/bin && make"
    out = subprocess.run(command, shell=True)
    print(out)
    lineaMakeFile = 60


    command  = "time "+localDirectory+"/GEM5/gem5/build/"+isa+"-"+branchpredictor+"/gem5.opt -d "+rutaLocal+"/m5out/ "+localDirectory+"/GEM5/gem5/configs/example/se.py  -c "+ ruta +" --caches --l2cache  --cpu-type="+cpu+"  --l1d_size="+l1d_size+" --l1i_size="+l1i_size+" --l2_size="+l2_size+" --l1d_assoc="+l1d_assoc+" --l1i_assoc="+l1i_assoc+" --l2_assoc="+l2_assoc+" --cacheline_size="+cacheline_size +" -I "+ flops
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print(out)
        
def iterate(cpu, isa, benchmark, flops, variable = "", variableLabel="", cacheline_size = ["64"], l1d_size = ["32kB"]):
    data = {"cacheline_size":[], "l1d_size":[], "cpu":[], "isa": [], "branchp": [], 
    "benchmark":[],"numCycles":[],
    "dcache.overallMissRate":[], "icache.overallMissRate":[], "dcache.overallHits":[],
    "icache.overallHits":[], "dcache.overallMisses":[]}

    l2_assoc = "1"
    l1i_assoc = "2"
    l1d_assoc = "2"
    l2_size = "1MB"
    l1i_size = "128kB"
    branchpredictor = "None"

    for l1d_size_aux in l1d_size:
        for cacheline_size_aux in cacheline_size:
            runSimulation(cacheline_size_aux, l2_assoc,l1i_assoc, l1d_assoc, l2_size, l1i_size, l1d_size_aux, cpu, isa, branchpredictor, benchmark, flops)
            data["cacheline_size"].append(cacheline_size_aux)
            data["l1d_size"].append(l1d_size_aux)
            data["cpu"].append(cpu)
            data["isa"].append(isa)
            data["branchp"].append(branchpredictor)
            data["benchmark"].append(benchmark)
            data["numCycles"].append(obtain("system.cpu.numCycles"))
            data["dcache.overallMisses"].append(obtain("system.cpu.dcache.overallMisses::total"))
            data["dcache.overallMissRate"].append(obtain("system.cpu.dcache.overallMissRate::total"))
            data["icache.overallMissRate"].append(obtain("system.cpu.icache.overallMissRate::total"))
            data["dcache.overallHits"].append(obtain("system.cpu.dcache.overallHits::total"))
            data["icache.overallHits"].append(obtain("system.cpu.icache.overallHits::total"))
    
    df = pd.DataFrame(data)
    xcolumns = [variable]
    xlabes = [variableLabel]

    ycolumns = ["numCycles","dcache.overallMisses","dcache.overallMissRate","icache.overallMissRate","dcache.overallHits","icache.overallHits"]
    ylabes = ["Numero de Ciclo", "Misses l1d", "Miss Rate l1d", "Miss Rate l1i","Hits l1d","Hits l1i"]


    folder = "../Resultados/"+benchmark+"-"+isa+"-"+cpu+"-"+variable

    command  = "mkdir " + folder
    out = subprocess.run(command, shell=True)
    print(out)


    df.to_csv(folder+"/data.csv")
    generateImages(df, xcolumns, xlabes, ycolumns, ylabes, folder)


# RISCV - TimingSimpleCPU - blackscholes - l1d_size
iterate("TimingSimpleCPU", "RISCV", "blackscholes", "10000000", variable = "l1d_size", 
         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
         l1d_size = [str(2**x)+"B" for x in range(7,14)])

# RISCV - TimingSimpleCPU - 458.sjeng - l1d_size
iterate("TimingSimpleCPU", "RISCV", "458.sjeng", "10000000", variable = "l1d_size", 
          variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
          l1d_size = [str(2**x)+"B" for x in range(7,14)])

# RISCV - TimingSimpleCPU - blackscholes - cacheline_size *Nota: en 11 se cae
iterate("TimingSimpleCPU", "RISCV", "blackscholes", "10000000", variable = "cacheline_size", 
          variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
          l1d_size = ["128kB"])

# RISCV - TimingSimpleCPU - 458.sjeng - cacheline_size
iterate("TimingSimpleCPU", "RISCV", "458.sjeng", "10000000", variable = "cacheline_size", 
           variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
           l1d_size = ["128kB"])




# RISCV - AtomicSimpleCPU - blackscholes - l1d_size
iterate("AtomicSimpleCPU", "RISCV", "blackscholes", "10000000", variable = "l1d_size", 
         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
         l1d_size = [str(2**x)+"B" for x in range(7,14)])

# RISCV - AtomicSimpleCPU - 458.sjeng - l1d_size
iterate("AtomicSimpleCPU", "RISCV", "458.sjeng", "10000000", variable = "l1d_size", 
          variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
          l1d_size = [str(2**x)+"B" for x in range(7,14)])

# RISCV - AtomicSimpleCPU - blackscholes - cacheline_size *Nota: en 11 se cae
iterate("AtomicSimpleCPU", "RISCV", "blackscholes", "10000000", variable = "cacheline_size", 
          variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
          l1d_size = ["128kB"])

# RISCV - AtomicSimpleCPU - 458.sjeng - cacheline_size
iterate("AtomicSimpleCPU", "RISCV", "458.sjeng", "10000000", variable = "cacheline_size", 
           variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
           l1d_size = ["128kB"])



# ARM - TimingSimpleCPU - blackscholes - l1d_size
iterate("TimingSimpleCPU", "ARM", "blackscholes", "100000000000", variable = "l1d_size", 
         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
         l1d_size = [str(2**x)+"B" for x in range(7,14)])

# ARM - TimingSimpleCPU - 458.sjeng - l1d_size
iterate("TimingSimpleCPU", "ARM", "458.sjeng", "10000000", variable = "l1d_size", 
          variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
          l1d_size = [str(2**x)+"B" for x in range(7,14)])

# ARM - TimingSimpleCPU - blackscholes - cacheline_size *Nota: en 11 se cae
iterate("TimingSimpleCPU", "ARM", "blackscholes", "100000000000", variable = "cacheline_size", 
          variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
          l1d_size = ["128kB"])

# ARM - TimingSimpleCPU - 458.sjeng - cacheline_size
iterate("TimingSimpleCPU", "ARM", "458.sjeng", "10000000", variable = "cacheline_size", 
           variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
           l1d_size = ["128kB"])


# ARM - AtomicSimpleCPU - blackscholes - l1d_size
iterate("AtomicSimpleCPU", "ARM", "blackscholes", "10000000", variable = "l1d_size", 
         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
         l1d_size = [str(2**x)+"B" for x in range(7,14)])

# ARM - AtomicSimpleCPU - 458.sjeng - l1d_size
iterate("AtomicSimpleCPU", "ARM", "458.sjeng", "10000000", variable = "l1d_size", 
          variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
          l1d_size = [str(2**x)+"B" for x in range(7,14)])

# ARM - AtomicSimpleCPU - blackscholes - cacheline_size *Nota: en 11 se cae
iterate("AtomicSimpleCPU", "ARM", "blackscholes", "10000000", variable = "cacheline_size", 
          variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
          l1d_size = ["128kB"])

# ARM - AtomicSimpleCPU - 458.sjeng - cacheline_size
iterate("AtomicSimpleCPU", "ARM", "458.sjeng", "10000000", variable = "cacheline_size", 
           variableLabel="Tamano de linea", cacheline_size = [str(2**x) for x in range(4,10)], 
           l1d_size = ["128kB"])



# Branch Predictor

cacheline_size = "64"
l2_assoc = "1"
l1i_assoc = "1"
l1d_assoc = "2"
l2_size = "1MB"
l1i_size = "128kB"
l1d_size = "32kB"
iteraciones = "10000000"

isas = ["ARM", "RISCV"]
cpus = ["AtomicSimpleCPU", "TimingSimpleCPU"]
branchpredictors = ["TournamentBP", "BiModeBP", "LocalBP"]
benchmarks = ['blackscholes', '458.sjeng']

for benchmark in benchmarks:
    for cpu in cpus:
        for isa in isas:
            #Branch Predictors
            data = {"cacheline_size":[], "l1d_size":[], "cpu":[], "isa": [], "branchp": [], 
            "benchmark":[],"BTBMissPct":[],"BTBHitRatio":[],"numCycles":[],
            "branchMispredRatio":[]}

            for branchpredictor in branchpredictors:
                runSimulation(cacheline_size, l2_assoc,l1i_assoc, l1d_assoc, l2_size, l1i_size, l1d_size, cpu, isa, branchpredictor, benchmark, iteraciones)
                data["cacheline_size"].append(cacheline_size)
                data["l1d_size"].append(l1d_size)
                data["cpu"].append(cpu)
                data["isa"].append(isa)
                data["branchp"].append(branchpredictor)
                data["benchmark"].append(benchmark)
                data["BTBMissPct"].append(obtain("system.cpu.branchPred.BTBMissPct"))
                data["BTBHitRatio"].append(obtain("system.cpu.branchPred.BTBHitRatio"))
                data["branchMispredRatio"].append(obtain("branchMispredRatio"))
                data["numCycles"].append(obtain("system.cpu.numCycles"))
            
            df = pd.DataFrame(data)
            xcolumns = ["branchp"]
            xlabes = ["Branch Predictor"]

            ycolumns = ["numCycles","BTBMissPct","BTBHitRatio","branchMispredRatio"]
            ylabes = ["Numero de Ciclos", "Porcentaje de Misses BTB", "Porcentaje de Hits BTB","Hits l1d","Razon de fallo de Prediccion"]

            folder = "../Resultados/branchpredictors-"+benchmark+"-"+isa+"-"+cpu

            command  = "mkdir " + folder
            out = subprocess.run(command, shell=True)
            print(out)


            df.to_csv(folder+"/data.csv")
            generateDiscrete(df, xcolumns, xlabes, ycolumns, ylabes, folder)