

class Add {
    void add(int... args) {
        int sum = 0;
        String plus=""; //from the discussion 
        for (int i : args) {
            System.out.print(plus+i);
            plus="+";
            sum += i;
        }
        System.out.println("=" + sum);
    }
}

