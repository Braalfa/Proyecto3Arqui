import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

rutaLocal = "/home/brayan/Documents/GEM5/gem5/parsec-2.1/pkgs/apps/blackscholes"

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

def runSimulation(cacheline_size, l2_assoc,l1i_assoc, l1d_assoc, l2_size, l1i_size, l1d_size, cpu, isa, branchpredictor, benchmark):
    global rutaLocal
    rutaLocal = "/home/brayan/Documents/Proyecto3/blackscholes"
    ruta = " " + rutaLocal+"/src/blackscholes -o "+rutaLocal+"/inputs/input_test/in_4.txt "
    lineaMakeFile = 60
    compileCmd = "CXX"
    compileC = "++"
    if benchmark != "blackscholes":
        rutaLocal = "/home/brayan/Documents/Proyecto3/fluidanimate"
        ruta = " " + rutaLocal+"/src/fluidanimate -o " + rutaLocal+"/inputs/input_test/in_5K.fluid"
        lineaMakeFile = 4
        compileCmd = "CC"
        compileC = "cc"

    with open(rutaLocal+'/src/Makefile', 'r') as file:
        data = file.readlines()
    if isa == "ARM":
        data[lineaMakeFile] = compileCmd+" = arm-linux-gnueabi-g"+compileC+" -static\n"
    else:
        data[lineaMakeFile] = compileCmd+" = riscv32-unknown-elf-g"+compileC+"\n"    
    with open(rutaLocal+'/src/Makefile', 'w') as file:
        file.writelines( data )

    command  = "cd " + rutaLocal + "/src && make"
    out = subprocess.run(command, shell=True)
    print(out)
    lineaMakeFile = 60


    command  = "time ~/Documents/GEM5/gem5/build/"+isa+"-"+branchpredictor+"/gem5.opt -d "+rutaLocal+"/m5out/ ~/Documents/GEM5/gem5/configs/example/se.py  -c "+ ruta +" --caches --l2cache  --cpu-type="+cpu+"  --l1d_size="+l1d_size+" --l1i_size="+l1i_size+" --l2_size="+l2_size+" --l1d_assoc="+l1d_assoc+" --l1i_assoc="+l1i_assoc+" --l2_assoc="+l2_assoc+" --cacheline_size="+cacheline_size
    out = subprocess.run(command, shell=True)
    print(out)
        
def iterate(cpu, isa, benchmark, variable = "", variableLabel="", cacheline_size = ["64"], l1d_size = ["32kB"]):
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
            runSimulation(cacheline_size_aux, l2_assoc,l1i_assoc, l1d_assoc, l2_size, l1i_size, l1d_size_aux, cpu, isa, branchpredictor, benchmark)
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



iterate("TimingSimpleCPU", "ARM", "adfasd", variable = "l1d_size", 
         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
         l1d_size = ["128kB", "16kB", "32kB", "64kB", "128kB"])

# iterate("TimingSimpleCPU", "ARM", variable = "l1d_size", 
#         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
#         l1d_size = ["8kB", "16kB", "32kB", "64kB", "128kB"])

# iterate("AtomicSimpleCPU", "RISCV", variable = "l1d_size", 
#         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
#         l1d_size = [str(2**x)+"B" for x in range(7,15)])

# iterate("TimingSimpleCPU", "RISCV", variable = "l1d_size", 
#         variableLabel="Tamano de la cache l1d", cacheline_size = ["64"], 
#         l1d_size = ["1kB", "2kB", "4kB", "8kB", "16kB"])


isas = ["ARM", "RISCV"]
cpus = ["AtomicSimpleCPU", "TimingSimpleCPU"]
branchpredictors = ["TournamentBP", "BiModeBP", "LocalBP"]

# for cpu in cpus:
#     for isa in isas:
        ############------------------------------###################
        # Branch Predictors
        # cacheline_size = "64"
        # l2_assoc = "1"
        # l1i_assoc = "1"
        # l1d_assoc = "2"
        # l2_size = "1MB"
        # l1i_size = "128kB"
        # l1d_size = "32kB"

        # data = {"cacheline_size":[], "l1d_size":[], "cpu":[], "isa": [], "branchp": [], 
        # "benchmark":[],"BTBMissPct":[],"BTBHitRatio":[],"numCycles":[],
        #  "branchMispredRatio":[]}

        # for branchpredictor_aux in branchpredictors:
        #     runSimulation(cacheline_size, l2_assoc,l1i_assoc, l1d_assoc, l2_size, l1i_size, l1d_size, cpu, isa, branchpredictor_aux, benchmark)
        #     data["cacheline_size"].append(cacheline_size)
        #     data["l1d_size"].append(l1d_size)
        #     data["cpu"].append(cpu)
        #     data["isa"].append(isa)
        #     data["branchp"].append(branchpredictor_aux)
        #     data["benchmark"].append(benchmark)
        #     data["BTBMissPct"].append(obtain("system.cpu.branchPred.BTBMissPct"))
        #     data["BTBHitRatio"].append(obtain("system.cpu.branchPred.BTBHitRatio"))
        #     data["branchMispredRatio"].append(obtain("branchMispredRatio"))
        #     data["numCycles"].append(obtain("system.cpu.numCycles"))
        
        # df = pd.DataFrame(data)
        # xcolumns = ["branchp"]
        # xlabes = ["Branch Predictor"]

        # ycolumns = ["numCycles","BTBMissPct","BTBHitRatio","branchMispredRatio"]
        # ylabes = ["Numero de Ciclos", "Porcentaje de Misses BTB", "Porcentaje de Hits BTB","Hits l1d","Razon de fallo de Prediccion"]

        # folder = isa+"-"+cpu+"-branchpredictors"

        # command  = "mkdir " + folder
        # out = subprocess.run(command, shell=True)
        # print(out)


        # df.to_csv(folder+"/data.csv")
        # generateDiscrete(df, xcolumns, xlabes, ycolumns, ylabes, folder)