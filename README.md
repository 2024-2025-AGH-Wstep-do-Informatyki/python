# python

This project consists of multiple modules:

- `firewall-manager` - manages firewall/iptable rules
- `log-reader` - reads logs from files and journal
- `log-processor` - processes logs and marks suspicious events

### Prerequisites for running the app

`Python 3.13` is required for this app to work. You can download it from
[python.org](https://www.python.org/downloads/). We also encourage you to
install [uv](https://github.com/astral-sh/uv) which is an alternatives for
[pip](https://pypi.org/project/pip/).

### Prerequisites for development

Everything above and also install [ruff](https://github.com/astral-sh/ruff)
which is an alternative for `black`/`flake8` (code formatters).

### Installing/developing the app

To install all dependencies run

```sh
uv venv
uv pip install .
```

Then to run a given module run

```sh
python -m <module>
```

Where `<module>` can be `firewall-manager`, `log-reader`, `log-processor`.

## Authors

* Paweł Pasternak

* Nikodem Marek

See also the list of [contributors](https://github.com/2024-2025-AGH-Wstep-do-Informatyki/python/contributors)
who participated in this project.

## License

This project is licensed under the Unlicense License - see the
[LICENSE](LICENSE) file for details.

## Acknowledgments

* This project is inspired by [fail2ban](https://github.com/fail2ban/fail2ban).
