hetro_elements = ['1',1,2,'a','abc','cba']
int_elements = [element for element in hetro_elements if type(element)== int]
non_int_elements = [element for element in hetro_elements if type(element) != int]

print("hetro_elements: ", hetro_elements)
print('int_elements: ', int_elements)
print('non_int_elements: ', non_int_elements)

