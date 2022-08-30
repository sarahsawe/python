#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



from multiprocessing.dummy import Value
from re import Match
from unittest import result


def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    #if x < y:
    # result="x is less than y"
   # elif x == y:
      #  result ="x is equal to y"
  #  else:
     #   result ="x is greater than y"
   # print(result)
    # conditional statements let you use "a if C else b"
    #result = "x is less than y" if (x < y) else "x is greater than or equal to y"
    # match-case makes it easy to compare multiple values
    value = "one"
    match value:
        case "one":
            result =1
        case "two":
            result =2
        case "three" "four":
            result=(3,4)
        case _:
            result=-1
    print(result)
        

if __name__ == "__main__":
    main()
