import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    high_paid_employees = []
    for i in range(len(employee)):
        manager_id = employee.iloc[i]["managerId"]
        if pd.notna(manager_id):
            manager_salary = employee[employee["id"] == manager_id]["salary"]
            if not manager_salary.empty and employee.iloc[i]["salary"] > manager_salary.values[0]:
                high_paid_employees.append(employee.iloc[i]["name"])
    result = pd.DataFrame(high_paid_employees, columns=["Employee"])
    return result
