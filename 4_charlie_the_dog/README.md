# Charlie the Dog

Have the function CharlietheDog(strArr) read the array of strings stored in strArr which will be a 4x4 matrix of the characters 'C', 'H', 'F', 'O', where C represents Charlie the dog, H represents its home, F represents dog food, and O represents and empty space in the grid. Your goal is to figure out the least amount of moves required to get Charlie to grab each piece of food in the grid by moving up, down, left, or right, and then make it home right after. Charlie cannot move onto the home before all pieces of food have been collected. For example: if strArr is ["FOOF", "OCOO", "OOOH", "FOOO"], then this looks like the following grid:

![dog](https://user-images.githubusercontent.com/49286935/201458051-400e834f-2e7a-483b-9e8e-8fcd284553f8.png)

Example Path -> down, down, left*, up, up, up*, right, right, right*, down, down

For the input above, the least amount of steps where the dog can reach each piece of food, and then return home is 11 steps, so your program should return the number 11. The grid will always contain between 1 and 8 pieces of food.

## Examples

Input: 
[
    "OOOO",
    "OOFF",
    "OCHO",
    "OFOO"
 ]

Output: 7

Example path -> down*, right, right, up, up*, left*, down

Input:
 
[
    "FOOO",
    "OCOH",
    "OFOF",
    "OFOO"
]

Output: 10

Example path -> up, left*, down, down, right*, down*, right, up, right*, up