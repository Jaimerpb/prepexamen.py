def count_mondays(birthday, current_date):
    # Calcular el número de días entre las dos fechas
    days = (current_date - birthday).days
  
    # Dividir el número de días entre 7 y redondear hacia abajo para obtener el número de semanas
    weeks = days // 7
  
    # Calcular el número de lunes sumando el número de semanas y el número de lunes entre las dos fechas
    mondays = weeks + (1 if birthday.weekday() <= current_date.weekday() and current_date.weekday() <= 4 else 0)
  
    return mondays

from datetime import date

def bad_monday_count(birthday, current_date):
    # Calcular la edad de la persona en la fecha actual
    age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
  
    # Verificar si la persona está en edad de trabajar
    if 22 <= age <= 78:
    # Calcular el número de lunes entre la fecha de cumpleaños y la fecha actual
        mondays = count_mondays(birthday, current_date)
        return mondays
    else:
        return 0

print(bad_monday_count(date(2000, 9, 9), date(2022, 12, 19)))

if __name__ == "__main__":
  main()
