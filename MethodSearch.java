import java.util.regex.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.util.List;
import java.util.ArrayList;

/**
********Notes********
*For now just try hard coding in the regex, later include a file that will contain them
*Try to think of a way that will improve the run time of the function 
*
***Current Status***
*Can search a text file for a pattern
*
***Methods Needed***
* 1. Read File
* 2. Compare line of byte code to regex pattern
* 3. Create patterns
*
**/

public class MethodSearch {
	
	public static void search(String fileName) {
		
		List<String> f = readFile(fileName); //iterate over a file, save as a list?
		
		regexMatches(f); //search it for a string
	}
	
	public static List<String> readFile(String filename){

		List<String> records = new ArrayList<String>();
		
		try{
			BufferedReader reader = new BufferedReader(new FileReader(filename));
			String line;
			while ((line = reader.readLine()) != null){
				records.add(line);
	
		    }
		    reader.close();
		    return records;
		}
		  
		catch (Exception e){
			System.err.format("Exception occurred trying to read '%s'.", filename);
		    e.printStackTrace();
		    return null;
		}
	}
	
	public static void regexMatches(List<String> l) {
		
		int count = 0; //create counter
		
	    //String pattern = "aload"; // String to be scanned to find the pattern.
		String pattern = "java\\/io.+";	//gets all the java/io methods
		//String pattern = "([a-z])\\w+";
		
	    Pattern r = Pattern.compile(pattern); // Create a Pattern object
	    
	    for (int i=0; i<l.size(); i++) {
	    	String line = l.get(i);
	    	Matcher m = r.matcher(line); // Now create matcher object.
			if (m.find( )) {
				System.out.println("Found value: " + m.group(0) );
				//System.out.println("Found value: " + m.group(1) );
			    //System.out.println("Found value: " + m.group(2) );
				count++;
			}
		}
	    System.out.println(count);
	}		
}
