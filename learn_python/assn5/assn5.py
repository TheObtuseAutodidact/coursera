"""
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475";

start = text.find("0")
ans = text[start:]
ans = float(ans)
print ans
"""
Desired Output
0.8475
"""
