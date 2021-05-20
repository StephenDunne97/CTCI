class isUnique{
    static boolean isUnique(String word){ 
        for(int i=0; i<word.length(); i++){
            int count = 0;
            for(int j=0; j<word.length(); j++){
                if(word.charAt(i) == word.charAt(j)){
                    count++;
                    if(count > 1){
                        System.out.println(word + " is not unique.");
                        return false;
                    }
                }
            }
        }
        System.out.println(word + " is unique.");
        return true;
    }
    public static void main(String args[]) {
        isUnique("Hello");       
        isUnique("Dog");
    }
}