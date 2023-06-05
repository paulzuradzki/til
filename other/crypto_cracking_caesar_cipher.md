# Caesar Cipher

A primer on cracking the Caesar cipher using relative frequency analysis and the chi-squared statistic.

## Background
The Caesar cipher -- also known as a substitution cipher -- is a simple cipher where you encode a text string by shifting the letters by some agreed upon shift number. The cipher is named after Julius Caesar who reportedly used the cipher to protect military messages.

* For example, if the key was 3, encoding the letter `'a'` would map to `'d'`, `'b'` maps to `'e'`, and so on. 
  * Shifting 3 forward from a later letter like `'y'` can wrap around to the beginning of the alphabet
  * `'y'` shifted by 3 maps to `'b'` (`y -> z -> a -> b`).

* You decode an encoded string by reverse shifting using the key.

* To crack the cipher by brute force: try every shift key for each letter in the alphabet and see which decoded string most resembles natural language (e.g., English). This is still quite manual.

* Detecting English
  * There is an automated approach to detecting whether a string of text resembles a language. We can compare the distribution of observed letters to a standard "expected" distribution of letters. 

  * E.g., the most common letter used in English text is the letter `'e'`. If a string was encoded using a Caesar cipher, the most commonly occurring letter would most likely have been mapped from `'e'`.
  * However, even valid English text won't always follow the expected distribution. 
    * E.g., we can find the most commonly occuring letter in an encoded string, assume it was shifted from `'e'`, then apply that shift value to the whole text.
    * While that would be a good guess, `'e'` may not actually be the most frequently occuring letter in the original message despite being the most commonly used in general English.

  * We want some other [less strict] way to score similarity. One of these is the chi-squared statistic. Chi-squared captures information about the similarity between two categorical distributions; we can use it to detect English.
    * The details of chi-squared are not important for our purposes except to know that a lower value corresponds to a greater similarity between two distributions.
    * tl;dr - you can use a chi-squared *test* to estimate whether an observed frequency pattern is likely to have come from another distribution. These hypothesis tests involve statistical table lookups or software that calculates area-under-the-curve integrals with respect to a cutoff value.
    * For this example, we just need the statistic itself.
    * Seeking the lowest chi-squared will be our scoring procedure. Specifically, the cipher shift key that produces the lowest chi-squared statistic is the one that most likely resembles English.

<br>

___

<br>

## Example

Let's encode the string `'hello world'` using a shift key of 3.

```python
import caesar

c = caesar.Cipher()
c.encode("hello world", 3) # => 'khoor zruog'
```

Let's say we receive the encoded string `'khoor zruog'`, we are the intended receiver, and we have the shift key: 3. We can decode by shifting the letters in the opposite direction.

```python
c.encode("khoor zruog", -3) # => 'hello world'
```

<br>

What if we do not know the shift key? 
* We can use brute force and visually inspect the results of trying each shift key. 
* Below, we can see that where `n==3` (`n` being shift key), the decoded text most looks like English (`"hello world"`). 

```python
encoded_text = "khoor zruog"

for n in range(0, 26):
    print(f'n: {n}, decoded text, {n}): {c.encode(encoded_text, -n)}')

# n: 0, decoded text, 0: khoor zruog
# n: 1, decoded text, 1: jgnnq yqtnf
# n: 2, decoded text, 2: ifmmp xpsme
# n: 3, decoded text, 3: hello world
# n: 4, decoded text, 4: gdkkn vnqkc
# n: 5, decoded text, 5: fcjjm umpjb
# n: 6, decoded text, 6: ebiil tloia
# n: 7, decoded text, 7: dahhk sknhz
# n: 8, decoded text, 8: czggj rjmgy
# n: 9, decoded text, 9: byffi qilfx
# n: 10, decoded text, 10: axeeh phkew
# n: 11, decoded text, 11: zwddg ogjdv
# n: 12, decoded text, 12: yvccf nficu
# n: 13, decoded text, 13: xubbe mehbt
# n: 14, decoded text, 14: wtaad ldgas
# n: 15, decoded text, 15: vszzc kcfzr
# n: 16, decoded text, 16: uryyb jbeyq
# n: 17, decoded text, 17: tqxxa iadxp
# n: 18, decoded text, 18: spwwz hzcwo
# n: 19, decoded text, 19: rovvy gybvn
# n: 20, decoded text, 20: qnuux fxaum
# n: 21, decoded text, 21: pmttw ewztl
# n: 22, decoded text, 22: olssv dvysk
# n: 23, decoded text, 23: nkrru cuxrj
# n: 24, decoded text, 24: mjqqt btwqi
# n: 25, decoded text, 25: lipps asvph
```

