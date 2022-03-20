import torch

from torch import nn 

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.cnn = nn.Sequential(
            nn.Conv2d(1, 10, kernel_size=5),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.ReLU(),

            nn.Conv2d(10, 20, kernel_size=5),
            nn.Dropout2d(0.2),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Flatten(),
        )

        self.fc = nn.Sequential(
            nn.Linear(320, 50),
            nn.ReLU(),
            nn.Linear(50, 10),
            nn.Softmax(1),
        )
    
    def forward(self, x):
        return self.fc(self.cnn(x))

net = Net()
x = torch.randn((1, 1, 28, 28))
print(net(x))
