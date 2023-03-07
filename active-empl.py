import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('employees.xml')
root = tree.getroot()

# Loop through the employee elements and check for the "active" tag
for employee in root.findall('employee'):
    if employee.get('type') == 'active':
        # Print the employee details
        print('Name:', employee.find('name').text)
        print('Age:', employee.find('age').text)
        print('Salary:', employee.find('salary').text)
        print('-----------------')