That is still a bit manual. How can we use properties of general English to do this? 

First we need an expected set of frequencies. You can estimate these yourself by doing counts on your own collections of texts or look them up online. The interpretation of the mapping below is that the letter `a` is expected to comprise 8.34% of any text; the 1.54% for the letter `b` and so on.

<br>

Expected frequencies
```bash
> c.standard_freqs
{'a': 0.0834,
 'b': 0.0154,
 'c': 0.0273,
 'd': 0.0414,
 'e': 0.126,
 'f': 0.0203,
 'g': 0.0192,
 'h': 0.0611,
 'i': 0.0671,
 'j': 0.0023,
 'k': 0.0087,
 'l': 0.0424,
 'm': 0.0253,
 'n': 0.068,
 'o': 0.077,
 'p': 0.0166,
 'q': 0.0009,
 'r': 0.0568,
 's': 0.0611,
 't': 0.0937,
 'u': 0.0285,
 'v': 0.0106,
 'w': 0.0234,
 'x': 0.002,
 'y': 0.0204,
 'z': 0.0006}
 ```

* Next, we will try each shift key from 0-25 (for each letter in the alphabet) and decode the encoded text by shifting in the opposite direction. The resulting text may or may not resemble English. 
* Let's try assuming that a shift key of 4 was used to produce the encoded string `'khoor zruog'`. We know from earlier that the shift key was actually 3 (applied to `'hello world'`). If we try to decode `'khoor zruog'` using a shift key of 4 (encode with -4), the resulting string is `'gdkkn vnqkc'`. Gibberish! 
* We can visually see that `'khoor zruog'` is not English. How can we apply a statistical measurement of this? 
* We will calculate the relative frequencies of each letter in the alphabet in our decoded string like below.

<br>

Observed frequencies
 ```python
 # same as c.get_freqs('gdkkn vnqkc')
>  c.get_freqs(c.encode('khoor zruog', -4))
{'a': 0.0,
  'b': 0.0,
  'c': 0.09090909090909091,
  'd': 0.09090909090909091,
  'e': 0.0,
  'f': 0.0,
  'g': 0.09090909090909091,
  'h': 0.0,
  'i': 0.0,
  'j': 0.0,
  'k': 0.2727272727272727,
  'l': 0.0,
  'm': 0.0,
  'n': 0.18181818181818182,
  'o': 0.0,
  'p': 0.0,
  'q': 0.09090909090909091,
  'r': 0.0,
  's': 0.0,
  't': 0.0,
  'u': 0.0,
  'v': 0.09090909090909091,
  'w': 0.0,
  'x': 0.0,
  'y': 0.0,
  'z': 0.0}
 ```

Interpretation of the observed frequency counts for the text string `'gdkkn vnqkc'`: 
* The letter 'c' has a relative frequency of 9.09%. The letter 'c' appears once and our string has 11 characters: `1/11 =>  0.0909`. 
* The zeroes are for letters in the alphabet that do not appear in our string at all.
* The remaining non-zero values are the same as the calcualtion that we did for 'c'. Count up the # of appearances of the letters divided by the total length of the string.


 Now we have two frequency distributions: 
 * The observed distribution for `'gdkkn vnqkc'` and the expected distribution in general English. 
 * We will use the formula for the chi-squared statistic below.

<br>

*Chi-Squared Statistic*

$$
\begin{equation}
\chi^2 = \sum_{i=1}^{n} \frac{(O_i - E_i)^2}{E_i}
\end{equation}
$$

<br>

This can be interpretted as: *"Take the sum of the squared differences between the observed (O) and expected (E) values divided by the expected value."* 
  * We take the squared differences because adding up equal positive and negative differences would result in a difference of 0, which we don't want. In other words, a negative plus a positive difference of equal amounts are still 2 differences that we want to measure.
  * By dividing each squared difference by the expected value, we are standardizing the difference regardless of their size. 
    * To say it differently, say you got overcharged a $1 on a $100 sale of a fancy dinner. This is a relatively small overcharge, but if you were charged an extra $1 on a $2 pack of gum, that same $1 difference is a bit more suspicious (relatively). Standardizing the $1 based on the size of the transaction makes the difference more comparable regardless of transaction size. 

<br>

In Python, we can calculate the chi-square statistic with a function like so:

```python
def chi_square(observed_list, expected_list):
    return sum([((o - e)**2 / e) for o, e in zip(observed_list, expected_list)])
```

<br>

