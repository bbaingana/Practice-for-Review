import re
import pandas as pd
import matplotlib.pyplot as plt

red_counter = 0
yellow_counter = 0
blue_counter = 0
results_list = ['Blue', 'Blue', 'Red', 'Yellow..', 'Red', 'Blue', 'Blue', 'Blue', 'Yellow121', 'Red/', 'RED123']

for str in results_list:
    valid_answer = re.sub(r'[^A-Za-z]+', '', str)
    valid_answer = valid_answer.lower()

    if valid_answer == 'red':
        red_counter += 1
    elif valid_answer =='yellow':
        yellow_counter += 1
    elif valid_answer == 'blue':
        blue_counter += 1
    else:
        print('Sorry, Try Again.')

results_dict = {"Red": red_counter, 'Yellow': yellow_counter, 'Blue': blue_counter}
names = list(results_dict.keys())
values = list(results_dict.values())

plt.bar(range(len(results_dict)), values, tick_label = names)
plt.title('Favorite Primary Colors')
plt.ylabel('Number of Students')
plt.xlabel('Colors')
plt.show()
