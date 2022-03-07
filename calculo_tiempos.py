import time

start = time.time()
print("The time used to execute this is given below")
end = time.time()
print(end - start)

# Calculando el tiempo en funciones 

start = time.process_time()
print("This time is being calculated")
end = time.process_time()
print(end - start)