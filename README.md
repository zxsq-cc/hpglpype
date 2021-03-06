# hpglpype

[`vpype`](https://github.com/abey79/vpype) plug-in to export to HPGL


## Examples

```$ vpype -read /path/to/file.svg hpgl /path/to/output/file.hpgl```


## Installation

See the [vpype installation instructions](https://github.com/abey79/vpype/blob/master/INSTALL.md) for information on how
to install `vpype`first, then continue below.


### Existing `vpype` installation

Use this method if you have an existing `vpype` installation (typically in an existing virtual environment) and you
want to make this plug-in available. You must activate your virtual environment (if applicable) beforehand.

```bash
$ pip install git+https://github.com/zxsq-cc/hpglpype.git#egg=hpglpype
```

Check that your install is successful:

```
$ vpype --help
Usage: vpype [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -v, --verbose
  -I, --include PATH  Load commands from a command file.
  --help              Show this message and exit.

Commands:
[...]
  Plugins:
    hpgl
[...]
```

### Stand-alone installation

Use this method if you need to edit this project. First, clone the project:

```bash
$ git clone https://github.com/zxsq-cc/hpglpype.git
$ cd hpglpype
```

Create a virtual environment (optional):

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
```

Install `hpglpype` and its dependencies (including `vpype`):

```bash
$ pip install -e .
```

Check that your install is successful:

```
$ vpype --help
Usage: vpype [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -v, --verbose
  -I, --include PATH  Load commands from a command file.
  --help              Show this message and exit.

Commands:
[...]
  Plugins:
    hpgl
[...]
```


## Documentation

[WIP] The complete plug-in documentation is available directly in the CLI help:

```bash
$ vpype hpgl --help
```


## License

See the [LICENSE](LICENSE) file for details.
