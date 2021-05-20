import java.util.Arrays;

public class Permutation {
    static String sortString(String s1){
        char tempArray[] = s1.toCharArray();
        Arrays.sort(tempArray);
        return new String(tempArray);
    }
    static void isPermutation(String s1, String s2){
        boolean perm = True;
        s1 = sortString(s1);
        s2 = sortString(s2);
    }
    public static void main(String args[]){
        String s1 = "abc";
        String s2 = "cba";
        String s3 = "baa";
        isPermutation(s1,s2);
        isPermutation(s1,s3);
    }
}