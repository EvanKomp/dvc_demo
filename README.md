# Demo of data version control DVC

## Install necessary deps:
```
pip install dvc
pip install numpy
pip install pyyaml
```

## Git tracked files

```
./pipeline/get_data.py                    # generates random numbers and creates a new file
./pipeline/process_data.py                # computes some parameter dependant statistics on the data, saves metrics
./environment.yml                         # conda environment
./params.yaml                             # specifies parameters for the pipeline
```

After running the DVC code, we will have the following:

```
./metrics/                                # contains output metrics
./dvc.yaml                                # defines pipeline
./dvc.lock                                # specifies current DVC state
```

## DVC tracked files

After running the DVC code, we will have the following:

```
./data/
./.dvc
```

## To run the pipeline and observe the new files

```
dvc init
dvc repro
git add dvc.lock
git commit -m "ran dvc"
```

execute `dvc repro` again... note that everything is skipped! no parameters or dependancies changed.

## To run an experiment with a new parameter, look at the result of all experiments

After the above has been executed...

```
dvc exp run -S 'process_data.test_size=0.5'
dvc exp show
```
