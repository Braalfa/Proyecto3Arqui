import subprocess

for branchpredictor in ["None", "TournamentBP", "BiModeBP", "LocalBP"]:
    with open('/home/brayan/Documents/GEM5/gem5/src/cpu/simple/BaseSimpleCPU.py', 'r') as file:
        data = file.readlines()
    if branchpredictor == "None":
        data[51] = "    branchPred = Param.BranchPredictor(NULL, 'No Branch Predictor')\n"    
    else: 
        data[51] = "    branchPred = Param.BranchPredictor("+branchpredictor+"(numThreads = Parent.numThreads), '"+branchpredictor+"')\n"
    with open('/home/brayan/Documents/GEM5/gem5/src/cpu/simple/BaseSimpleCPU.py', 'w') as file:
        file.writelines( data )

    command  = "cd /home/brayan/Documents/GEM5/gem5 && scons build/ARM/gem5.opt -j 9"
    out = subprocess.run(command, capture_output=True, shell=True)
    print(out)
    print("compiled arm")
    command  = "cp -r /home/brayan/Documents/GEM5/gem5/build/ARM /home/brayan/Documents/GEM5/gem5/build/ARM-"+branchpredictor
    out = subprocess.run(command, capture_output=True, shell=True)
    print("renamed arm")

    command  = "cd /home/brayan/Documents/GEM5/gem5 && scons build/RISCV/gem5.opt -j 9"
    out = subprocess.run(command, capture_output=True, shell=True)
    print(out)
    print("compiled riscv")
    command  = "cp -r /home/brayan/Documents/GEM5/gem5/build/RISCV /home/brayan/Documents/GEM5/gem5/build/RISCV-"+branchpredictor
    out = subprocess.run(command, capture_output=True, shell=True)
    print("renamed riscv")
