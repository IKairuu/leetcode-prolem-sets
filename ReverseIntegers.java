
class Solution {
    public int reverse(int x){
        try
        {
            String num = Integer.toString(x) ;
            String answer = "" ;
            StringBuilder sb = new StringBuilder(answer) ;
            for (int a = num.length()-1 ; a >= 0 ; a--)
            {
                if (num.charAt(a) == '-')
                {
                    sb.insert(0, '-') ;
                }
                else
                {
                    sb.append(num.charAt(a)) ;
                }
            }
            String createString = sb.toString() ;
            int createInt = Integer.parseInt(createString) ;
            return createInt ;
        }
        catch (NumberFormatException a)
        {
            return 0 ;
        } 
    }
}
