To encrypt the string, we need to rotate the alphabets in the string by a number k. If k is a multiple of 26, then rotating the alphabets in the string by k has no effect on the string. Rotation by k is same as rotation by k+26. So by taking modulo of k with 26, we get the number of times we need to rotate the alphabets of the string. To rotate the alphabets in a string by a value k, we add k to the character. If this value exceeds the range of the alpabets, we need to wrap it back. The range of uppercase characters is from 65 ('A') to 90 ('Z'). The range of lowercase characters is from 97 ('a') to 122 ('z').
Example: For the string : "middle-Outz" and k=2
We add 2 to 'm'. 'm' becomes 'o'. This value is within the ascii range so we don't need to wrap it. '-' remains unaltered. 'z' on adding 2 becomes 124. This value lies outside the range of lowercase characters. We need to wrap this value. By taking the modulo of this value with 122, and adding this value to 96('a'-1) we get the rotated character.

For lowercase characters,

// Let char c = s[i] be a lowercase character in the string.
k = k % 26;
c += k;
if(c > 122) {
    c = 96 + (c % 122);
}