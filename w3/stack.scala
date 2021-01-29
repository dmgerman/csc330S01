import scala.io.StdIn._
import sys.process._
import scala.annotation.tailrec

object  test {


  def printStack = try { 1/0 } catch {
    case ex: Throwable =>
      val stack = ex.getStackTrace drop 1 filter (_.toString.startsWith("Main"))
      stack.reverse.zipWithIndex foreach println
      ();
  }

  def f(i:Int):Int = {
    if (i <= 1) {
      printStack
      1
    } else {
      i*f(i-1)
    }
  }
  
  def main(args:Array[String]):Unit = {
    printStack
    print("----\n")
    f(1);
  }
}



/*
def f2(i:Int):Int = {
  def helper(i:Int, acc:Int):Int = {
    if (i <= 1) {
      printStack
      acc
    } else
        helper(i-1, acc*i)
  }
  printStack
  print("++++\n")
  helper(i,1)
}
 */
