import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class ToUpperCaseTest{

	@Test
	public void testThatTheFunctionOnlyTakesString(){

	Input userInput = new Input();

	String theString = userInput.ToUpper();
	
	assertEquals(theString, "");
	}
}
