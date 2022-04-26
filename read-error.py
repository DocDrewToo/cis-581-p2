import matplotlib.pyplot as plt


test_error_file = open('test_err_rate.dat', 'r+')
test_error = []
for line in test_error_file:
    test_error.append(float(line.strip()))
test_error_file.close()

train_error_file = open('train_err.dat', 'r+')
train_error = []
for line in train_error_file:
    train_error.append(line.strip())
train_error_file.close()

number_of_iterations = len(test_error)
iterations = []
for iteration in range(1, number_of_iterations+1):
    iterations.append(iteration)

plt.plot(test_error, label="Test")
plt.plot(train_error, label="Train")
# plt.xlabel('Iterations')
# plt.ylabel('Error')
plt.show()