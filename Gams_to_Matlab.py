# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
def split(string):
    return re.split("([+-])",string.replace(' ',''))

prog  = 'function [lb, ub, A, b, Aeq, beq, Initial_Guess, fit_handle, NLC_handle] =  '
func_name = raw_input('Enter the program name')
prog = prog + func_name + '\n'

prog = prog + 'fit_handle = @'+ func_name + '_ObjFn; \n'
prog = prog + 'NLC_handle = @'+ func_name + '_NL_Con; \n'
prog = prog + 'function objvar = '+ func_name +'_ObjFn(x)\n  end \n' 
prog = prog + 'function [c,ceq] = '+ func_name +'_NL_Con(x)\n  end \n end'

print prog
c=''
ceq = ''
itr = 1
itr2 = 1

size = raw_input('Enter the size: ')
st = ''
for x in range(1,int(size)):
    st = st + 'x'+str(x)+'=x(' + str(x) + ');'
print st
x = raw_input('Enter the equations : ')
x = x.replace('\n','')
eq = x.split(';')
Aeq = '['
Beq = '['
A = '['
B = '['
for l in eq:
    print l
    if('objvar' in l):
        eqno = raw_input('Enter the equation Number:')
        l = l.replace('e'+str(eqno)+'..','')
        l = l.replace('=E= 0','')
        l = l.replace(' + objvar ','')
        print 'objvar = ' + l + ';'
    else:
        if('E' in l):
            
            opt = raw_input('Is it coefficient separable ? ')
            if(opt == '1'):
                eqno = raw_input('Enter the equation Number:')
                l = l.replace('e'+str(eqno)+'..','')
                for x in range(0,int(size)+1):
                    if('x'+str(x) in l):
                        i = l.index('x'+str(x))
                        if(not l[i+len(str(x)) +1].isdigit()):
                            j = i
                            while(l[j]!=' '):
                                j = j - 1
                            if(i-j == 1):
                                if(l[j-1] == '+'):
                                    Aeq = Aeq + ' ' + str(1)
                                else:
                                    Aeq = Aeq + ' ' + str(-1)
                            else:
                                Aeq = Aeq + ' ' +str(l[j+1:i-1])
                    else:
                        Aeq = Aeq + ' 0'
  
              
                Aeq = Aeq + ';'
                k = l.split('=E=')
                bcoff = k[-1]
                Beq = Beq + bcoff + ';'
            else:
                eqno = raw_input('Enter the equation Number:')
                l = l.replace('e'+str(eqno)+'..','')
                temp = l.split('=E=')
                c = c + 'Ceq(' + str(itr)+ ') =' + str(temp[-2]) + ';'
                itr2 = itr2 + 1
                
        if('G' in l or 'L' in l):
            opt = raw_input('Is it coefficient separable ? ')
            if(opt == '1'):
                eqno = raw_input('Enter the equation Number:')
                l = l.replace('e'+str(eqno)+'..','')
                
                for x in range(0,int(size)+1):
                    if('x'+str(x) in l):
                        i = l.index('x'+str(x))
                        if(not l[i+len(str(x)) +1].isdigit()):
                            j = i
                            while(l[j]!=' '):
                                j = j - 1
                            if(i-j == 1):
                                if(l[j-1] == '+'):
                                    A = A + ' ' + str(1)
                                else:
                                    A = A + ' ' + str(-1)
                            else:
                                A = A + ' ' +str(l[j+1:i-1])
                    else:
                        A = A + ' 0'
                A = A + ';'
                if('G' in l ):
                    k = l.split('=G=')
                if('L' in l ):
                    k = l.split('=L=')

                bcoff = k[-1]
                B = B + bcoff + ';'
            else:
                eqno = raw_input('Enter the equation Number:')
                l = l.replace('e'+str(eqno)+'..','')
                if('G' in l ):
                    temp = l.split('=G=')
                    c = c + 'c(' + str(itr)+ ') =' + str(temp[-2]) + ';'
                    itr = itr + 1
                if('L' in l ):
                    temp = l.split('=L=')
                    c = c + 'c(' + str(itr) + ')' + str(temp[-2]) + ';'
                    itr = itr + 1
                    
            
            
            
            
print c

Aeq = Aeq + ']'
Beq = Beq + ']'

A = A + ']'
B = B + ']'
A = A[:-2] + A[-1]
B = B[:-2] + B[-1]
Aeq = Aeq[:-2] + Aeq[-1]
Beq = Beq[:-2] + Beq[-1]

print 'Aeq = '+ Aeq
print 'Beq = ' +Beq
print 'A = ' + A
print 'B =' + B

print "Variables for upper and lower limit " 
lim = raw_input('Enter the variable limits ')
print "Variables for fz"
fx = raw_input('Enter the fx ')

lim = lim.replace('\n','')
fx = fx.replace('\n','')

fzlim = fx.split(';')
limits = lim.split(';')


lb = ['a' for x in range(int(size))]
ub = ['a' for x in range(int(size))]

pv = raw_input('Enter the positive variable')
for x in range(1,int(size)+1):
    if('x'+str(x) in pv):
        lb[x-1] = 0
        

for x in range(1,int(size)+1):
     for f in fzlim:
         if('x'+str(x)+'.fx' in f):
             temp = f.split('=')
             lb[x-1] =  int(temp[-1])
             ub[x-1] =  int(temp[-1])
        
for x in range(1,int(size)+1):
    for q in limits:
        if('x'+str(x)+'.lo' in q):
            temp = q.split('=')
            lb[x-1] =  int(temp[-1])
        if('x'+str(x)+'.up' in q):
            temp = q.split('=')
            ub[x-1] =  int(temp[-1])
            

for x in range(1,int(size)+1):
    if(lb[x-1] == 'a'):
        lb[x-1] = 'LB_UB(1)'
    if(ub[x-1] == 'a'):
        lb[x-1] = 'LB_UB(2)'
    
print 'lb = ' ,lb
print 'ub = ' ,ub

print "Variables for initial guess " 
lim = raw_input('Enter the variable guess ')

lim = lim.replace('\n','')

limits = lim.split(';')

ub = '['
for q in limits:
    for x in range(1,int(size)+1):
        if('x'+str(x)+'.l' in q):
            temp = q.split('=')
            ub = ub + temp[-1] + ','
            

ub = ub + ']'

ub = ub[:-2] + ub[-1]

ub = ub + ';'

print 'Initial_Guess = ' + ub

        





              
                
                
