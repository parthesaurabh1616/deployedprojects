from fastapi import FastAPI
from app.convert import celsius_to_fahrenheit, fahrenheit_to_celsius

app = FastAPI()

@app.get("/c_to_f/")
def c_to_f(c: float):
    return {"fahrenheit": celsius_to_fahrenheit(c)}

@app.get("/f_to_c/")
def f_to_c(f: float):
    return {"celsius": fahrenheit_to_celsius(f)}
