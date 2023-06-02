import torch
import torch.nn as nn
print("the ali")
class Net(nn.Module):
    def __init__():
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(20, 64, 5)
        self.fc1 = nn.Linear(64*5*5, 64)
        self.fc2 = nn.Linear(64, 10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = x.view(-1, 64*5*5)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x    
    
net = Net()

net.load_state_dict(torch.load('model.pth'))
net.eval()
