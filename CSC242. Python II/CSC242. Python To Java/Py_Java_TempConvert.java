/*
Python CSC242
TempConvert Class()

To Execute Program run Command Prompt
> javac Py_Java_TempConvert.java
> java Py_Java_TempConvert
*/

import java.util.Scanner;

public class Py_Java_TempConvert {
	
	public static void main(String args[]){
		
		double _fahr, _cel;
		Scanner sc;
		
		sc = new Scanner(System.in);
		System.out.print("Enter Temp in F: ");
		_fahr = sc.nextDouble();
		
		_cel = (_fahr -32) * 5.0/9.0;
		
		System.out.println(String.format("Temperature in C: %.2f", _cel));
	}
}
