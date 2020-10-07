# Amplified-Caesar-Cipher(ACC)
## Created by Rushi Ranade
Amplified Caesar-Cipher, also called n-4Shift encryption, is an encryption method first created by Rushi A Ranade, an HarvardX student, from India. It is derived from Caesar-Cipher. Caesar Cipher or Shift Encryption is encryption in which the letters shift by a number x. For example, ABC will become DEF, when the shift or x is 3. But decrypting this was easily possible. Thus, an amplified way was needed. n-4Shift suits the need perfectly.
***
As you know there are 26 letters in the English alphabet. n-4Shift takes a shift of 4 at the beginning and for each letter multiplies the shift by n, and when shift * n results in a number greater than 26, it does (shift - n) * n. Let's take an example of ABCD with n as 2. A will get a shift of 4, B will be 4 * 2 = 8, C will be 8 * 2 = 16 and finally D. 16 * 2 = 32 which is greater than 26, so D will be (16 - 2) * 2 = 28. Resulting in EJSF.
***
Note: Decryption needs a password... I have set it to EJSF...the encrypted form of ABCD.
