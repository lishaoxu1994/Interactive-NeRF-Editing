import torch.nn as nn
import torch
class Grid_fun(nn.Module):
    def __init__(self):
        super().__init__()
        self.DEGREE = 5
        self.a = torch.rand([96,3], requires_grad=True)
        self._parameters = dict(a=self.a)
    def forward(self, x):
        device = x.device
        x = torch.cat([x,torch.ones(x.shape[0],1).to(device)],1)
        y = None
        z = None
        all = None
        for i in range(0, self.DEGREE + 1):
            for j in range(0,4):
                if z is None:
                    z = x.clone()
                if y is None:
                    y = torch.mul(z,z[:,j:j+1].repeat(1,4))
                else:
                    y = torch.cat([y,torch.mul(z,z[:,j:j+1].repeat(1,4))],1)
            if all is None:
                all = y.clone()
            else:
                all = torch.cat([all,y],1)
            z = None
            y = None            

        #y = torch.cat([y**i for i in range(0,self.DEGREE + 1)], 1)

        out = torch.mm(all,self.a.to(device))

        return out
    

if __name__=='__main__':
    device = 'cuda:1'
    x = torch.rand([100,3]).to(device)
    net = Grid_fun()
    y = net(x)
