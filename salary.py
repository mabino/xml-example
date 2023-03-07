import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('employees.xml')
root = tree.getroot()

# Loop through the employee elements and check for salary of 50000 or more
for employee in root.findall('employee'):
    salary = int(employee.find('salary').text)
    if salary >= 50000:
        # Print the employee details
        print('Name:', employee.find('name').text)
        print('Age:', employee.find('age').text)
        print('Salary:', salary)
        print('-----------------')
