
# Merge figures

`merge_figures` is a command line tool for merging figures.

## Dependency

- cv2
- numpy
- argparse

## Getting Started

```bash
git clone https://github.com/koido/merge_figures.git
cd merge_figures
./merge.py -h
```

Example code:

```bash
./_make_ex_figs.py
inputs=(`ls -1d ./example/input/*`)
output=./example/output/test
./merge.py -i ${inputs[@]} -o ${output}_3x3 -r 3 -c 3
./merge.py -i ${inputs[@]} -o ${output}_5x5 -r 5 -c 5
```

## Citation

None

## License

GNU GPL v3.
