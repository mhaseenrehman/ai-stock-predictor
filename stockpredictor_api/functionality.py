"""
PyTorch AI Stock Prediction Mechanisms - Predict closing price for stock

Linear Regression
Logistic Regression
Long Short Term Memory Gate

"""

import torch
import numpy as np

# ----------------------------------------------- ML Algorithms ----------------------------------------------

class LinearRegressionModel(torch.nn.Module):
    def __init__(self, inputSize, outputSize):
        super(LinearRegressionModel, self).__init__()
        self.layer1 = torch.nn.Linear(inputSize, 250)
        self.layer2 = torch.nn.Linear(250, 100)
        self.layer3 = torch.nn.Linear(100, outputSize)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        x = self.layer3(x)
        return x

def linear_regression(dataset):
    # 0) Setup
    result = None
    window = 30
    output = 5
    learningRate = 0.01
    epochs = 1000
    
    # 1) Process data
    #x_train, y_train, x_test, y_test = linear_regression_process_data(dataset, window, output)
    x_train, y_train, x_test = linear_regression_process_data(dataset, window, output)

    # 2) Instantiate Model
    model = LinearRegressionModel(int(window*4), int(output))
    if torch.cuda.is_available():
        model.cuda()
    
    # 3) Train model loop
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)
    for epoch in range(epochs):
        outputs = model(x_train)
        loss = criterion(outputs, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print("epoch", epoch, "\n")
    
    print("Completed Training")
    
    # 4) Test Model
    with torch.no_grad():
        test_outputs = model(x_test)
    
    # 5) Make Prediction
    predictions = test_outputs[-1].cpu().numpy()
    result = predictions

    # 6) Return result
    return result

# --------------------------------------------- Helper Functions ---------------------------------------------

def linear_regression_process_data(dataset, window=30, output=5):
    # 80:20 train, test dataset split
    split = int(0.8*len(dataset))

    # Convert to numpy & Take only the values: open, high, low, close
    raw_data = dataset.to_numpy()
    raw_data = raw_data[:, :4]

    # Split into train, test datasets
    train = raw_data[:split]
    test = raw_data[split:]

    # Windowed Training - Train on one month at a time and predict 5 days into the future
    N = len(train)
    stock_data = []
    for w in range(window, N-output+1):
        open1, high1, low1, close1, = np.array(train[w-window:w]).T.tolist()
        open2, high2, low2, close2, = np.array(train[w:w+output]).T.tolist()
        stock_data.append([open1+high1+low1+close1, close2])

    data = [torch.tensor(data_item[0], dtype=torch.float32) for data_item in stock_data]
    result = [torch.tensor(data_item[1], dtype=torch.float32) for data_item in stock_data]
    
    stock_train_data = torch.stack(data)
    stock_train_result = torch.stack(result)

    if torch.cuda.is_available():
        stock_train_data.cuda()
        stock_train_result.cuda()
    
    # Windowed Test - Test again on a small subset of dates for stock prices
    t1, t2, t3, t4 = np.array(test[-window:]).T.tolist()
    test_data = torch.tensor(t1+t2+t3+t4, dtype=torch.float32)
    stock_test_data = torch.stack((test_data,))
    if torch.cuda.is_available():
        stock_test_data.cuda()
    #stock_test_result = t4

    # Return result
    return stock_train_data, stock_train_result, stock_test_data #stock_test_result


# -------------------------------------------- Initiate Algorithm --------------------------------------------

def initiate_prediction(dataset, algorithm):
    result = None
    if algorithm == "lin_reg":
        print("ALGORITHM: LINEAR REGRESSSION STARTING")
        result = linear_regression(dataset)
        print("ALGORITHM: LINEAR REGRESSSION COMPLETED")
    elif algorithm == "LSTM":
        pass
    else:
        print("INVALID ALGORITHM")
    return result
