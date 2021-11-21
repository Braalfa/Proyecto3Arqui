# -- Script gen ́erico para ejecuci ́on de GEM5 --
# -- Direcci ́on donde GEM5 fue constru ́ıdo --
export GEM5_DIR=~/Documents/GEM5/gem5 
export OPT=$GEM5_DIR/build/ARM-None/gem5.opt
export PY=$GEM5_DIR/configs/example/se.py 
export BENCHMARK=./src/blackscholes
export ARGUMENT=./inputs/input_test/in_4.txt
# -- Ejecuci ́on del ambiente --.
time $OPT -d m5out/ $PY  -c $BENCHMARK -o $ARGUMENT