Again, we have our observed and expected frequencies. This time, the letters are removed and we keep just the percentages sorted by alphabetical position.

```bash
> observed_list = c.get_freqs(c.encode('khoor zruog', -4)).values()
> dict_values([0.0, 0.0, 0.09090909090909091, 0.09090909090909091, 0.0, 0.0, 0.09090909090909091, 0.0, 0.0, 0.0, 0.2727272727272727, 0.0, 0.0, 0.18181818181818182, 0.0, 0.0, 0.09090909090909091, 0.0, 0.0, 0.0, 0.0, 0.09090909090909091, 0.0, 0.0, 0.0, 0.0])

> expected_list = c.standard_freqs.values()
> expected_list
dict_values([0.0834, 0.0154, 0.0273, 0.0414, 0.126, 0.0203, 0.0192, 0.0611, 0.0671, 0.0023, 0.0087, 0.0424, 0.0253, 0.068, 0.077, 0.0166, 0.0009, 0.0568, 0.0611, 0.0937, 0.0285, 0.0106, 0.0234, 0.002, 0.0204, 0.0006])
```

For each frequency value in both lists, we will use this part of the formula for chi-squared. We are omitting the summation for now:

$$
\frac{(O_i - E_i)^2}{E_i}
$$

On the first iteration -- positon 0 in the observed and expected lists, corresponding to letter `'a'` --  we have `(0.0 - 0.0834)^2 / 0.0834 = 0.0834`. We will proceed with this for letters `'b'` through `'z'` and add up the results.

The decoded string `'gdkkn vnqkc'` produces a chi-squared statistic of `19.1121`. The string `'gdkkn vnqkc'` was produced by reversing `khoor zruog` -- the string we're trying to decipher -- with a shift key of 4, which we know to be incorrect. 

If we write a loop to calculate chi-squared and decode the text for each shift key from 0-25, we get the following results. We will sort the results from lowest to highest chi-squared values. A lower chi-squared value imprecisely meaning:  "more likely to be English" or "more closely matches the distribution of general English".

Below we can see that our algorithm fails. A shift key of 6 gets the lowest chi-squared value (1.966) when we know the real shift key was 3. We can still see that the correct shift key still appears in the top 5 results. With shorter text (like `'hello world'`), this statistical test is less reliable. However, we can see that our initial incorrect guess of `'gdkkn vnqkc'` using a shift key of 4 appears further down the sorted list indicating that it was not a good guess.

```bash
Chi-Square calculations
        {'shift_key': 6, 'chi_square': 1.9663524105806363, 'decoded': 'ebiil tloia'}
        {'shift_key': 14, 'chi_square': 2.073667594908809, 'decoded': 'wtaad ldgas'}
        {'shift_key': 3, 'chi_square': 2.264050321066854, 'decoded': 'hello world'}
        {'shift_key': 12, 'chi_square': 5.253802697840998, 'decoded': 'yvccf nficu'}
        {'shift_key': 22, 'chi_square': 5.374265654262933, 'decoded': 'olssv dvysk'}
        {'shift_key': 25, 'chi_square': 5.535200833787072, 'decoded': 'lipps asvph'}
        {'shift_key': 10, 'chi_square': 6.344987296476867, 'decoded': 'axeeh phkew'}
        {'shift_key': 2, 'chi_square': 8.976048877413229, 'decoded': 'ifmmp xpsme'}
        {'shift_key': 19, 'chi_square': 9.160260021134738, 'decoded': 'rovvy gybvn'}
        {'shift_key': 13, 'chi_square': 9.245896676545522, 'decoded': 'xubbe mehbt'}
        {'shift_key': 23, 'chi_square': 10.750430891178485, 'decoded': 'nkrru cuxrj'}
        {'shift_key': 21, 'chi_square': 16.246988711404853, 'decoded': 'pmttw ewztl'}
        {'shift_key': 0, 'chi_square': 16.30902489454178, 'decoded': 'khoor zruog'}
        {'shift_key': 9, 'chi_square': 17.789689767546975, 'decoded': 'byffi qilfx'}
        {'shift_key': 16, 'chi_square': 18.251072819610155, 'decoded': 'uryyb jbeyq'}
        {'shift_key': 7, 'chi_square': 18.5280436538918, 'decoded': 'dahhk sknhz'}
        {'shift_key': 4, 'chi_square': 19.11210314975558, 'decoded': 'gdkkn vnqkc'}
        {'shift_key': 11, 'chi_square': 21.30723216038879, 'decoded': 'zwddg ogjdv'}
        {'shift_key': 20, 'chi_square': 28.45721611789728, 'decoded': 'qnuux fxaum'}
        {'shift_key': 8, 'chi_square': 32.38237662334605, 'decoded': 'czggj rjmgy'}
        {'shift_key': 5, 'chi_square': 34.8614926737347, 'decoded': 'fcjjm umpjb'}
        {'shift_key': 1, 'chi_square': 41.93021386634819, 'decoded': 'jgnnq yqtnf'}
        {'shift_key': 17, 'chi_square': 46.85936597754077, 'decoded': 'tqxxa iadxp'}
        {'shift_key': 18, 'chi_square': 58.63481643782736, 'decoded': 'spwwz hzcwo'}
        {'shift_key': 24, 'chi_square': 87.11165679411226, 'decoded': 'mjqqt btwqi'}
        {'shift_key': 15, 'chi_square': 126.77665394673753, 'decoded': 'vszzc kcfzr'}
```

