class Solution(object):
  s=[]
  def h(gg):
      n=len(gg)
   
      for i in range(n,-1,-1):
          f=i
          l=(i*2)+1
          r=(i*2)+2
          if l<n:
              if gg[f]>gg[l]:
                  gg[f],gg[l]=gg[l],gg[f]
          if r<n:
              if gg[f]>gg[r]:
                  gg[f],gg[r]=gg[r],gg[f]

      s.append(gg[0])
      gg[0]=gg[-1]
      gg.pop(-1)
    
      if len(gg)>0:
          gg=h(gg)
        
      return s
