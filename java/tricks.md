Binary operations:
x << y is equivalent to x * Math.pow(2, y)



Change an array to a set (remove duplicates)

```java
int[] array = new int[] {1, 1, 4, 5, 6, 7, 4};
Integer[] array2 =  {1, 34,4,5 ,56};
//change array to a list then change to a set(remove duplicates)
Set<Integer> set1 = new HashSet<Integer>(Arrays.stream(array)
                                         .boxed() //box the primitive type to wapper class
                                         .sorted()
                                         .collect(Collectors.toList()));

Set<Integer> set2 = new HashSet<Integer>(Arrays.toList(array2));
```

Change a set to an array

```java
T[] array = mySet.toArray(new T[mySet.size()]);
```

change int array to Integer array

``` java
int[] array = new int[] {1, 1, 4, 5, 6, 7, 4};
Integer[] newArray = Arrays.stream(array)
    						.boxed()
    						.collect(Collectors.toList());
```

## sort 

sort an array

```java
Arrays.sort(myArray);
Arrays.sort(myArray, startIdx, endIdx);
Array.sort(myArray, Collections.reverseOrder());
```

sort a list

```java 
// Integer list
List<Integer> nums = Arrays.asList(1,3,4,54,4);
nums.sort(Comparator.naturalOrder());
nums.sort(Comparator.reverseOrder());

// String list
List<String> stringList = Array.asList("ny", "nj", "fl", "ca");
stringList.sort(String.CASE_INSENSITIVE_ORDER); //ignore cases
stringList.sort(Comparator.naturalOrder());

// Object list
List<Movie> movies = Array.asList(new Movie("Rings"), new Movie("Back to the future"), new Movie("Matrix"));
movies.sort(Comparator.comparing(Movie::getTitle));
```



Fill an array with same numbers

```java
Arrays.fill(myArray, 10);
Arrays.fill(myArray, 1, 5, 10); // (array, startIdx, endIdx, element)
```

create an array with index

```java 
// method 1
Arrays.setAll(myArray, i -> i);

// method 2
int[] array = IntStream.range(1, 100).toArray();
```



## sum

sum of array elements (average() method can also apply)

```java
Array.stream(myArray).sum(); // int[] myArray
Array.stream(myArray).maptoInt(Integer::intValue).sum(); // Integer[] myArray
```

## 

sum of list elements

```java
List<Integer> integers = Arrays.asList(1, 3, 4, 5, 5);
// method 1
Integer sum = integers.stream()
    				  .reduce(0, (a, b) -> a + b);
Integer sum = integers.stream()
    			      .reduce(0, Integer::sum);
// method 2
Integer sum = integers.stream()
    				  .collect(Collectors.summingInt(Integer::intValue));

// method 3
Integer sum = integers.stream()
    				  .mapToInt(Integer::intValue)
    				  .sum();
```



## DataType Conversion

char array to String

```java
char[] chars = {'a', 'b', 'c'};
String str = new String(chars);
```

String to char array

```java
String str = "abc";
char[] chars = str.toCharArray();
```

char to String

```java
char c = 'a';
String s = String.valueOf(c);
```

string to char

```java
char c = s.charAt(0);
```



## ASCII conversion

check if a char is lower

```java
String S = "World";
System.out.println(Character.isLetter(S.charAt(0)));

// if there is only alphanumeric
// in ascii, 'a' represent 97, 'A' represent 65
// if a char is alphanumeric and larger or equal than 65, it is a lowercase letter.
System.out.println(S.charAt(0) - 'a' >= 0)
```

