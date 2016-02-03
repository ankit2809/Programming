public class Factorial 
{
	
	public static void main (String [] args)
	{ 
		System.out.print(facto(5));
				
	}
	
	public static int facto(int x)
	{
		if (x>1)
			return x*facto(x-1);
		else
			return 1;
		
	}
	
	
}