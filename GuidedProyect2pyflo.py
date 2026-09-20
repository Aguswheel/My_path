print("-" * 80)
print("-" * 30 + "FINANCIAL VISUALIZER" + "-" * 30)
print("-" * 80)

salary = (input("Annual Salary:\n"))
housing = (input("Monthly Housing:\n"))
bills = (input("Monthly Bills:\n"))
food = (input("Weekly Food:\n"))
travel = (input("Annual Travel:\n"))

valid_salary = salary.replace(".", "", 1).isnumeric()
valid_housing = housing.replace(".", "", 1).isnumeric()
valid_bills = bills.replace(".", "", 1).isnumeric()
valid_food = food.replace(".", "", 1).isnumeric()
valid_travel = travel.replace(".", "", 1).isnumeric()

if valid_salary and valid_housing and valid_bills and valid_food and valid_travel:
    print("All inputs confirmed valid.")
    salary_float = float(salary)
    housing_float = float(housing)
    bills_float = float(bills)
    food_float = float(food)
    travel_float = float(travel)

    # Paso 3: Impuestos (Ya lo tenías perfecto)
    if salary_float <= 10000:
        tax = salary_float * 0.05
    elif salary_float <= 40000:
        tax = salary_float * 0.10
    elif salary_float <= 80000:
        tax = salary_float * 0.15
    else:
        tax = salary_float * 0.20
        
    print(round(tax, 2))

    # Paso 4: Cálculos de montos anuales
    # No hace falta IF acá, solo multiplicar para llevar todo a 1 año
    housing_ann = housing_float * 12
    bills_ann = bills_float * 12
    food_ann = food_float * 52
    travel_ann = travel_float
    tax_ann = tax
    
    # Calculamos lo que sobra (Extra)
    extra_ann = salary_float - (housing_ann + bills_ann + food_ann + travel_ann + tax_ann)

    # Paso 4.1: Calcular qué porcentaje del salario representa cada gasto
    percent_housing = (housing_ann / salary_float) * 100
    percent_bills = (bills_ann / salary_float) * 100
    percent_food = (food_ann / salary_float) * 100
    percent_travel = (travel_ann / salary_float) * 100
    percent_tax = (tax_ann / salary_float) * 100
    percent_extra = (extra_ann / salary_float) * 100

    # Ahora ya tenés los dólares y los porcentajes listos para el gráfico final.

    print("\n" + "-" * 30 + "VISUALIZACION" + "-" * 35)
    print(f"Vivienda | $ {housing_ann:10,.2f} | {percent_housing:6.1f} % | {'#' * int(max(0, percent_housing))}")
    print(f"Facturas | $ {bills_ann:10,.2f} | {percent_bills:6.1f} % | {'#' * int(max(0, percent_bills))}")
    print(f"Comida   | $ {food_ann:10,.2f} | {percent_food:6.1f} % | {'#' * int(max(0, percent_food))}")
    print(f"Viaje    | $ {travel_ann:10,.2f} | {percent_travel:6.1f} % | {'#' * int(max(0, percent_travel))}")
    print(f"Impuestos| $ {tax_ann:10,.2f} | {percent_tax:6.1f} % | {'#' * int(max(0, percent_tax))}")
    print(f"Extra    | $ {extra_ann:10,.2f} | {percent_extra:6.1f} % | {'#' * int(max(0, percent_extra))}")
    print("-" * 80)
else:
    print("Invalid input, please try again.")
    
