with open('input.in') as f:
    my_input = f.read()

def start_packet(data, number):
    for i in range(len(data)-number):
        if len(set(data[i:i+number])) == number:
            return i+number
            break

print(start_packet(my_input,4))
print(start_packet(my_input,14))