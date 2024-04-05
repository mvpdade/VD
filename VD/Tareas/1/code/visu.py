import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo 2023 Car Dataset.csv
car_data = pd.read_csv("C:/Users/Dade/OneDrive - Universidad Técnica Federico Santa María/2024/2024-1/VD/Tareas/1/code/2023 Car Dataset.csv")

# Filtrar los datos por las marcas Toyota, Mazda y Honda
car_data_filtered = car_data[car_data['Car Make'].isin(['Toyota', 'Mazda', 'Honda'])]

# Calcular la cantidad de autos eléctricos por marca
electric_cars_count = car_data_filtered[car_data_filtered['Fuel Type'] == 'Electric']['Car Make'].value_counts()

# Convertir los valores de la columna Horsepower a enteros
car_data['Horsepower'] = car_data['Horsepower'].astype(int)

# Calcular la potencia promedio por marca
horsepower_avg = car_data_filtered.groupby('Car Make')['Horsepower'].mean()

# Cargar los datos del otro archivo CSV
# Cargar los datos del archivo .xlsx
marca_data = pd.read_excel("C:/Users/Dade/OneDrive - Universidad Técnica Federico Santa María/2024/2024-1/VD/Tareas/1/code/toyota.xlsx")

# Filtrar los datos por las marcas Toyota, Mazda y Honda
marca_data_filtered = marca_data[marca_data['Marca'].isin(['Toyota', 'Mazda', 'Honda'])]

# Obtener los promedios por marca
promedio_marca = marca_data_filtered.set_index('Marca')['Promedio']

# Crear el gráfico de radar
labels = ['Cantidad de autos eléctricos', 'Potencia promedio', 'Promedio marca']
toyota_data = [electric_cars_count.get('Toyota', 0), horsepower_avg.get('Toyota', 0), promedio_marca.get('Toyota', 0)]
mazda_data = [electric_cars_count.get('Mazda', 0), horsepower_avg.get('Mazda', 0), promedio_marca.get('Mazda', 0)]
honda_data = [electric_cars_count.get('Honda', 0), horsepower_avg.get('Honda', 0), promedio_marca.get('Honda', 0)]

num_vars = len(labels)

angles = [n / float(num_vars) * 2 * 3.14159 for n in range(num_vars)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, toyota_data, color='blue', alpha=0.25)
ax.fill(angles, mazda_data, color='green', alpha=0.25)
ax.fill(angles, honda_data, color='red', alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.show()