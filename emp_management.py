import logging
import json
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample collections to represent databases
Employee_Collection = []
Hash_1234 = []

# Function to create a new collection
def create_collection(name):
    logging.info(f"Collection '{name}' has been successfully created.")
    return []

# Function to index data into the collection
def index_data(collection, data, exclude_columns=None):
    if exclude_columns is None:
        exclude_columns = []
    for row in data:
        indexed_data = {k: v for k, v in row.items() if k not in exclude_columns}
        collection.append(indexed_data)
    logging.info(f"Data indexed into collection excluding columns {exclude_columns}.")

# Function to add a new employee
def add_employee(collection, employee_data):
    required_fields = ['Employee ID', 'Full Name', 'Job Title', 'Department', 'Business Unit', 'Gender', 'Ethnicity', 'Age', 'Hire Date']
    if all(field in employee_data for field in required_fields):
        collection.append(employee_data)
        logging.info(f"Employee {employee_data['Employee ID']} added to collection.")
    else:
        logging.error("Failed to add employee: Missing required fields.")

# Function to update an employee
def update_employee(collection, emp_id, updated_data):
    for emp in collection:
        if emp['Employee ID'] == emp_id:
            emp.update(updated_data)
            logging.info(f"Updated employee details for ID '{emp_id}'.")
            break
    else:
        logging.warning(f"No employee found with ID '{emp_id}'.")

# Function to delete an employee
def delete_employee(collection, emp_id):
    for emp in collection:
        if emp['Employee ID'] == emp_id:
            collection.remove(emp)
            logging.info(f"Employee with ID '{emp_id}' has been deleted.")
            break
    else:
        logging.warning(f"No employee found with ID '{emp_id}'.")

# Function to find employees by department
def find_employees_by_department(collection, department):
    results = [emp for emp in collection if emp['Department'] == department]
    logging.info(f"Records found in collection for department '{department}': {results}")
    return results

# Function to find employees by gender
def find_employees_by_gender(collection, gender):
    results = [emp for emp in collection if emp['Gender'] == gender]
    logging.info(f"Records found in collection for gender '{gender}': {results}")
    return results

# Function to get department counts
def get_department_counts(collection):
    counts = Counter(emp['Department'] for emp in collection)
    logging.info(f"Department counts in collection: {counts}")
    return counts

# Function to export data to JSON
def export_to_json(collection, filename):
    with open(filename, 'w') as f:
        json.dump(collection, f, indent=4)
    logging.info(f"Data exported to {filename}.")

# Main Menu Function
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View Employees")
        print("5. Export to JSON")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp_data = {
                'Employee ID': input("Enter Employee ID: "),
                'Full Name': input("Enter Full Name: "),
                'Job Title': input("Enter Job Title: "),
                'Department': input("Enter Department: "),
                'Business Unit': input("Enter Business Unit: "),
                'Gender': input("Enter Gender: "),
                'Ethnicity': input("Enter Ethnicity: "),
                'Age': input("Enter Age: "),
                'Hire Date': input("Enter Hire Date (YYYY-MM-DD): ")
            }
            add_employee(Employee_Collection, emp_data)

        elif choice == '2':
            emp_id = input("Enter Employee ID to update: ")
            updated_data = {}
            updated_data['Full Name'] = input("Enter updated Full Name: ")
            updated_data['Job Title'] = input("Enter updated Job Title: ")
            updated_data['Department'] = input("Enter updated Department: ")
            updated_data['Business Unit'] = input("Enter updated Business Unit: ")
            updated_data['Gender'] = input("Enter updated Gender: ")
            updated_data['Ethnicity'] = input("Enter updated Ethnicity: ")
            updated_data['Age'] = input("Enter updated Age: ")
            updated_data['Hire Date'] = input("Enter updated Hire Date (YYYY-MM-DD): ")
            update_employee(Employee_Collection, emp_id, updated_data)

        elif choice == '3':
            emp_id = input("Enter Employee ID to delete: ")
            delete_employee(Employee_Collection, emp_id)

        elif choice == '4':
            for emp in Employee_Collection:
                print(emp)

        elif choice == '5':
            filename = input("Enter filename to export (with .json extension): ")
            export_to_json(Employee_Collection, filename)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

# Initialize collections
Employee_Collection = create_collection("Employee_Collection")
Hash_1234 = create_collection("Hash_1234")

# Sample data to index (replace this with your CSV data as needed)
sample_data = [
    {
        'Employee ID': 'E02001',
        'Full Name': 'Kai Le',
        'Job Title': 'Controls Engineer',
        'Department': 'Engineering',
        'Business Unit': 'Manufacturing',
        'Gender': 'Male',
        'Ethnicity': 'Asian',
        'Age': '47',
        'Hire Date': '2022-05-02'
    },
    {
        'Employee ID': 'E02002',
        'Full Name': 'Anna Smith',
        'Job Title': 'Software Developer',
        'Department': 'IT',
        'Business Unit': 'Technology',
        'Gender': 'Female',
        'Ethnicity': 'Caucasian',
        'Age': '29',
        'Hire Date': '2021-06-15'
    },
    {
        'Employee ID': 'E02003',
        'Full Name': 'John Doe',
        'Job Title': 'Data Analyst',
        'Department': 'IT',
        'Business Unit': 'Technology',
        'Gender': 'Hispanic',
        'Ethnicity': 'Hispanic',
        'Age': '34',
        'Hire Date': '2020-01-12'
    },
    {
        'Employee ID': 'E02004',
        'Full Name': 'Jane Roe',
        'Job Title': 'Marketing Specialist',
        'Department': 'Marketing',
        'Business Unit': 'Sales',
        'Gender': 'Female',
        'Ethnicity': 'Black',
        'Age': '28',
        'Hire Date': '2019-03-11'
    },
    {
        'Employee ID': 'E02005',
        'Full Name': 'Chris Green',
        'Job Title': 'HR Manager',
        'Department': 'Human Resources',
        'Business Unit': 'Corporate',
        'Gender': 'Male',
        'Ethnicity': 'Caucasian',
        'Age': '42',
        'Hire Date': '2018-07-22'
    },
    {
        'Employee ID': 'E02006',
        'Full Name': 'Emily White',
        'Job Title': 'Web Designer',
        'Department': 'IT',
        'Business Unit': 'Technology',
        'Gender': 'Female',
        'Ethnicity': 'Asian',
        'Age': '31',
        'Hire Date': '2023-08-30'
    },
]

# Index sample data
index_data(Employee_Collection, sample_data)

# Start the main menu
if __name__ == "__main__":
    main_menu()
