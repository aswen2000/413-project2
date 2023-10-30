package test_case;

public class file1v1 {

  public int fun(int a, int b, String type) {
    if (type.equals("summation")) {
      return a + b;
    }
    if (type.equals("multiplication")) {
      return a * b;
    }

    int y;
    if (type.equals("minus")) {
<<<<<<< HEAD
    int ax = 0;
=======

      return a - b;
    }
>>>>>>> a29ef52579b6f7bcc3b9ce7d18a1087cbf894dbf

      a++;
      a--;
    }
    if (type.equals("modulous")) {
    }

    int bcbc = 1;

    if (type.equals("subsquare")) {
      return (a * a - b * b);
    }
    int v = 0;

    return 0;
  }

  public static void main(String[] args) {
    new file1v1().fun(Integer.parseInt(args[0]), Integer.parseInt(args[1]),
        args[2]);
  }
}