Let's try this procedure on a longer string. Here is our encoded text. For simplifying assumptions, we'll assume that the text is lower-cased prior to being encoded. We will ignore non-alphabetical characters.


Encoded text
```
qfoqywbu qcrsg kwhv ghohwghwqoz awuvh,
qvw-geiofs hsghg obr qosgof'g qwdvsf ibwhs.
tfseisbqm obozmgwg, dohhsfbg sasfus,
vwrrsb asggousg, w'zz eiwqyzm ifus.

gvwthsr zshhsfg, gsqfshg hvsm vczr,
kwhv ghohwghwqoz hcczg, hvswf ghcfm ibtczrg.
rsqcrwbu amghsfwsg, cbs pm cbs,
ibjswzwbu gsqfshg, hvs fwrrzs wg rcbs.

kvoh oa w?
```

Cracking the code. 
* The method `Cipher.decipher()` implements the procedure that we described.
* *"try each shift key and return the decoded message that produces the lowest chi-squared statistic"*.

```python
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

c = Cipher()

encoded_text = "qfoqywbu qcrsg kwhv ghohwghwqoz awuvh,\nqvw-geiofs hsghg obr qosgof'g qwdvsf ibwhs.\ntfseisbqm obozmgwg, dohhsfbg sasfus,\nvwrrsb asggousg, w'zz eiwqyzm ifus.\n\ngvwthsr zshhsfg, gsqfshg hvsm vczr,\nkwhv ghohwghwqoz hcczg, hvswf ghcfm ibtczrg.\nrsqcrwbu amghsfwsg, cbs pm cbs,\nibjswzwbu gsqfshg, hvs fwrrzs wg rcbs.\n\nkvoh oa w?"

most_likely_shift_key, deciphered = c.decipher(encoded_text.lower())

logging.info(f"Most likely shift key: {most_likely_shift_key}")    
logging.info(f"Best-guess deciphered text:\n\n{deciphered}")

```

Log Output
```
Most likely shift key: 14
Best-guess deciphered text:

cracking codes with statistical might,
chi-square tests and caesar's cipher unite.
frequency analysis, patterns emerge,
hidden messages, i'll quickly urge.

shifted letters, secrets they hold,
with statistical tools, their story unfolds.
decoding mysteries, one by one,
unveiling secrets, the riddle is done.

what am i?
```
<br>

___

<br>

### Resources

For more programming practice or historical reading on introductory cryptography, see:

#### [*Cracking Codes with Python* by Al Sweigart](https://inventwithpython.com/cracking/)
* This is also a solid Python beginner programming book. I often recommend [*Automate the Boring Stuff*](http://automatetheboringstuff.com/) by the same author to beginners (just look past the camel case).
* *Cracking Codes* is great practice with text manipulation and basic data structures.
* Sweigart uses a different frequency analysis scoring procedure in lieu of chi-squared. See [`englishFreqMatchScore()`](https://inventwithpython.com/cracking/chapter19.html).

<br>

#### [*The Code Book* by Simon Singh](https://www.amazon.com/dp/0385495323) (432 pages)

* This is a no-code (well, no-programming-code) introduction to cryptography. It's one of my favorites in non-fiction. 
* You will go from basic Caesar ciphers and spy stories, to WWII and the Enigma machine, and all the way to a good layperson's intro to public-private (aka, asymmetric) key cryptography which is used heavily in modern security (e.g, the digital handshakes behind authentication and securing credentials and sensitive payment data). 

<br>

#### [*The Code Breakers* by David Khan](https://www.amazon.com/dp/0684831309) (1200 pages)
I have not gotten around to reading Code Breakers yet. It's got good reviews and I keep seeing it come up in citations.
