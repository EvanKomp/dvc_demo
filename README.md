# Demo of data version control DVC

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
git commit -m "ran dvc"
git push
```