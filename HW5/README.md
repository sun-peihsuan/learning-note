# BFS

## <原理>
  
    是從根節點開始，沿著樹的寬度遍歷樹的節點
    
    也就是說，要先走訪完一層之後才會往下一層走訪。如果所有節點均被存取，則演算法中止
  
## <流程圖>
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/BFS.JPG)

# DFS

## <原理>
  
    沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支
    
    當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點
    
    這一過程一直進行到已發現從源節點可達的所有節點為止
  
## <流程圖>
![image](https://github.com/sun-peihsuan/learning-note/raw/master/image/DFS.JPG)
