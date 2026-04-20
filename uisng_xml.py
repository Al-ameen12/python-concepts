import xml.etree.ElementTree as ET

# data = '''
# <person>
#     <name>Al-ameen</name>
#     <role>Software Developer</role>
#     <location>Lagos</location>
# </person>
# '''

# tree = ET.fromstring(data)

# print(tree.find('name').text)
# print(tree.find('role').text)
# print(tree.find('location').text)

tree = ET.parse('students_log.xml')
root = tree.getroot()

for student in root.findall('student'):
    name = student.find('name').text
    department = student.find('department').text
    school = student.find('school').text
    print(f'Name: {name}, Department: {department}, School: {school}')