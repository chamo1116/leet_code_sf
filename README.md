# Leetcode Exercise.

## Statement.

Given a string s, find the length of the longest substring	without repeating characters.

### Example 1.

Input: s = "abcabcbb"

Output: 3

Explanation: The answer is "abc", with the length of 3.

### Example 2.

Input: s = "bbbbb"

Output: 1

Explanation: The answer is "b", with the length of 1.

### Example 3.

Input: s = "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints:

0 <= s.length <= 5 * 10^4

s consists of English letters, digits, symbols and spaces.


## Detailed Implementation.

- Before implement the solution first validate the constraints with the following code:

```
# Validate contraints
if not s or len(s) > 50000:
    raise ValueError("The length of the string should be less than 50000")
```

where it's raised a `ValueError` exception if the length is greater than 50000

- Next need to initialize our variables that will be changed thoughtout the iteration:
```
# Create variables to store last item and max_length
seen_characters = {}
max_length = 0
# starting the initial point of window to index 0
start = 0
```

- Start the iteration and check if we already seen the element, if so, change the start point calculating the maximium with itself and the index where was found plus 1 (because indexes in python start in 0):

```
# Checking if we have already seen the element
current_character = s[current_index]

if current_character in seen_characters:
    # If we have seen the number, move the start pointer
    # to position after the last occurrence
    start = max(start, seen_characters[current_character] + 1)
```

- Finally, update the last value seen and recalculate the maximium length with the current_index and the start point (previously updated) plus 1 (for the previous reason):

```
# Updating the last seen value of the character
seen_characters[current_character] = current_index
max_length = max(max_length, current_index - start + 1)
```

## Performance.

### Time complexity.
It is `O(n+d)` where `n` is the length of the input string and `d` is number of characters in input string. In this case, the  string consists of lowercase English characters, digits, ascii symbols and spaces, so `d` would be:

```
(26 + 10 + 128 + 1) = 165.
```

### Space complexity.
It is O(d) where d was calculated previously.



## Run The Solution.

The solution of this problem was implemented in a cli and it's dockerized. 

To test the solution, just run this command:

```
docker build -t substring --rm . && docker run -it --name my_substring --rm substring python3 main.py --string=pwwkew
```

where just need to change the input string in the parameter --string and will get the result printed in the screen:

```
The length of the longest substring is 3!
```
