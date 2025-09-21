import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading

API_KEY = "E39L6L27WNRNWC93NLUSK9WVM"
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# --------------------------
# Fetch Weather Function
# --------------------------
def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    progress.start()

    def get_data():
        try:
            url = f"{BASE_URL}{city}?unitGroup=metric&key={API_KEY}&contentType=json"
            response = requests.get(url)
            data = response.json()

            if "days" not in data:
                raise ValueError("Invalid response from API")

            today = data["days"][0]
            temp = today["temp"]
            humidity = today["humidity"]
            conditions = today["conditions"]

            result = (
                f"City: {data['resolvedAddress']}\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {conditions}"
            )

            result_label.config(text=result)

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            progress.stop()

    threading.Thread(target=get_data).start()

# --------------------------
# Main Window
# --------------------------
root = tk.Tk()
root.title("Weather App - Visual Crossing")
root.geometry("400x300")

style = ttk.Style()
style.theme_use("clam")

# Notebook Tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Tab 1: Current Weather
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Current Weather")

frame = ttk.Frame(tab1, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="Enter City:").pack(side="left", padx=5)
city_entry = ttk.Entry(frame, width=20)
city_entry.pack(side="left", padx=5)

search_btn = ttk.Button(frame, text="Get Weather", command=fetch_weather)
search_btn.pack(side="left", padx=5)

progress = ttk.Progressbar(tab1, mode="indeterminate")
progress.pack(fill="x", padx=10, pady=10)

result_label = ttk.Label(tab1, text="Weather info will appear here", font=("Arial", 12))
result_label.pack(pady=20)

# Tab 2: Forecast (future expansion)
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Forecast")
ttk.Label(tab2, text="Forecast feature coming soon...").pack(pady=20)

root.mainloop()
