Binary operations:
x << y is equivalent to x * Math.pow(2, y)



Remove duplicates in an int array

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

