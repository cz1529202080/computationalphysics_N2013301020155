{\rtf1\ansi\ansicpg936\cocoartf1404\cocoasubrtf130
{\fonttbl\f0\fnil\fcharset134 PingFangSC-Regular;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs22 \cf0 \CocoaLigature0 \'ca\'fd\'d6\'b5\'bd\'e2\'b3\'cc\'d0\'f2
\f1 \
N_peo=[]\
t=[]\
a=10\
dt=10\
N_peo.append(1000)\
t.append(0)\
end_time=100\
for i in range(int(end_time/dt)):\
    m=N_peo[i]+a*N_peo[i]*dt\
    N_peo.append(m)\
    t.append (dt*(i+1))\
    print t[-1],N_peo[-1]\
import numpy as np\
import matplotlib.pyplot as plt\
plt.plot(t,N_peo)\
plt.show()\
\

\f0 \'bd\'e2\'ce\'f6\'bd\'e2\'b3\'cc\'d0\'f2
\f1 \
x=np.arange(0,100,10);\
y=1000*np.exp(10*x)\
plt.plot(x,y)\
plt.show()}