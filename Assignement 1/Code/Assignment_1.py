
import random as rd

sample_data = 100000

list_of_sample = [[rd.randint(0 , 1) , rd.randint(0 , 1)]]

i = 1
for i in range(sample_data):
    list_of_sample.append([rd.randint(0 , 1), rd.randint(0 , 1)])
    # 0 corresponds to head
    # 1 corresponds to tail
i = 0
count = 0
for i in range(sample_data):
    if (list_of_sample[i] == [1,1]):
        count += 1
probalility_of_two_tails = count / sample_data
probability_of_at_least_one_head = 1 - probalility_of_two_tails


print("Following results are obtained from the simulation")
print("Probability of atleast one head : {}".format(probability_of_at_least_one_head))

print("Following results are obtained theoretically")
print("Probability of atleast one head : 0.75")

print()
print("Following are the absolute errors in calculating probabilties")
print("Absolute error in calculating probability: {}".format(abs(probability_of_at_least_one_head - 0.75)))
print("As the errors are extremely small, we can conclude that both sets of results are approximately the same")