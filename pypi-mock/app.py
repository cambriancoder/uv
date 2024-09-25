from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from numpy_html import numpy_html

app = FastAPI()


@app.get("/simple/{package_name}/", response_class=HTMLResponse)
def get_package_info_html(package_name: str):
    if package_name == "numpy":
        return numpy_html

    # Redirect to the real PyPI
    raise HTTPException(status_code=302, detail="Redirecting to PyPI", headers={"Location": f"https://pypi.org/simple/{package_name}/"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
