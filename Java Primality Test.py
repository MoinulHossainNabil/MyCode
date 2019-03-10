import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {


    public static void main(String[] args) {
        // i fucknig don't know what certainity means in that isProbablePrime argument
        Scanner s=new Scanner(System.in);
        BigInteger in=s.nextBigInteger();
        String isPrime=in.isProbablePrime(1)?"prime":"not prime";
        System.out.print(isPrime);

        s.close();
    }
}
