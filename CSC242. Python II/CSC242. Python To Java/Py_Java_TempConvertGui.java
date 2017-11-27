/*
Python CSC242
TempCovertGUI Class()

To Execute run Command Prompt
> javac Py_Java_TempConvertGUI.java
> java Py_Java_TempConvertGUI
*/

import javax.swing.JOptionPane;

public class Py_Java_TempConvertGui{
	
	public static void main(String args[]){
		
		//instantiating variables
		String _inpValue;
		Double _fahr, _cel;
		
		_inpValue = JOptionPane.showInputDialog("Enter Temp in F");
		
		_fahr = new Double(_inpValue);
		
		_cel = (_fahr -32) * 5.0/9.0;
		
		JOptionPane.showMessageDialog(null, "Temperature in C: " + _cel);
	}
}
