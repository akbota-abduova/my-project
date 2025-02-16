import json

# Открываем JSON-файл и загружаем данные
with open("C:/Users/user/Desktop/pp2/my-project/lab4/json/sample-data.json", "r") as file:
    data = json.load(file)

# Получаем список интерфейсов
interfaces = data.get("imdata", [])

# Вывод заголовка
print("Interface Status")
print("=" * 65)
print(f"{'DN':<50} {'Admin State':<12} {'Speed':<10} {'MTU':<5} {'Switching State':<15}")
print("-" * 65)

# Проходим по каждому интерфейсу и выводим данные
for item in interfaces:
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    
    dn = attributes.get("dn", "N/A")
    admin_state = attributes.get("adminSt", "N/A")
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
    switching_state = attributes.get("switchingSt", "N/A")
    
    print(f"{dn:<50} {admin_state:<12} {speed:<10} {mtu:<5} {switching_state:<15}")

# Сохраняем выход в файл
with open("output.txt", "w") as out_file:
    out_file.write("Interface Status\n")
    out_file.write("=" * 65 + "\n")
    out_file.write(f"{'DN':<50} {'Admin State':<12} {'Speed':<10} {'MTU':<5} {'Switching State':<15}\n")
    out_file.write("-" * 65 + "\n")
    
    for item in interfaces:
        attributes = item.get("l1PhysIf", {}).get("attributes", {})
        dn = attributes.get("dn", "N/A")
        admin_state = attributes.get("adminSt", "N/A")
        speed = attributes.get("speed", "N/A")
        mtu = attributes.get("mtu", "N/A")
        switching_state = attributes.get("switchingSt", "N/A")
        
        out_file.write(f"{dn:<50} {admin_state:<12} {speed:<10} {mtu:<5} {switching_state:<15}\n")

print("Выходной файл создан: output.txt")
