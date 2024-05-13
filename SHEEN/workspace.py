def miarrsum(miarr,zero):
  arrsumss = 0
  if len(miarr) >=2:
    if len(miarr) % 2 == 0:
        for miarrr in range(0,len(miarr),2):
          arrsumss+= (miarr[miarrr] * miarr[miarrr+1])
    else:    
        for miarrr in range(1,len(arr),2):
          arrsumss+= (miarr[miarrr] * miarr[miarrr-1])  
          print(arrsumss)  
        if len(zero) > 0:
               pass
        else:
           arrsumss += miarr[-1]          
  elif len(miarr) == 1:
        if len(zero) > 0:
               pass
        else:
           arrsumss += miarr[0]       
  else:
     return arrsumss  
  
  miarr = [-11,-10,-9,-5,-2]
  