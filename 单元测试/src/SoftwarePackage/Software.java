package SoftwarePackage;

public class Software{
	public void PopSort(int nums[]) {
	//简单冒泡排序
		for(int i=0;i<nums.length;i++) {
			for (int j=nums.length-1;j>i;j--) {
				if (nums[j]>nums[j-1]) {
					int tem = nums[j - 1];
					nums[j-1] = nums[j];
					nums[j] = tem;
				}
			}
		}
	}
	
	public int Add(int a,int b) {
		//简单加法
		return a+b;
	}
	
	public int Cost(int a, int b) {
		return a-b;
	}
	
	public int Mul(int a,int b) {
		return a*b;
	}
}
