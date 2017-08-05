package agosto;

//Les traigo el método de ordenación mas ineficiente. Pero el mas sencillo de aprender. El método Burbuja.
public class Ordenamiento 
{	
	public void burbuja(int[] A) 
	{
		//Primeramente muestro los números desordenados.
		for(int y:A)
			System.out.print(y+" ");
		
		int i, j, aux;
		//Comparamos cada elemento con el adyacente. Después de varias iteraciones se encontrarán ordenados.
		for (i = 0; i < A.length - 1; i++) 
		{
			for (j = 0; j < A.length - i - 1; j++) 
			{
				if (A[j + 1] < A[j]) 
				{
					//Usamos una variables auxiliar para guardar temporalmente algunos números.
					//Para comprenderlo más, en Google hay información gráfica.
					aux = A[j + 1];
					A[j + 1] = A[j];
					A[j] = aux;
				}
			}
		}
	
		//Los mostramos de manera ordenada.
		System.out.println();
		for(int x:A)
			System.out.print(x+" ");
	}
	
	//Con este método generamos un array de números. Aquí genero 10,000 y esto funciona "rápido", pero intenta con 1,000,000, se tornaría lento, 
	//para esto existen otros métodos ordenamiento como quicksort.
	public int[] generarNumeros()
	{
		int numeros []=new int[10000];
		try
		{
			for(int i=0;i<numeros.length;i++)
				numeros[i]=(int)(Math.random()*10000);
			
		}catch(Exception e){e.getMessage();};
		
		return numeros;
	}
	
	public static void main(String[] args) 
	{
		Ordenamiento o=new Ordenamiento();
		o.burbuja(o.generarNumeros());
	}

}
