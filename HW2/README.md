#　Heap sort 

## <原理>
若以升序排序說明，把陣列轉換成Max-Heap Heap

對於除了根之外的每個節點i, A[parent(i)] ≥ A[i]。

重複從最大堆積取出數值最大的結點(把根結點和最後一個結點交換，把交換後的最後一個結點移出堆)，並讓殘餘的堆積維持最大堆積性質。

## <流程圖>
![image](https://github.com/sun-peihsuan/learning-note/raw/master/image/heap%20sort.jpg)

#　Merge sort

## <原理>

分割：遞迴地把目前序列平均分割成兩半。

整合：在保持元素順序的同時將上一步得到的子序列整合到一起（合併）。

## <流程圖>
![image](https://github.com/sun-peihsuan/learning-note/raw/master/image/merge_sort.jpg)
