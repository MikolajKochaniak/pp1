import random
class Arrays():
    @staticmethod
    def method_one(number_of_array_elements, value_of_array_elements):
        arr = []
        for i in range(number_of_array_elements):
            arr.append(value_of_array_elements)
        return arr
    def method_two(number_of_array_elements, value_from, value_to):
        arr = []
        for i in range(number_of_array_elements):
            random_number = random.randint(value_from,value_to)
            arr.append(random_number)
        return arr
    def method_three(array, value_from, value_to):
        arr = []
        for i in range(array):
            arr.append(random.randint(value_from,value_to))
        return arr

            

print(Arrays.method_one(6,5))
print(Arrays.method_two(5,5,10))
print(Arrays.method_three(5,5,10))