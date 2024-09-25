# PyPI Mock for `uv` bug replication


# Steps
Ensure you have `uv` installed and python 3.9.* available. The numpy_html.py file contains a copy of the numpy HTML index page with the `data-requires-python` attribute removed from the `numpy` package.

From the ./pypi-mock directory:

```shell
uv python pin python3.9
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python app.py
```

Then, from a new terminal:


```shell
source .venv/bin/activate
uv add numpy
```
#### Fails
`uv` attempts to build from source

---

```shell
source .venv/bin/activate
uv pip install numpy
```
#### Fails
`uv` attempts to build from source

---

```shell
source .venv/bin/activate
uv add numpy --no-build-package numpy
```
#### Fails
`uv` will fail to find a compatible wheel for python3.9 and error out

---

```shell
source .venv/bin/activate
uv pip install numpy --only-binary=:all:
```
#### Succeeds
`uv` will find and install the latest compatible wheel for python3.9 (`numpy@2.0.2`)
