import torch
from torch import nn
from torchvision import models
import torch.nn.init as init

class LSTM(nn.Module):
    def __init__(self):
        super(LSTM, self).__init__()
        load_layer = {'conv1','bn1','relu','maxpool',
                      'layer1','layer2','layer3','layer4','avgpool'}
        resnet = models.resnet50(pretrained=True)
        self.feature_extractor = nn.Sequential()
        for name, layer in resnet.named_children():
            if name in load_layer:
                self.feature_extractor.add_module(name,layer)
        self.lstm = nn.LSTM(2048, 512, batch_first=True)
        self.fc = nn.Linear(512, 7)

        init.xavier_normal_(self.lstm.all_weights[0][0])
        init.xavier_normal_(self.lstm.all_weights[0][1])
        init.xavier_uniform_(self.fc.weight)

    def forward(self,x):
        x = self.feature_extractor(x)
        x = x.view(-1, 1, 2048)
        x, _ = self.lstm(x)
        x = x.contiguous().view(-1, 512)
        x = self.fc(x)

        return x

class ResNet(nn.Module):
    def __init__(self):
        super(ResNet, self).__init__()
        self.res = models.resnet50(pretrained=True)
        self.res.fc = nn.Linear(2048, 7)
        init.xavier_uniform_(self.res.fc.weight)

    def forward(self, x):
        x = self.res(x)
        return x

class LSTM_ResNet(nn.Module):
    def __init__(self):
        super(LSTM_ResNet, self).__init__()
        load_layer = {'conv1', 'bn1', 'relu', 'maxpool',
                      'layer1', 'layer2', 'layer3', 'layer4', 'avgpool'}
        resnet = models.resnet50(pretrained=True)
        self.feature_extractor = nn.Sequential()
        for name, layer in resnet.named_children():
            if name in load_layer:
                self.feature_extractor.add_module(name, layer)

        # LSTM
        self.lstm = nn.LSTM(2048, 512, batch_first=True)
        self.lstm_fc = nn.Linear(512, 7)
        # ResNet
        self.resnet_fc = nn.Linear(2048, 7)

        init.xavier_normal_(self.lstm.all_weights[0][0])
        init.xavier_normal_(self.lstm.all_weights[0][1])
        init.xavier_uniform_(self.lstm_fc.weight)
        init.xavier_uniform_(self.resnet_fc.weight)

    def forward(self, x):
        x = self.feature_extractor(x)
        x = x.view(-1, 1, 2048)

        # LSTM
        lstm_out, _ = self.lstm(x)
        lstm_out = lstm_out.contiguous().view(-1, 512)
        lstm_out = self.lstm_fc(lstm_out)

        # ResNet
        resnet_out = self.resnet_fc(x.squeeze(1))

        return resnet_out, lstm_out
    
class LSTM_ResNet_CL(nn.Module):
    def __init__(self):
        super(LSTM_ResNet_CL, self).__init__()
        load_layer = {'conv1', 'bn1', 'relu', 'maxpool',
                      'layer1', 'layer2', 'layer3', 'layer4', 'avgpool'}
        resnet = models.resnet50(pretrained=True)
        self.feature_extractor = nn.Sequential()
        for name, layer in resnet.named_children():
            if name in load_layer:
                self.feature_extractor.add_module(name, layer)

        # LSTM
        self.lstm = nn.LSTM(2048, 512, batch_first=True)
        self.lstm_fc = nn.Linear(512, 7)
        # ResNet
        self.resnet_fc1 = nn.Linear(2048, 512)
        self.resnet_fc2 = nn.Linear(512, 7)

        # p2t
        self.p2t_fc = nn.Linear(512, 7)

        self.relu = nn.ReLU()

        init.xavier_normal_(self.lstm.all_weights[0][0])
        init.xavier_normal_(self.lstm.all_weights[0][1])
        init.xavier_uniform_(self.lstm_fc.weight)
        init.xavier_uniform_(self.resnet_fc1.weight)
        init.xavier_uniform_(self.resnet_fc2.weight)
        init.xavier_uniform_(self.p2t_fc.weight)

    def forward(self, x):
        x = self.feature_extractor(x)
        x = x.view(-1, 1, 2048)

        # LSTM
        y, _ = self.lstm(x)
        y = y.contiguous().view(-1, 512)
        lstm_out = self.lstm_fc(self.relu(y))

        # ResNet
        resnet_out = self.resnet_fc1(x.squeeze(1))
        resnet_out = self.resnet_fc2(self.relu(resnet_out))

        # p2t
        p2t_out = self.p2t_fc(self.relu(y))

        return resnet_out, lstm_out, p2t_out