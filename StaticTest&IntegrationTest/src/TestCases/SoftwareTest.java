package TestCases;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import SoftwarePackage.Software;

class SoftwareTest {

	@Test
	void testPopSort() {
		Software testcase = new Software();
		int[] input = {3,6,7,8,2,9};
		testcase.PopSort(input);
		int[] exceptresult = {9,8,7,6,3,2};
		//数组不能直接比较,首先判断长度
		assertEquals(input.length,exceptresult.length);
		//再逐个判断里面的值
		for(int i=0;i<input.length;i++) {
			assertEquals(input[i],exceptresult[i]);
		}
	}

	@Test
	void testAdd() {
		assertEquals(5,new Software().Add(3, 2));
	}

	@Test
	void testCost() {
		assertEquals(1,new Software().Cost(3, 2));
	}

	@Test
	void testMul() {
		assertEquals(6,new Software().Mul(3, 2));
	}

}
