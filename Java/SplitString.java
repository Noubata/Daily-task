public class SplitString {

    public String[] myString(String word) {
        if (word.equals("")) {
            return new String[] {""};
        }

        return word.split(" ");
    }

}