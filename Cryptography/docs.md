# Pseudorandom Generator (PRG) and Statistical Tests

## Basic PRG Definition
- G: {0,1}^s → {0,1}^n
- G: K → {0,1}^n
- Let G: K → {0,1}^n be a PRG

---

## Statistical Test on {0,1}^n

- A statistical test is an algorithm A(x)
- A(x) outputs:
  - "0" → input is **not random**
  - "1" → input is **random**

### Common properties of random strings:
- Number of 0's is nearly equal to number of 1's
- Number of "00" patterns ≈ n / 4
- Maximum run of 0's ≈ log₂(n)

---

## Examples of Statistical Tests

1. **Balance Test**
   - A(x) = 1
     if and only if
     |#0(x) - #1(x)| ≤ 10 * sqrt(n)

2. **Consecutive Zeros Test**
   - A(x) = 1
     if and only if
     |#00(x) - n/4| ≤ 10 * sqrt(n)

3. **Run-Length Test**
   - A(x) = 1
     if and only if
     max_run_of_0(x) ≤ 10 * log₂(n)

---

## Notes

- Many more statistical tests exist.
- Tests are **not perfect** — some might falsely say a non-random string is random.
- In older methods, a battery of such tests was used to decide if a generator is "good".
