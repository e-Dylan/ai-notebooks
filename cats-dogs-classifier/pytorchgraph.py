import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

model_name = "model-1593639189"

def create_acc_loss_graph(model_name):
    contents = open("C:/Users/Dylan/Desktop/build/python_projects/ai-notebooks/catsdogs-net/model.log", "r").read().split("\n") # get each line of the model log file in /currentdir
    
    times = []

    accuracies = []
    losses = []

    val_accs = []
    val_losses = []

    for c in contents:
        if model_name in c:
            name, timestamp, acc, loss, val_acc, val_loss = c.split(",")

            # fill lists with their associated data from every line in model file
            times.append(float(timestamp))

            accuracies.append(float(acc))
            losses.append(float(loss))

            val_accs.append(float(val_acc))
            val_losses.append(float(val_loss))

    # graph each data set on y, x = time.
    fig = plt.figure() # define multiple graphs

    ax1 =  plt.subplot2grid((2, 1), (0, 0)) # x-axis
    ax2 =  plt.subplot2grid((2, 1), (1, 0), sharex = ax1) # y-axis

    ax1.plot(times, accuracies, label = "acc") # in-sample training accuracy
    ax1.plot(times, val_accs, label = "val_acc") # out of sample data accuracy, testing during training
    ax1.legend(loc = 2) 

    ax2.plot(times, losses, label = "loss") # in-sample training loss
    ax2.plot(times, val_losses, label = "val_loss") # out of sample data loss, testing during training
    ax2.legend(loc = 2)

    plt.show()  


create_acc_loss_graph(model_name)