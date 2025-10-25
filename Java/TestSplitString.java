import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestSplitString{


@Test
public void testThatTheStringExistsAndItReturnsAnArray(){

	SplitString user = new SplitString();
	
	String [] result = user.myString("my string");

	assertEquals("", "", result[0]);
	assertEquals("my", result[0]);
	assertEquals("string", result[1]);
	}

}