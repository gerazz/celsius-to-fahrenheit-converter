def celsius_to_fahrenheit(celsius):
    """Преобразование температуры из градусов Цельсия в градусы Фаренгейта."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    celsius = float(input("Введите температуру в градусах Цельсия:\n--> "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C это {fahrenheit}°F.")

if __name__ == "__main__":
    main()

